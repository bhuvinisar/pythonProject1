a=[]
b=[]
item=int(input("No. of items needed:"))
for i in range(item):
    x=input("Enter the items needed:")
    a.append(x)
    y=int(input("Enter the price:"))
    b.append(y)
    shop={'items':a,'price':b}
print(shop)
l=shop['items']
m=shop['price']
while True:
    s=input("Want to shop:")
    if s=='yes':
        i=input("Enter a item to shop:")
        if i in l:
            q = int(input("Enter the quantity/amt needed:"))
            q = q * m
            print(q)
        else:
            print("Enter a item in list")
    else:
        break
