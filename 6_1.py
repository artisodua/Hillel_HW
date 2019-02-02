# Задача-1
# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.

try:
    with open('file.txt', 'r+', encoding='utf-8') as infile:
        data = infile.readlines()
except (FileNotFoundError):
    print('Error - File not found!!!!! Please enter validate link')

def line(item):
    with open('new.txt', 'a', encoding='utf-8') as f:
        for i in item:
            f.write('\n')
            for j in i.split():
                if len(j) == 3 or len(j) == 4 or len(j) == 5:
                    pass
                else:
                    f.write(j+' ')
    return f

line(data)