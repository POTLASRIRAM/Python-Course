class Computer:
    def __init__(self,CPU,RAM):
        self.CPU=CPU
        self.RAM=RAM
    def system_details(self):
        print("System Information")
        print(self.CPU,self.RAM)
        
comp1=Computer("Intel",8)
comp2=Computer("AMD",8)
comp1.system_details()
comp2.system_details()
