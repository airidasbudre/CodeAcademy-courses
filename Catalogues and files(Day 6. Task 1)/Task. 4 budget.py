import pickle

# Sukurti minibiudžeto programą, kuri:

# Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
# Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
# Atvaizduotų jau įvestas pajamas ir išlaidas
# Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)

#1 ivesti pajamas arba išlaidas. Input i file


while True:
    decision = input("""1 - Add income/expenses,\n2 - Print all income and expenses,\n3 - Print balance
    -""")
    if decision == "2":
        try:
            with open("budget.pkl", 'rb') as failas:
                print(pickle.load(failas))
        except:
            print("Nėra tokio failo")
            with open("budget.pkl", 'wb') as failas:
                budget = []
                pickle.dump(budget, failas)
    if decision == "1":
        with open("budget.pkl", 'rb') as failas:
            budget = pickle.load(failas)
            income_expenses = int(input("Add amount"))
            with open("budget.pkl", 'wb') as failas:
                budget.append(income_expenses)
                pickle.dump(budget, failas)
    if decision == "3":
        with open("budget.pkl", 'rb') as failas:
            budget = pickle.load(failas)
        print(sum(budget))






