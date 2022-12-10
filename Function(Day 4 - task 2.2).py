# Task 2.2
import random


personal_code = []
personal_code_2 = []
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
personal_code.append(random.randint[1:999])
print(personal_code)





#Personal code contral number check

s = personal_code_2[0]*1 + personal_code_2[1]*2 + personal_code_2[2]*3 + personal_code_2[3]*4 + personal_code_2[4]*5 + personal_code_2[5]*6 + personal_code_2[6]*7 + personal_code_2[7]*8 + personal_code_2[8]*9 + personal_code_2[9]*1

if s % 11 != 10:
    k = s % 11 
    if k == personal_code_2[10]:
        print("Personal code is walid")    
else:
    s_2 = personal_code_2[0]*3 + personal_code_2[1]*4 + personal_code_2[2]*5 + personal_code_2[3]*6 + personal_code_2[4]*7 + personal_code_2[5]*8 + personal_code_2[6]*9 + personal_code_2[7]*1 + personal_code_2[8]*2 + personal_code_2[9]*3
    if s_2 == personal_code_2[10]:
        print("ok")
    else:
        print("Personal code not walid!")
