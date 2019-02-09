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

class IPAddress():
    def __init__(self, line):
        self._line = line
        # self._ar = []

    def get_address(self):
        ar = []
        for i in self._line:
            ar.append(i)
        return ar

    def reverse_address(self):
        ar = []
        for i in self._line:
            j = i.split('.')
            j.reverse()
            ar.append('.'.join(j))
        return ar

    def address_not_first(self):
        ar = []
        for i in self._line:
            j = i.split('.')
            ar.append('.'.join(j[1::]))
        return ar

    def last_oktet(self):
        ar = []
        for i in self._line:
            j = i.split('.')
            ar.append('Last otket -> {}'.format(j[-1]))
        return ar