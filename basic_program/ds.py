n = []
r=int(input("No. of records:"))
for i in range(r):
    a = input("enter a name:")
    n.append(a)
print(n)


name=input("Enter a name:")
if name in n:
    print("element found")
else:
    print("element not found")



