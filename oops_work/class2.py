from class1 import bloodbank


class details(bloodbank):
    def password_check(self):
        if self.password2 == self.password:
            print("Registered")
        else:
            print("Enter correct password")
