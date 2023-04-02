'''
Напишите программу, которая из первого аргумента командной строки получает фразу, а затем меняет в ней
местами рядом стоящие буквы.

Если фраза имеет нечетное число символов, то последний символ остается на своём месте.
ABCDEF --- BADCFE
'''
import sys
alpha = sys.argv[1:]
alpha_str = []
sd = []
for i in alpha:
    alpha_str += i

for al in range(1,len(alpha_str),2):
    sd.append(alpha_str[al])
for al in range(0,len(alpha_str),2):
    sd.insert(al+1, alpha_str[al])

print(''.join(sd))




