import sys
numbers = sys.argv[1:]
up_numbers = numbers[0]
for item in numbers:
    if item != "null":
        up_numbers = item
    print(up_numbers, end =" ")
