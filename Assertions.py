from re import A


class Assertions:
    def __init__(self,greet : str,no1 : int,no2 : int):
        assert no1>=0 ,"Number one should be greater than zero"
        assert no2>=0 ,"Number two should be greater than zero"
        self.greet=greet
        self.no1=no1
        self.no2=no2
        print(self.greet,self.no1,self.no2)

a=Assertions("Hi",1,2)
