"""
Попробуем реализовать чтение RAID 0 на Python. Рядом с программой находится N текстовых файлов в кодировке utf-8.
Каждый файл имеет имя data-1.txt, data-2.txt, ..., data-N.txt. При записи данных, первый символ текста был помещен в
файл data-1.txt, второй в data-2.txt и тд. В случае если длина текста больше N, то алгоритм записывает данные по кругу.
Например, для трёх файлов и текста «Программирование» данные распределяются так:

Файл data-1.txt: «Пгмрае». Файл data-2.txt: «ррмон» . data-3.txt: «оаиви» .

Напишите программу, которая из первого аргумента командной строки принимает количество файлов, которые были
использованы для записи, а из второго количество символов, которе нужно из них прочитать. Результатом программа
должна вернуть восстановленный текст.
"""


import sys
number_files = int(sys.argv[1]) + 1
number_symbol = int(sys.argv[2])
text = ''
fileNum = ''
for i in range(number_symbol):
    for j in range(1, number_files):
        fileNum = str(j)
        dat = 'data-{:s}.txt'.format(fileNum)
        file = open(dat, 'r', encoding='utf-8')
        if len(text) < number_symbol:
            for read in file.readlines():
                text += read[i].replace('\n', '')
                file.close()
print(text)
