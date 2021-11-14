# This script allows to make backups of your files in your folder
import os
import time

# Файлы и каталоги, кторые необходимо скопировать, собираются в список
source = ['"D:\\Documents\\Txt documents"',
          '"D:\Programming\Python\IBA\Tic Tac"']

# Резервные копии должны храниться в основном каталоге резерва
target_dir = 'D:\\Documents\\Copies'

# Файлы помещаются в zip-архив. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Enter some comment: ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Создаем каталог, если его еще нет
if not os.path.exists(today):
    os.mkdir(today)
    print('Directory created successfully!')

# Используем комманду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
print(zip_command)# Если это вбить с cmd то работает
if os.system(zip_command) == 0:
    print("The backup was successfully created in", target)
else:
    print('Backup failed')



