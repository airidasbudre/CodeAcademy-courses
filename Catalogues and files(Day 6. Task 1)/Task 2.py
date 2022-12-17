
# Sukurti programą, kuri:

# Leistų vartotojui įvesti norimą eilučių kiekį
# Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
# Įrašytų įvestą tekstą atskiromis eilutėmis į failą
# Patarimai:

# Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)

text = None
while True:
    input_text = input("Input text: ")
    if text == None:
        text = input_text
    if not input_text:
        break
    else:
        text += input_text + "\n"
    
with open(input("Input file name with .txt: "), 'w', encoding="utf-8") as failas:
    print(failas.write(text))