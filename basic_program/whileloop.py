#c=int(input("enter the count:"))

while True:
    username = input("Enter the username: ")

    if username == 'nisar':
        password = int(input("Enter the password: "))
        if password == 1234:
            print("Login success")
            break
        else:
            print("Invalid")
            continue