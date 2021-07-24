u1 = []
p1 = []
l = int(input("No. of login needed:"))
for i in range(l):
    u = input("Enter the username:")
    p = input("Enter the password:")
    u1.append(u)
    p1.append(p)
d = {'username': u1, 'password': p1}
print(d)
k = d['username']
q = d['password']
d1 = input("Enter a name")
if d1 in k:
    print(d1.index(q))
