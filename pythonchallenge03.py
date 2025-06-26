def register_check(x):
    in_students = 0
    total_students = 0
    for names in x:
        if x[names].lower() == 'no':
          total_students += 1
        else:
            in_students += 1
            total_students += 1
    return f"There are {total_students} students but only {in_students} are in school!"
