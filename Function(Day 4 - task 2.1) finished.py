# Task 2.2
import random

personal_code = []
x = []
date = []
insert_data = input("Insert date. yyyy-mm-dd format: ")
insert_gender = input("Insert your gender. m or f:  ")


# Put date in the list

date = insert_data.split("-")

print(date)

# Generate first number 
if insert_gender == "m":
    if int(date[0]) > 1799 and int(date[0]) < 1900:
        personal_code.append(str(1))
    elif int(date[0]) > 1899 and int(date[0]) < 2000:
        personal_code.append(str(3))
    elif int(date[0]) > 1999 and int(date[0]) < 2099:
        personal_code.append(str(5))
elif insert_gender == "f": 
    if int(date[0]) > 1799 and int(date[0]) < 1900:
        personal_code.append(str(2))
    elif int(date[0]) > 1899 and int(date[0]) < 2000:
        personal_code.append(str(4))
    elif int(date[0]) > 1999 and int(date[0]) < 2099:
        personal_code.append(str(6))

# Datos pridėjimas
years = str(date[0])
personal_code.append(str(years[2]+str(years[3])))
personal_code.append(date[1])
personal_code.append(date[2])

h = random.randint(1, 999)
personal_code.append(str(h))
print(personal_code)

personal_code_2 = personal_code[0] + personal_code[1] + personal_code[2] + personal_code[3] + personal_code[4] 

for integer in personal_code_2:
    x.append(int(integer))


#Personal code contral number check
k = 0
s = x[0]*1 + x[1]*2 + x[2]*3 + x[3]*4 + x[4]*5 + x[5]*6 + x[6]*7 + x[7]*8 + x[8]*9 + x[9]*1
print(s)
if s % 11 != 10:
    k = s % 11 
    print("Personal code is walid")    
    x.append(k)
else:
    s_2 = x[0]*3 + x[1]*4 + x[2]*5 + x[3]*6 + x[4]*7 + x[5]*8 + x[6]*9 + x[7]*1 + x[8]*2 + x[9]*3
    if s_2 % 11 != 10:
        x.append(k)
        print("ok")
    else:
        x.append(0)
        print("Personal code not walid!")
