import sys
numbers = sys.argv[1:]
numbers = list(map(int, numbers))
best = max(numbers)

x = []
for dig in numbers:
    dig -= best
    x.append(dig)
print(' '.join(list(map(str, x))))

