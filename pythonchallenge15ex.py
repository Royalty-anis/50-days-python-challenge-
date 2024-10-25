
    
names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}



def add_age(x,y):
    age = input("input age: ").lower()
    x[y] = age
    print(f"Hi, {y},you are {age} years old")
    

def your_age(names):
    student_name = input("your name: ").lower()
    for name in names:
        if name == student_name:
            return f"Hi, {student_name} you are {names[student_name]} years old"
    else:
       name != student_name
       print("your name is not in the data base")
       add_age(names_age,student_name)

       
print(your_age(names_age))
    
       
