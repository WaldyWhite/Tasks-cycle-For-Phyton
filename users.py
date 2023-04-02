import sys
email = sys.argv[1]
email = email.lower()
password = sys.argv[2]

users = [
    {"email": "user1@domain.com", "password": "password1"},
    {"email": "user2@domain.com", "password": "abcde"},
    {"email": "user3@domain.com", "password": "123456"},
    {"email": "user4@domain.com", "password": "lovelove"},
    {"email": "user5@domain.com", "password": "kdmUdmk84M"},
    {"email": "user7@domain.com", "password": "123456"},
    {"email": "user8@domain.com", "password": "123456"},
    {"email": "user9@mail.com.ru", "password": "password9"}
]
x = ''
y = ''
for user_email in users:
    if user_email['email'] == email:
        x = user_email['email']
        for user_password in users:
            if user_password['password'] == password:
                y = user_password['password']
if x == email and y == password:
    print("Доступ открыт")
elif x == email and y != password:
    print("Доступ закрыт")
else:
    print("Пользователь не найден")

