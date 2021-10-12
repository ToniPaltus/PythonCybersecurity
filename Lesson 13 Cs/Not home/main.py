# 1
'''
s = """
RegExr was created by gskinner.com, and is proudly hosted by
Media Temple.
Edit the Expression & <img src='www.lenta.ru'>Text to see matches.
Roll over matches or the <img src='www.lenta.ru'>expression for
details. PCRE & JavaScript flavors of RegEx are supported. Validate
your expression with Tests mode.
The side bar includes a Cheatsheet, full Ref<img
src='www.lenta.ru'>rence, and Help. You can <img
src='www.lenta.ru'>also Save & Share with the Community, and view
patterns you create or favorite in My Patterns.
Explore results with the <img src='www.lenta.ru'>Tools below.
Replace & List output custom results. Details lists capture groups.
Explain describes your expression in plain English.
"""
print(s)
'''

# 2
import re

re.match()
#re.match(pattern, string)#ищет по заданному шаблону в начале строки

re.search()
#re.search(pattern, string)#Метод похож на match(), но ищет по всей строке.
#Возвращает только первое найденное совпадение

re.findall()
#re.findall(pattern, string)#Возвращает список всех найденных совпадений.
#Ищет по всей строке РЕКОМЕНДУЕТСЯ для использования

re.split()
#re.split(pattern, string, [maxsplit=0])# Разделяет строку по заданному шаблону

re.sub()
#re.sub(pattern, repl, string)
#Ищет шаблон в строке и заменяет его на указаннную подстроку.
#Если щаблон не найден, строка остается неизменной

re.compile()
#Формирует регулярное выражение как отдельный объект,
#который может быть использован для поиска
#Это так же избавляет от переписывания одного и того же выражения