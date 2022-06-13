class Main:
    def __init__(self):
        self.__a=10
        print(self.__a)
    
class Child(Main):
    def __init__(self):
        '''Main.__init__(self)
        print(self.__a)
        self.__a=20
        print(self.__a)
        print(self.__a)'''
        pass
c=Main()
ch=Child()
