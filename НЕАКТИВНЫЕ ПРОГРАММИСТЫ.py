import sys
language = sys.argv[1]
users = [
    {"id": 17,  "active": False, "langs": ["python", "javascript"]},
    {"id": 156, "active": True,  "langs": ["php"]},
    {"id": 23,  "active": True,  "langs": ["java", "c++"]},
    {"id": 84,  "active": True,  "langs": ["python", "c++"]},
    {"id": 28,  "active": False, "langs": ["java", "php"]},
    {"id": 21,  "active": True,  "langs": ["java", "javascript"]},
    {"id": 55,  "active": True,  "langs": ["python", "c#"]},
    {"id": 88,  "active": True,  "langs": []},
    {"id": 287, "active": False, "langs": ["c++", "c#", "java"]},
    {"id": 481, "active": False, "langs": ["php", "javascript", "python"]},
    {"id": 134, "active": True,  "langs": ["c++", "python"]},
    {"id": 65,  "active": True,  "langs": ["php", "python"]},
    {"id": 7,  "active": False,  "langs": ["javascript", "c#"]}
]
user_id = []

for ident in users:
    for lang in ident['langs']:
        if lang == language and ident['active'] == False:
            user_id.append(str(ident['id']))


print(', '.join(user_id))
