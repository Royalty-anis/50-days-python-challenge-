def student_tuple(x):
    male = 0
    female = 0
    for names in x:
        if names.lower() == "male":
            male += 1
        elif names.lower() == "female":
            female += 1
        else:
            return "invalid"
    return f"[('Male',{male}),('Female',{female})]"
