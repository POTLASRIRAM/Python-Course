class Books:
    Book_price=100
    def __init__(self,Quantity : int):
        assert Quantity>=0, "Quantity should be greater than zero"
        self.quantity=Quantity
    def total_books_price(self):
        total_price=self.quantity*self.Book_price
        print("Price = ",total_price)
    
b1=Books(7)
b1.Book_price=10
b2=Books(4)
b3=Books(10)
b1.total_books_price()
b2.total_books_price()
b3.total_books_price()