import sys
symbols = sys.argv[1]
smal = []
large = []
for letter in symbols:
    if letter.islower():
        smal.append(letter)
    else:
        large.append(letter)
print(''.join(smal)+''.join(large))
