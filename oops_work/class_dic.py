class login():
    def register(self):
        self.u1 = []
        self.p1 = []
        l = int(input("No. of login needed:"))
        for i in range(l):
            u = input("Enter the username:")
            p = input("Enter the password:")
            self.u1.append(u)
            self.p1.append(p)
        self.d = {'username': self.u1, 'password': self.p1}
        print(self.d)


class user(login):
    def register(self):
        super().register()
        k = self.d['username']
        d1 = input("Enter a name")
        if d1 in k:
            #print(self.u1 ,self.d('password'))
2


x = user()
x.register()
