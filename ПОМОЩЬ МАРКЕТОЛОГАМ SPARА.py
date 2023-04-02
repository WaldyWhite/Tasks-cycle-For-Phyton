import sys
file = open('dict.txt', 'r', encoding='utf-8')
spar = 'SPAR'
sPaR = 'спар'
fileReaded = []
b = 0
for i in file.readlines():
    fileReaded.append(i.replace('\n', '').split(','))
file.close()
for j in fileReaded:
    for k in j:
        if sPaR in k or sPaR.title() in k:
            k = k.replace('спар', 'SPAR')
            k = k.replace('Спар', 'SPAR')
            print(k)

