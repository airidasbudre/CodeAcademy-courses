# Duotas sąrašas: sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# Sukurti programą, kuri:

# + Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
# Sudėtų ir atspausdintų visus sąrašo žodžius
# Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme
# Patarimai:

# Naudoti filter arba comprehension, sum, " ".join()

list_1 = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

print(sum(type(c) is int for c in list_1))
print(sum(type(c) is str for c in list_1))
print(sum(type(c) is bool for c in list_1))
