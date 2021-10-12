import re

# Example 1

text = 'Who will live on Earth in the 21th century?'
result = re.match(r'Who', text)# только в начале строки
print(result)
# Example 2
print(result.group())
print(result.start())
print(result.end())


# Example 3
'''
#Функция search () ищет в строке совпадение и возвращает объект
#Match, если совпадение
text = 'Who will live on Earth in the 21th century?'
result = re.search(r'th', text)
print(result)

#Найдите в строке первый символ пробела
txt = 'The rain in Spain'
x = re.search('\s', txt)
print(x)
print("The first white-space character is located in position:", x.start())

# Выполните поиск, который не возвращает совпадений
x = re.search('Portugal', txt)
print(x)
'''

# Example 4
'''
text = 'Who will live on Earth in the 21th century?'
result = re.findall(r'th', text)
print(result)

txt = 'The rain in Spain'
# Return empty list if coincidences didn't found
x = re.findall('Portugal', txt)
print(x)

# Распечатайте лист полных совпадений
x = re.findall('ai', txt)
print(x)
'''

# Example 5
'''
#Функция split () возвращает список, в котором строка была разделена
#при каждом совпадении:
text = 'Who will live on Earth in the 21th century?'
result = re.split(r'r', text)# Все возможные участки
print(result)

# Разделить на каждый символ пробела
txt = 'The rain in Spain'
x = re.split('\s', txt)
print(x)
# Example 6
result = re.split(r'i', text, maxsplit=1)#только 1 участок (ПЕРВОЕ СОВПАДЕНИЕ)
print(result)
#Разделите строку только при первом вхождении:
x = re.split('\s', txt, 1)
print(x)
'''

# Example 7
'''
#Функция sub () заменяет совпадения выбранным вами текстом:
text = 'Who will live on Earth in the 21th century?'
result = re.sub(r'21', '31', text)
print(result)

#Замените каждый символ пробела цифрой 9:
txt = 'The rain in Spain'
x = re.sub('\s', '9', txt)
print(x)
'''

# Example 8
'''
text = 'Who will live on Earth in the 21th century?'
pattern = re.compile(r'21')
result1 = pattern.findall(text)
print(result1)

result2 = pattern.findall(text + 'COVID-21')
print(result2)
'''

# Example 9  Извлечение слов
'''
# Сначала попробуем вытащить каждый символ стороки (используя .)
text = 'Who will live on Earth in the 21th century?'
result = re.findall(r'.', text)# достать все символы, и записать их в список
print(result)

#Распечатайте список всех совпадений:
txt = 'The rain in Spain'
x = re.findall('.', txt)#list of li
print(x)

# Example 10  Извлечение слов
# Для того, чтобы в конечный результат не попал пробел, используем \w вместо .
result = re.findall(r'\w', text)
print(result)

# Example 11  Извлечение слов
# Теперь попробуем достать каждое слово (используя * или +)
result = re.findall(r'\w*', text)#w*\s
print(result)

# Example 12  Извлечение слов
# В результат попали пробелы, так как * означает «ноль или более символов».
# Для того, чтобы их убрать, используем +:
result = re.findall(r'\w+', text)#w*\s
print(result)
'''

# Example 13 Извлечение слов
'''
# Теперь вытащим первое слово, используя ^:
text = 'Who will live on Earth in the 21th century?'
result = re.findall(r'^\w+', text)# (r'^W\w+', text)
print(result)

text = 'ho will live on Earth in the 21th century?'
result = re.findall(r'^W\w+', text)#(r'^\w+', text) - ['ho]
print(result)
'''

# Example 14 Извлечение слов
'''
# Если мы используем $ вместо ^, то мы получим
# последнее слово, а не первое

text = 'Who will live on Earth in the 21th century? hell'
result = re.findall(r'\w+$', text)
print(result)

result = re.findall(r'\w$', text)
print(result)#['l']
'''

# Example 15 Вернуть первые два символа каждого слова
'''
# Вариант 1: используя \w, вытащить два
# последовательных символа, кроме пробельных, из
# каждого cлова

text = 'Who will live on Earth in the 21th century?'
result = re.findall(r'\w\w', text)
print(result)

# Example 16
# Вариант 2: вытащить два последовательных символа,
# используя символ границы слова (\b):
result = re.findall(r'\b\w{2}', text) #r' b w w' r' b w.'
print(result)
'''

# Example 17 Вернуть домены и почтовые адреса
'''
#Сначала вернём все символы после «@»:
#чтение из файла БД паролей

s = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com,\
 first.test@rest.biz 1@by'
result = re.findall(r'@\w+', s)
print(result)

# Example 18 Вернуть домены и почтовые адреса
# Как видим, части «.com», «.in» и т. д. не попали в
#результат. Изменим наш код

result = re.findall(r'@\w+.\w+|@\w+', s)
print(result)

# Example 19 Вернуть домены и почтовые адреса
#Второй вариант вытащить только домен верхнего уровня,\
# используя группировку ——():

result = re.findall(r'@((\w+).(\w+))', s)
print(result)
'''

# Example 20 Вытащим адрес целиком
'''
s = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com,\
 first.test@rest.biz'
result = re.findall(r'\b\w+@\w+.\w+', s)
print(result)

# Example 21 Вытащим адрес целиком
s = 'qwerty.abc.test@gmail.com, xyz@test.in,\
test.first@analyticsvidhya.com, first.test@rest.biz 1@ee.rrrr.tttt.qqq.www.by'

result = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:.[a-zA-Z0-9-]+)+', s)
print(result)
'''

# Example 22 Извлечь дату
'''
s = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
result = re.findall(r'\d{2}-\d{2}-\d{4}', s)
print(result)
# Example 23 Извлечь только год
result = re.findall(r'(\d{2}-\d{2})-(\d{4})', s)
print(result)
'''

# Example 24 Разбить строку по нескольким разделителям
'''
line = 'asdf fjdk;afed,fjek,asdf,foo'# String has multiple delimiters (";",","," ").
result = re.split(r'[;,\s]', line)
print(result)
# Example 25 Разбить строку по нескольким разделителям
#Также мы можем использовать метод re.sub()
#для замены всех разделителей пробелами:

sep = ' '
result = re.sub(r'[;,\s]', sep, line) #==(r'[;, s]', " ", line)
print(result)
'''

# Example 26 Проверить формат телефонного номера
# Номер должен быть длинной 10 знаков и начинаться с 8 или 9
# Есть список телефонных номеров и нужно проверить их используя re
'''
li = ['9999999999', '999999-999', '99999x9999']
for val in li:
    if re.match(r'[8-9]{1}[0-9]{9}', val) and len(val) == 10:
        print('Yes')
    else:
        print('No')
'''

# Example 27 Извлечь слова, начинающиеся на гласную/согласную
# Для начала вернем все слова:
'''
result = re.findall(r'\w+', 'AV is largest Analytics community of India')
print(result)

# А теперь только те, которые начинаются на гласные буквы (используя[]):
result = re.findall(r'[aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
print(result)

# Example 28 Извлечь слова, начинающиеся на гласную/согласную
# Выше мы видим обрезанные слова «argest» и «ommunity».
# Для того, чтобы убрать их, используем \b для обозначения границы слова:
result = re.findall(r'\b[aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
print(result)

# Example 29 Извлечь слова, начинающиеся на гласную/согласную
# на согласную
# Также мы можем использовать ^ внутри квадратных скобок для инвертирования группы:
result = re.findall(r'\b[^aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
print(result)

# Example 30 Извлечь слова, начинающиеся на гласную/согласную
# В результат попали слова, «начинающиеся» с пробела. Уберем их,
#включив пробел в диапазон в квадратных скобках:
result = re.findall(r'\b[^aeiouAEIOU\s]\w+', 'AV is largest Analytics community of India')
print(result)
'''

# Example 31 Извлечь информацию из html файла
'''
test_str = '1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily'
result = re.findall((r'\d([A-Z][a-z]+)([A-Z][a-z]+)'), test_str)
print(result)
'''

# Example 32 Замены
'''
# Задача: заменить все числа на слово ____

pattern = '[0-9]+'
sep = '____'
string = 'Мой дядя родился в 60 году и в 2021 ему было 61'
print(re.sub(pattern, sep, string))
'''

# Example 33 Использование групп при заменах
'''
def convert_dates(text):
    # gr 1 ([0-9]{2}) цифры от 0 до 9, две штуки
    # gr 2 ([0-9]{2}) цифры от 0 до 9, две штуки
    # gr 3 ([0-9]{4}) цифры от 0 до 9, четыре штуки
    pattern = '([0-9]{2})/([0-9]{2})/([0-9]{4})'
    repl = r'\3/\1/\2'# перестановки

    return re.sub(pattern, repl, text)

print(convert_dates('Гагарин полетел в космос 04/12/1961. Американцы высадились на Луну 07/20/1969'))
'''

# Example 34 Именованные группы
'''
def convert_dates(text):
    pattern = '(?P<m>[0-9]{2})/(?P<d>[0-9]{2})/(?P<y>[0-9]{4})(?P<hm>[0-9]{2}:[0-9]{2})'
    repl = r'\g<y>/\g<m>/\g<d> в \g<hm>'

    return re.sub(pattern, repl, text)
print(convert_dates('Гагарин полетел в космос 04/12/1961 09:07 по\
московскому времени. Американцы высадились на Луну 07/20/1969\
20:17 UTC'))

# Example 35 Именнованные группы
def get_main_provider(email):
    pattern = '(?P<login>[a-zA-Z0-9_]+)@(?P<provider>(?P<name>[a-zA-Z0-9_]+)\.(?P<domain>[a-zA-Z]+))'
    result = re.search(pattern, email)
    print(result.group('login'))
    if result:
        return result.group('provider')
    return None

print(get_main_provider('ivan@yandex.ru'))
'''