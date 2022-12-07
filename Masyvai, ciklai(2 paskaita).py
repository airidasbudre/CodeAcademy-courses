import random
import sys

# 1 task

# list_1 = [1, 2 , 3, 4]
# print(list_1[2])
# list_1.append(25)
# print(list_1)
# list_1.remove(2)
# print(list_1)
# list_1[0] = 10
# print(list_1)
# ------------------------------------------

# 2 task
# -------------------------------------------
# number = 0
# final = 0

# while number >= 0:
#     number = float(input("Insert number: "))
#     if number >= 0: 
#         final = final + number 
# print(f"Bendra suma:{final}")
# --------------------------------------------

# 3 task
# ---------------------------------------------
# list_2 = []
# current = 0
# amount_of_words = int(input("How many words? "))

# while amount_of_words > current:
#     list_2.append(input("Input names: "))
#     current += 1 
# print(list_2)

# in_list = 0

# for i in list_2:
#     print(i)
#     print(len(i))
#     in_list += 1 
#     print(f"Pozition: {in_list}")
# ---------------------------------------------

# 4 task
# ---------------------------------------------

list_3 = []
i = 0

while i < 3:
    a = random.randint(1,6)
    list_3.append(a) 
    i += 1
print(list_3)

for n in list_3:
    if n == 5:
        print("Lose")
        sys.exit()

print("Winner")