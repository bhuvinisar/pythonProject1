d = {'name': ['bhuvi', 'nisar', 'moni'], 'age': [20, 60, 25]}
j = d['name']
k = d['age']
x = input("Enter a name:")
if x in j:
    i = j.values(x)
    print("The age is:"+str(i))
