class nisar:

    def good(self, b):
        print("Nisar is good boy")



class bhuvi(nisar):

    def good(self, a):
        super().good()
        print("bhuvi is bad girl")


b=bhuvi()
b.good(10)
