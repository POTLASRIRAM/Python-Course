import csv
class Data:
    @classmethod
    def books_data(cls):
        with open('Day17-5-04-2022\data.csv','r') as f:
            reader = csv.DictReader(f)
            items=list(reader)
        for item in items:
            print(item)
Data.books_data()