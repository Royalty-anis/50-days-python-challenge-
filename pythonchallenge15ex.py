def add_age(x):
    try:
        name_input = input("input name: ")
        return (f"hi, {name_input} you are {x[name_input]}")
    except KeyError:
        print("your name dose not exist in the database")
        age = input("input age: ")
        names_age[name_input] = age
        return (f"hi, {name_input} you are {x[name_input]} years old")
print(add_age(names_age))
