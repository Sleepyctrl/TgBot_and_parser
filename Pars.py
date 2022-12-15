# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import sqlite3
from config import URL_TEMPLATE_PAGE_CR

#1-ый уровень Страница Со списком CR
req_cr_page = requests.get(URL_TEMPLATE_PAGE_CR)
soup_cr_page= bs(req_cr_page.text, "html.parser")
cr_page_find=soup_cr_page.find(class_='article-content')
cr_page_find=cr_page_find.contents[9].findAll('a')

connection = sqlite3.connect('Dnd_random_enemies.db')
cursor = connection.cursor()

Count_except=''
Href_except=''
timecounter=1
for i in cr_page_find:
    # Получаем ссылку из начального URL
    URL_TEMPLATE_CR = i.get('href')
    req_cr = requests.get(URL_TEMPLATE_CR)
    soup_cr = bs(req_cr.text, "html.parser")
    href_find= soup_cr.find(class_='flexbox divboxes',)
    # Получаем список всех ссылок внутри начального URL
    allNews = href_find.findAll('a')
    URL_TEMPLATE=''
    for i in allNews:
        
        try:
            #Сразу проспускаем ссылку, если это рекламная ссылка (Помечается как 3РР)
            if(i.contents[0] == '[3PP]'):
                continue
            URL_TEMPLATE=i.get('href')
            req_main = requests.get(URL_TEMPLATE)
            soup_main = bs(req_main.text, "html.parser")

            mob_name = soup_main.find('p',class_='title')
            title = soup_main.find_all_next(class_='title')
            mob_description = soup_main.find(class_='description')
            mob_stats = soup_main.find(class_='statblock')
            
            #Если поле statictics не найдено (разная html структура страниц)
            if(mob_stats==None):
                mob_stats = soup_main.find(class_='article-content')    

            #Если описание не найдено (разная html структура страниц)
            if(mob_description==None):
                try:
                    mob_description = soup_main.find('i').find('span')
                except:
                    pass
            
            str=''
            skip=0
            for outputing in mob_stats:
                #if для пропуска имени и CR (первые два значения в нужном нам классе с информацией)
                if(skip<2):
                    skip+=1
                    continue
                str+=outputing.get_text()

            #иногда встречаются проблемы с кодировкой символов, встречается "â\x80\x9"
            try:
                mob_description=mob_description.contents[0].get_text().encode("ascii","ignore").decode('utf-8')
            except:
                mob_description=''

            try:
                mob_cr=mob_name.contents[1].get_text().encode("ascii","ignore").decode('utf-8')
            except:
                mob_cr=''

            try:
                mob_names=mob_name.contents[0].get_text().encode("ascii","ignore").decode('utf-8')
            except:
                mob_names=''

            Full_page_Mob2=[mob_names,
            mob_cr+" ",
            mob_description,
            str.encode("ascii","ignore").decode('utf-8')]

            sql_create='''CREATE TABLE IF NOT EXISTS Dnd_random_enemies(
                            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            Name_enemy TEXT , 
                            CR_enemy TEXT,
                            Description_enemy TEXT,
                            Details_enemy TEXT)'''

            sql_insert= '''INSERT INTO Dnd_random_enemies
            (Name_enemy, CR_enemy, Description_enemy, Details_enemy) VALUES(?, ?, ?, ?)'''

            with sqlite3.connect('Dnd_random_enemies.db') as connection:
                rows = connection.cursor().execute(sql_create).fetchall()
                rows = connection.cursor().execute(sql_insert,Full_page_Mob2).fetchall()
        except:
            Count_except=+1
            #В текстовый файл отправляются ссылки, которые не смог обработать парсер
            Href_except+= URL_TEMPLATE+'\n'

#Вывод "битых" не обрабатываемых ссылок
str_intext='errors on next href:\n'+Href_except
with open("test.txt","w",encoding="utf-8") as writing_obj:
        writing_obj.write(str_intext)

#Удаляет пустые значения, или значения где есть \n или пробел
sql_delete='''DELETE FROM Dnd_random_enemies WHERE CR_enemy = '' or CR_enemy = ' ' or CR_enemy = '
' or Details_enemy = '' or Details_enemy = '
' or Details_enemy = ' ' or CR_enemy='
 ' or CR_enemy='  ';'''
with sqlite3.connect('Dnd_random_enemies.db') as connection:
        rows = connection.cursor().execute(sql_delete).fetchall()

#Формирует числа формата 001, 010 для более легкой доступности и форматирования бд, так же удаляет ненужные пробелы в поле,
#там где они есть.
for i in range(1,38):
    c=str(f'{i:03}')
    sql_update="UPDATE Dnd_random_enemies Set CR_enemy ='CR {}' WHERE CR_enemy ='CR {}' or CR_enemy = 'CR {} 'or CR_enemy='CR {}  'or CR_enemy='CR {}     '".format(c, i, i, i,i)
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
        rows = connection.cursor().execute(sql_update).fetchall()

#Все монстры у которых половинчатый CR в базе записываются как CR >1
part_of_1=['1/2','1/3','1/4','1/6','1/8','CR 1/8     ','CR 1/4  ','CR 1/2  ']
for i in part_of_1:
    #c=str(f'{i:03}')
    sql_update="UPDATE Dnd_random_enemies Set CR_enemy ='CR >1' WHERE CR_enemy ='CR {} 'or CR_enemy='{}'".format(i,i)
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
        rows = connection.cursor().execute(sql_update).fetchall()

#Приведение к общему форматированию, и редактирование, не корректных полей.
for i in range(1,38):
    c=str(f'{i:03}')

    sql_update="UPDATE Dnd_random_enemies Set CR_enemy ='CR {}' WHERE CR_enemy ='CR {} '".format(c,i)

    #Второй апдейт нужен для особых случаев, когда указывается "CR 15 (Какой-либо текст) или CR 15/MR 23" 
    #пример :Flytrap CR 6 
    sql_update2="UPDATE Dnd_random_enemies Set CR_enemy ='CR {}' WHERE CR_enemy like'%CR {} (%' or CR_enemy like'%CR {}/M%'".format(c,i,i)
    
    #Третий апдейт нужен, чтобы отшлифовать оставшиеся небольшие данные, которые не получилось отловить двумя предыдущими апдейтами
    #и которые содержат лишние слова, как пример "Flytrap CR 6" или "CR 6 Flytrap "
    sql_update3="UPDATE Dnd_random_enemies Set CR_enemy ='CR {}' WHERE CR_enemy Like '%CR {}%'".format(c,i)    
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
        rows = connection.cursor().execute(sql_update).fetchall()
        rows = connection.cursor().execute(sql_update2).fetchall()
        rows = connection.cursor().execute(sql_update3).fetchall()