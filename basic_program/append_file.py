r=int(input("No. of recprds:"))
for x in range(r):
    z = input("Enter your name:")

    f=open("my1.doc","a")
    f.write(z)
y=open("my.doc","r")
y=y.read()
print(y)

