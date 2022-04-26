class Main:
    def __init__(self):
        self.name="Sriram"
    def name(self):
        print("Hi",self.name)
class Main1(Main):
    def __init__(self):
        Main.__init__(self)
        
        
m=Main1()    
class Sub(Main1):
    def __init__(self):
        Main1.__init__(self)
        print(self.name)
        
s=Sub()