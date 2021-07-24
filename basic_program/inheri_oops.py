from class_object import bhuvi

class display(bhuvi):
    def exm2(self):
        maths=100
        science=99
        social=98
        total=maths+science+social+500
        print(total)




class marks(display):
    def exm1(self):
        maths=100
        science=99
        social=98
        total=maths+science+social
        print(total)



class students(marks):
    def record(self):
        a=int(input("Enter rollno:"))
        print(a)
s=students()
s.record()
s.exm1()
s.exm2()
s.nisarmental()