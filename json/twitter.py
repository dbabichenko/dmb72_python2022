import json

class User:
    user_id = 0
    first_name = ""
    last_name = ""


u1 = User()
u1.user_id = 10
u1.first_name = "Dmitriy"
u1.last_name = "Babichenko"

print(json.dumps(u1.__dict__))