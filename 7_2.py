# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу

from to_do_json import *

object1 = ToDoJson('jfirst.json')
object2 = ToDoJson('jsecond.json')

first_file = object1.read_json_file()
second_file = object2.read_json_file()

twofiles = [first_file, second_file]

object1.write_json_file(twofiles)

folder_puth = object1.puth_folder()
print('path to the current folder: {}'.format(folder_puth[0]))

file_puth = object1.puth_file()