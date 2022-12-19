from datetime import date 
from datetime import datetime

# Python faile padaryti šiuos veiksmus (atskirai, ne iškart):

# Importuoti modulį datetime. Atsispausdinti šiandienos datą ir laiką kartu, tik datą (date.today()) bei tik laiką (.now().time()).
# Iš paketo datetime importuoti modulį date. Atsispausdinti šiandienos datą.
# Iš paketo datetime importuoti modulį date kaip data (as data). Atsispausdinti šiandienos datą.

#Date
date1 = date.today()
print(date1.strftime("%d/%m/%Y"))

#Date and time
date_time = datetime.today()
print(date_time)

#Time
now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
print("Time =", dt_string)	


