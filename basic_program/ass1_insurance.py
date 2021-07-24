initial=50000
age=int(input("Enter your age:"))
male=500
female=1000
while True:
    gender = input("Enter gender:")
    if age<25:
        if gender=="male":
            initial=initial+male
            print(initial)
            break
        else:
            initial=initial+female
            print(initial)
    break
while True:
    if (age < 45)and(age > 25):
        if gender == "male":
            initial = initial + male + 5000
            print(initial)
            break
        else:
            initial = initial + female + 5000
            print(initial)
    break
while True:
    if (age < 90)and(age > 45):
        if gender == "male":
            initial = initial + male + 10000
            print(initial)
            break
        else:
            initial = initial + female + 10000
            print(initial)
    break






