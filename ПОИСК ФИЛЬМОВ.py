import sys
file = open('films.txt', 'r', encoding='utf-8')
filmsName = sys.argv[1]
fileReaded = []
for i in file.readlines():
    fileReaded.append(i.replace('\n', '').split(','))
file.close()
for j in fileReaded:
    for k in j:
        if filmsName.lower() in k.lower():

            print(j[1])


