

data = {
    "admin": ("admin", "123456", "admin", 9),
    "Joseph": ("Joseph", "234", "student", 13),
    "Sam": ("Sam", "567", "student", 13)
}

def check(user, password):
    return user in data and password == data[user][1]

def rolecheck():
    return data

def withdraw(user, ent):
    if data[user][3] >= ent:
        data[user] = (data[user][0], data[user][1], data[user][2], data[user][3] - ent)
        return True
    else:
        return False

def add(user, wnch):
    data[user] = (data[user][0], data[user][1], data[user][2], data[user][3] + int(wnch))

def getbalance(user):
    return data[user][3]

def addnew(a: str, b: str, c: str, d: str):
    if d == "student" or d == "admin":
        data.setdefault(a, (b, c, d, 9))
    else:
        print("Invalid role")
