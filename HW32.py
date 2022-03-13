name=input("Enter name")
date=input("Enter date")
letter='''Dear Name!
           Your selected dated on Date.'''
letter=letter.replace("Name",name)
letter=letter.replace("Date",date)
print(letter)