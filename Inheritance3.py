class Flower:
    def __init__(self):
        print("Flower class")
    def main_class(self):
        self.c1=1
class Rose(Flower):
    def __init__(self):
        super().__init__()
        print(' Rose class ')
r=Rose()
class Jasmine(Flower):
    def __init__(self):
        super().__init__()
        print(' Jasmine class ')
j=Jasmine()