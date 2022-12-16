import datetime
import calendar
from datetime import timedelta
# + Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) ir metodus, kurie:

# + Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
# + Gražina, ar nurodytos sukakties metai buvo keliamieji
# + Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
# + Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą

class Anniversary():
    def __init__(self, year, month, day, hour, minute, second):
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

