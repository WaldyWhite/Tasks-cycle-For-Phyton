import sys
amount = int(sys.argv[1])

products = [
    {"name": "Гречка", "price": 69},
    {"name": "Хлеб", "price": 34},
    {"name": "Молоко", "price": 57},
    {"name": "Яйца", "price": 78},
    {"name": "Рис", "price": 88},
    {"name": "Макароны", "price": 49},
    {"name": "Сахар", "price": 22},
    {"name": "Яблоки", "price": 79},
    {"name": "Картофель", "price": 18},
    {"name": "Свинина", "price": 120},
    {"name": "Масло", "price": 66},
    {"name": "Помидоры", "price": 64}
]
prod_list = []
for data in products:
    if amount < data['price']:
        continue
    if amount >= data['price']:
        prod_list.append(data['name'])
        amount -= data['price']
print(', '.join(prod_list))




