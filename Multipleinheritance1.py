class Grandpa:
    def __init__(self,grandpa):
        self.grandpa=grandpa
        print("Grandfather = ",self.grandpa)
class father(Grandpa):
    def __init__(self,father,grandpa):
        self.father=father
        print("Father = ",self.father)
        Grandpa.__init__(self,grandpa)
class Son(father):
    def __init__(self,Son,father,grandpa):
        self.son=Son
        print("Son = ",self.son)
        father.__init__(self,father,grandpa)
    
s=Son("S","P","R")
