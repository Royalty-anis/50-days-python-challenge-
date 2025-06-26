from random import randint as r
def user_name():
    name = input("name: ")
    rname = name[::-1]

    return f"your username is: {rname}{r(0,9)}"
print(user_name())
