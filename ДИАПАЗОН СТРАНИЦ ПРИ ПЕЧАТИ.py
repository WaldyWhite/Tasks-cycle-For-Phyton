import sys
stroka = sys.argv[1]
s = stroka.split(',')
l = []
for i in s:
    if i.isdigit():
        l.append(int(i))
    for n, j in enumerate(i):
        if j == '-':
            for y in range(int(i[:n]),int(i[n+1:])+1):
                l.append(int(y))

x = list(set(l))
print(','.join(map(str, x)))





