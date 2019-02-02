# Задача-2
# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.

import re

myfile = 'phone_number.txt'

with open(myfile, 'r', encoding='utf-8') as file_read:
    for i in file_read.readlines():
        lookfor = r'[C,K]'
        result = re.findall(lookfor, i)
        if result:
            with open('new_phone_number.txt', 'a', encoding='utf-8') as file_write:
                file_write.writelines(i)