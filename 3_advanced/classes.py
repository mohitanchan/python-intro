

class Car:
    def __init__(self):
        """ This is the constructor """
        self.make = "Maruti"
        self.name = "Swift"
        self.seater = 5

    def describe(self):
        """This is an instance method"""
        print(f"Your car is {self.make} {self.name}")

swift = Car()
print(swift.name)

swift.describe()

# print all attributes of a class
print(swift.__dict__)

""" classmethod and static method---------------------------------------------------"""

class MyDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, datestr):
        """cls is an object that holds the class itself, not an instance of the class"""
        year = int(datestr[0:4])
        month = int(datestr[4:6])
        day = int(datestr[6:])
        mydate1 = cls(day, month, year)
        return mydate1

    @staticmethod
    def is_valid(datestr):
        year = int(datestr[0:4])
        month = int(datestr[4:6])
        day = int(datestr[6:])
        return day <= 31 and month <= 12 and year <= 3999

    def __str__(self):
        return f"{self.day}-{self.month}-{self.year}"

datestr = "20190123"
if (MyDate.is_valid(datestr)) :
    date = MyDate.from_string(datestr)
    print(date)
else:
    print("Invalid Date")
