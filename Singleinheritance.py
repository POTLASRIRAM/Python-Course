class Main:
    def __init__(self):
        self.name="Sriram"
class Sub(Main):
    def __init__(self):
        Main.__init__(self)
        print(self.name)
s=Sub()
