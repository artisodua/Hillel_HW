# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)

from ip_address import *

mylink = 'iplist.txt'

with open(mylink, 'r', encoding='utf-8') as file_input:
    line = file_input.read().split()

ip = IPAddress(line)

ip.get_address()
ip.reverse_address()
ip.address_not_first()
ip.last_oktet()