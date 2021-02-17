def save_into_db(info):
    print("saved into databse")


user_name = input('Please enter your username: ')
save_into_db(user_name)
birth_year = int(input('Please enter your birth year: '))
age = 2020 - birth_year
print("You are",age, "years old.")
