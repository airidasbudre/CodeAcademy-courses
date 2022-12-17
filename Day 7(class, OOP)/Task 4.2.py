import datetime
import calendar
from datetime import timedelta

# Perdaryti 2 užduotį taip, kad spausdinant datos objektą, spausdintų ne objekto adresą, o įvestą datą

class Anniversary():
    def __init__(self, year=input("Year: "), month=input("month: "), day=input("day: "), hour=input("hour: "), minute=input("minute: "), second=input("second: ")):
        self.year = year 
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        
        self.date = datetime.datetime(year, month, day, hour, minute, second)
    

    def time_passed(self):
        time_passed = datetime.datetime.today() - self.date
        print(time_passed)
        print(f"Years: {time_passed.days//365}, months: {time_passed.days//12}, days: {time_passed.days}, hours: {time_passed.days*24} ")

    def is_leap_year(self):
        if calendar.isleap(self.year):
            print("Its leap year!")

    def subtract(self):
        print(datetime.datetime.today() - timedelta(days=5))
    
    def plus(self):
        print(datetime.datetime.today() + timedelta(days=5))

bandom = Anniversary(2020, 2, 5, 1, 1, 1)
bandom.time_passed()
bandom.subtract()
bandom.plus()

