class book:
    def __init__(self,author,title):
        self.author = author
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print("you borrowed a book from libarary",self.title)

    def return_book(self):
        self.is_borrowed = False
        print("you return the booked",self.title)

book1 = book("rd", "cherry_and_ch")
book2 = book("jk", "harry potter")
book3 = book("kishimato", "jujutsu_kaizen_manga")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow(
)
book3.return_book()

       

 