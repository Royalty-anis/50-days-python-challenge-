def age_in_minutes():
        age = input("input year of birth: ")
        if len(age) > 4:
            return ValueError
        elif int(age) < 1900 or int(age) > 2024:
            return ValueError
        else:
            ageInMinitues = 525600 * (2022 - int(age))
            return ageInMinitues
while True:
    try:
        age_in_minutes()
        break
    except ValueError:
        print("input a valid year")
