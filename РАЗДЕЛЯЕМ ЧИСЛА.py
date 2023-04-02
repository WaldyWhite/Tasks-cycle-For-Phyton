import sys
digits = sys.argv[1:]
digits = list(map(int, digits))
negative = []
positive = []
for dig in digits:
    if dig < 0:
        negative.append(dig)
    else:
        positive.append(dig)

print(' '.join(list(map(str, negative))), ' '.join(list(map(str, positive))))
