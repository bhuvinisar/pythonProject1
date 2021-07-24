
while True:
    initial = int(input("Enter your initial:"))
    age = int(input("Enter your age:"))
    gender = input("Enter your gender(male /female): ")
    if age <25 and gender == 'male':
        print("The Insurance amount for the candidate: ",initial+500)
    elif age <25 and gender == 'female':
        print("The Insurance amount for the candidate: ",initial+1000)
    elif (age >= 25)and(age <45) and gender == 'male':
        print("The Insurance amount for the candidate: ",initial+500+(initial*10/100))
    elif (age >= 25)and(age <45) and gender == 'female':
        print("The Insurance amount for the candidate: ",initial+1000+(initial*10/100))
    elif (age >= 45)and(age < 75) and gender == 'male':
        print("The Insurance amount for the candidate: ",initial+500+(initial*20/100))
    elif (age >= 45)and(age < 75) and gender == 'female':
        print("The Insurance amount for the candidate: ",initial+1000+(initial*10/100))
    e = input("Need to run the code again (yes /no): ")
    if e=="yes":
        continue
    else:
        break