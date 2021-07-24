a={'items': ['biscuit', 'chocolate'], 'price': [100, 200]}

b= a['items']
c= input("Enter your product:")
x=b.index(c)
d= a['price']
e=d[x]
c= int(input("Enter your count:"))
print(a.keys())
print(a.values())
print(e*c)