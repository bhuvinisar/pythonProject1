username=[]
password=[]
l=int(input("No. of login needed:"))
for i in range(l):
    u=input("Enter the username:")
    p=input("Enter the password:")
    username.append(u)
    password.append(p)
print(username)
print(password)
x=input("Need to login:")
if x=="yes":
    u1=input("Enter the user name:")
    p1=input("Enter the password:")
    f=open("write.txt","a")
    f.write("\n how r u")
    f.close()
    if u1 in username:
        i = username.index(u1)
        if password[i] == p1:
            print("Login successful")
        else:
            print("Incorrect password or username")


