class Main:
    def __init__(self):
        self._a=10
class Child(Main):
    def __init__(self):
        Main.__init__(self)
        print(self._a)
        self._a=20
        print(self._a)
        print(self._a)
ch=Child()