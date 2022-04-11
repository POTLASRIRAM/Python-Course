class Count:
    def __init__(self):
        self.n1=30
        self.n2=40
class CC(Count):
    def __init__(self):
        print(super().__init__(Count))
c1=CC()        
