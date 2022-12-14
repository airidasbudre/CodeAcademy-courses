# Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:

# + Gražina tekstą atbulai
# + Gražina tekstą mažosiomis raidėmis
# + Gražina tekstą didžiosiomis raidėmis
# + Gražina žodį pagal nurodytą eilės numerį
# + Gražina, kiek tekste yra nurodytų simbolių arba žodžių
# + Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
# + Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# Susikurti kelis klasės objektus ir išbandyti visus metodus


class Sakinys:
    def __init__(self, text):
        self.text = text
    
    def reverse(self):
        print(self.text[::-1])

    def lower(self):
        print(self.text.lower())

    def upper(self):
        print(self.text.upper())

    def write_from(self):
        x = int(input("From with position print text? "))
        print(self.text[x:])
    
    def count_symbols_and_words(self, text):
        print(self.text.count(text))
        
    def replace(self):
        text = self.text
        print(self.text.replace("Airidas", "Denas"))

    def count(self):
        text = self.text
        print(f"symbols:{sum(len(x) for x in text.split())}, words:{len(text.split())}, upper:{len(text.upper())}") 
        



sakinys = Sakinys("Airidas Budreckis")
sakinys.reverse()
sakinys.lower()
sakinys.upper()
sakinys.write_from()
sakinys.count_symbols_and_words("Ai")
sakinys.replace()
sakinys.count()


