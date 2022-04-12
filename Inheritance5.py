class Values:
    def __init__(self):
        self.x1=50
        self.x2=50
class Sum(Values):
    def sum(self):
        super().__init__()
        sum=self.x1+self.x2
        print(sum)
s=Sum()
s.sum()
