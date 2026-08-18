class computer:
    def __init__(self):
       self.__privno = 900

    def sell(self):
        print(self.__privno)

    def setmaxprice(self,price):
        self.__privno = price

c = computer()
c.sell()

c.__privno = 1000
c.sell()

c.setmaxprice(1000)
c.sell()