import sys
numbers = sys.argv[1:]
numbers = list(map(int, numbers))
income = []
expense = []
for dig in numbers:
    if dig > 0:
        income.append(dig)
    else:
        expense.append(dig * -1)
print(f'Доходы: {sum(income)} руб.\nРасходы: {sum(expense)} руб.')



