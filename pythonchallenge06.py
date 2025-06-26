def user_name():
    email = input("input your email: ")
    username = email.split("@")
    return f"your username is {username[0]}"
