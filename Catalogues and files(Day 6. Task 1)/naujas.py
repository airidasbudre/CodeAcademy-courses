import os
import this
from datetime import datetime

# ----------------------------------------------------------------------------------------
# Sukurti programą, kuri:

# + Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
# + Atspausdintų tekstą iš sukurto failo
# + Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
# +- Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
# +- Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
# Atspausdintų visą failo tekstą atbulai
# Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS
# ----------------------------------------------------------------------------------------


# os.mkdir("Naujas kat")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# # Task 1 + 3
# with open("Failas.txt", "w") as failas:
#     failas.write(f"{tekstas} \n {dt_string}")

# # Task 2
# with open("Failas.txt", 'r', encoding="utf-8") as failas:
#     print(failas.readlines())

# # Task 4
# s = 1
# with open("Failas.txt", 'r', encoding="utf-8") as failas:
#     for eilute in failas:
#         print(str(s) + " " + eilute)
#         s+=1

# # Task 5
# with open("Failas.txt", 'w', encoding="utf-8") as failas:
#     failas.write("Beautiful is better than ugly.")
#     failas.seek(0)
#     failas.write("Gražu yra geriau nei bjauru.")

# Task 6
with open("Failas.txt", 'r', encoding="UTF-8") as failas:
    print(failas.readlines()[4])


