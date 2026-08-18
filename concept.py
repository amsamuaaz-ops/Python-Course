class myname:
    __privnumber = 27
    def __priv_meth(self):
        print("THIS IS MY PRIV NUMBER")

    def hello(self):
        print("THIS IS MY PRIV NO",myname.__privnumber)

foo = myname()

foo.hello()

foo.__priv_meth()