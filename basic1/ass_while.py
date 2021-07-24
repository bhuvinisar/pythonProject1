username = input("Enter a name:")
password = int(input("Enter a password:"))
password2 = int(input("Enter confirm password:"))
if password2 == password:
    print("Registered")
else:
    print("Enter correct password")
while True:
    x = input("To check blood requirement yes/no:")
    if x == "yes":
        name = input("Enter your name:")
        age = int(input("Enter your age:"))
        gender = input("Enter your gender:")
        bg = input("Enter your blood group:")
        c = input("Enter your mobile no:")
        l = {'a+': '50', 'b+': '80', 'b-': '40', 'ab+': '60', 'ab-': '20', 'o+': '60'}
        bg2 = input("Enter required blood group:")
        if bg2 in l:
            print("Blood in stock")
        else:
            print("No stock")
            break
    else:
        break
