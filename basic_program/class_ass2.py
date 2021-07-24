from class_ass2 import update

class login(update):
    def login1(self):
        x = input("Need to login:")
        if x == "yes":
            u1 = input("Enter the user name:")
            p1 = input("Enter the password:")
            if u1 in self.username:
                i = self.username.index(u1)
                if self.password[i] == p1:
                    print("Login successful")
                else:
                    print("Incorrect password or username")
r=update()
r.login1()

