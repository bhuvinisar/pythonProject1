from class_ass1 import mail

class update(mail):
    def __init__(self):
        l = int(input("No. of login needed:"))
        for i in range(l):
            u = input("Enter the username:")
            p = input("Enter the password:")
            self.username.append(u)
            self.password.append(p)
        print(self.username)
        print(self.password)

