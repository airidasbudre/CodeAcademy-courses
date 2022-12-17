# Perdaryti 1 užduotį taip, kad spausdinant sakinio objektą, spausdintų ne objekto adresą, o įvestą tekstą


class Sakinys:
    def __init__(self, text=input("Input text: ")):
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
        



sakinys = Sakinys()
sakinys.reverse()
sakinys.lower()
sakinys.upper()
sakinys.write_from()
sakinys.count_symbols_and_words("Ai")
sakinys.replace()
sakinys.count()
