num=int(input("Enter a number:"))
fact=1
if num<0:
    print("Factorial does not exist:")
elif num==0:
    print("Factorial of 0 is always 1")
else:
    for i in range(1,num+1):
        fact=fact*i
        print("Factorial",num,"is",fact)