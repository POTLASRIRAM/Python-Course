import csv
class Data:
    @classmethod
    def books_data(cls):
        f= open('Day17-5-04-2022\data.csv','r')
        reader = csv.DictReader(f)
        items=list(reader)
        for item in items:
            print(item)
Data.books_data()