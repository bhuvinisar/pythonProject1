a=10
print(a)
c='nisar'
b=20

try:
    while True:
        username = int(input("Enter the username: "))

        if username == 'nisar':
            password = int(input("Enter the password: "))
            if password == 1234:
                print("Login success")
                break
            else:
                print("Invalid")
                continue
except ValueError as e:
    print(e)

finally:
    print('FINAL')
    print(b)
print('Loose')