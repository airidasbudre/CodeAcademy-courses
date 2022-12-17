import os
from datetime import datetime

# Sukurti programą, kuri:

# + Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
# + Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
# + Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
# Patarimai:

# Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_ctime


os.chdir(r'C:\Autofiles\auto\Coding school\Catalogues and files -Day 6. Task 1\New catalog')
print(os.getcwd())



with open("New file.txt", 'w', encoding="utf-8") as failas:
    data = os.stat("New file.txt").st_mtime
    print(failas.write(str(datetime.now())))
    print(datetime.fromtimestamp(data))

