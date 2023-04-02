import sys
digits = sys.argv[1:]
digits_digit = list(map(int, digits))
var_digit = None
list_digits = []
for number in digits_digit:
    if var_digit is None or number > var_digit:
        var_digit = number
        list_digits += [number]
print(', '.join(list(map(str,list_digits))))
