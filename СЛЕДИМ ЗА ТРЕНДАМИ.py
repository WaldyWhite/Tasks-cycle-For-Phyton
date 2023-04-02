import sys
data = sys.argv[1:]
datas = list(map(int, data))

data_update = datas[0]
for i in range(len(datas)):

    if data_update > datas[i-1]:
        data_update = datas[i]
        print('green', end=' ')
    if data_update > datas[i-2] and data_update == datas[i-1]:
        data_update = datas[i]
        print('green', end=' ')
    if data_update < datas[i-1]:
        data_update = datas[i]
        print('red', end=' ')
print(data_update)
