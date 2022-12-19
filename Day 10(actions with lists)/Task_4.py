from operator import attrgetter

# Sukurti programą, kuri:

# + Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# + Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
# + Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# + Įdėti sukurtus Zmogus objektus į naują sąrašą
#  Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)
# Patarimai:

# Naudoti sorted, attrgetter, reverse, funkciją repr
# from operator import attrgetter

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return(f"({self.name}, {self.age}")

person1 = Person("Antanas", 18)
person2 = Person("Gedas", 30)

list_1 = [person2, person1]

print(list_1)
    
sorted = sorted(list_1, key=attrgetter("age"))
print(sorted)


