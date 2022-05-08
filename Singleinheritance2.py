class Main:
    def __init__(self):
        self.name="Sriram"
    def namee(self):
        print("Hi",self.name)
class Sub(Main):
    def __init__(self):
        Main.__init__(self)
        print(self.name)
        super().namee()
s=Sub()

