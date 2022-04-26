class Main:
    def __init__(self,name):
        self.name=name
    def name(self):
        print("Hi",self.name)
class Main1:
    def __init__(self,name):
        self.name=name
        print("How are u",self.name,"?")
class Sub(Main,Main1):
    def __init__(self,name):
        Main.__init__(self,name)
        super().name()
        
s=Sub("Sriram")
m=Main1("Potla")
