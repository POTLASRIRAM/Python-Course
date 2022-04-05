class Digits:
    @staticmethod
    def int_or_not(num):
        if isinstance(num,int):
            print(" Integer ")
        else:
            print("Not an Integer")
a=int(input("Enter a number = "))
Digits.int_or_not(a)