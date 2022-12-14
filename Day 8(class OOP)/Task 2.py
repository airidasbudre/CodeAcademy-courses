import datetime
import numpy as np
import datetime as dt

class Worker():
    def __init__(self, name, hour_price, work_from):
        self.name = name
        self.hour_price = hour_price
        self.work_from = work_from
        self.date = datetime.datetime.strptime(work_from, "%Y-%m-%d")
    #Jeigu padarau privatų meta klaida
    def working_days(self):
        work_days = (datetime.datetime.today() - self.date).days
        return work_days

    def salary(self):
        salary = 8 * self.hour_price * self.working_days()
        print(salary)

class Normal_Worker(Worker):
    def working_days(self):
        #klaida
        start = dt.datestr(self.date)

        end = dt.date(datetime.datetime.today())
        work_days = np.busday_count( start, end )
        # work_days = (datetime.datetime.today() - self.date).days
        print(work_days)


#Jeigu padarau privatų meta klaida
worker = Worker("Jonas", 10, "2022-09-30")
worker.working_days()
worker.salary()
worker2 = Normal_Worker("Jonas", 10, "2022-09-30")
worker2.working_days()
worker2.salary()
