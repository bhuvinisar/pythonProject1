from multidispatch import dispatch
class overload:

    @dispatch(str, int)
    def print_mark(self, ta):
        print(456)
        print(ta)

    @dispatch(int)
    def print_mark(self, en):
        print(876)
        print(en)


o=overload()
o.print_mark('nisar', 34)