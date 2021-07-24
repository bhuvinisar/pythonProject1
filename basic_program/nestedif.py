a=input("Enter the username:")
if a=='bhuvi123':
    print("access granted")
    a=int(input("Enter the password:"))
    if a==12345:
        print(" proceed")
    else:
        print("Pincord error")
else:
    print("access denied")