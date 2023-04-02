import sys
numbers = sys.argv[1:]
numbers = list(map(int, numbers))

x = 0
y = []
for dig in numbers:
    x += dig
    y.append(x)
print(' '.join(list(map(str, y))))
