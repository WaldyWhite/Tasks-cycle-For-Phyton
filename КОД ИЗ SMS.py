import sys
sms = sys.argv[1]
number = []
for dig in sms:
    if dig.isdigit():
        number.append(dig)

print(''.join(number))
