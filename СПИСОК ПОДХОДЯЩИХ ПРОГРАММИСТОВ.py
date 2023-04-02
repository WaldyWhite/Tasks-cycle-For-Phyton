import sys
language = sys.argv[1]
users = [
    {"id": 17,  "lang": "python", "active": False},
    {"id": 156, "lang": "php",    "active": True},
    {"id": 23,  "lang": "java",   "active": True},
    {"id": 84,  "lang": "python", "active": True},
    {"id": 28,  "lang": "java",   "active": False},
    {"id": 21,  "lang": "java",   "active": True},
    {"id": 55,  "lang": "python", "active": True},
    {"id": 88,  "lang": "python", "active": True},
    {"id": 287, "lang": "c++",    "active": False},
    {"id": 481, "lang": "php",    "active": False},
    {"id": 134, "lang": "c++",    "active": True},
    {"id": 65, "lang": "php",    "active": True},
]
user_id = []

for ident in users:
    if ident['lang'] == language and ident['active'] == True:
        user_id.append(int(ident['id']))
        user_id.sort()

print(', '.join(list(map(str, user_id))))
