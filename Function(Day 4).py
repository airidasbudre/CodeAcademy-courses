# Task 1.1

import copy
from datetime import timedelta, datetime


def Sum_1():
   a = int(input("Input first numbers: "))
   b = int(input("Input second numbers: "))
   c = int(input("Input third numbers: "))
   d = a + b + c
   print(d)

# Task 1.2

def sum_2():
    total = 0
    a = None
    list_1 = []
    while not a == "stop":
        a = input("Input first numbers: ")
        if a == "stop":
            break
        list_1.append(a)
    list_2 = [eval(i) for i in list_1]
    
    for i in list_2:
        total = total + i
    print(total)
    return total

# Task 1.3
list_1 = [11, 2, 16, 10, 5]
def biggest_number(list_1):
    big = None
    for i in list_1:
        if i == list_1[0]:
            big = i
        elif big < i:
            big = i   
        else:
            continue
    print(big)

# Task 1.4
def reverse_string():
    a = input("Input something: ")
    print(a[::-1])


# Task 1.5
def string_info():
    # How many words
    a = input("Input something: ")
    b = a.split()
    print(len(b))
    
    # How many upper case letters
    uppercase_count = sum(1 for char in a if char.isupper())
    print(uppercase_count)

    # How many lower case letters
    lowercase_count = sum(1 for char in a if char.islower())
    print(lowercase_count)

# Task 1.6
def sorted_list():
    list_6 = [1, 3, 1, 6 , 6]
    list_6 = sorted(set(list_6))
    print(list_6)


# Task 1.7
# Program to check if a number is prime or not
def prime_numbers():
    # To take input from the user
    num = int(input("Enter a number: "))

    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

# Task 1.8

def reverse_string():
# How many words
    a = input("Input something: ")
    list_4 = a.split()
    list_4.reverse()
    print(list_4)

# Task 1.9

def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  # Else it is not a leap year  
  else:  
    print ("Given Year is not a leap Year")  
# Taking an input year from user  
# Year = int(input("Enter the number: "))  
# Printing result  

# Task 1.10
def count_date():

    insert_data = input("Insert date and time: ")
    data = datetime.strptime(insert_data, "%Y %m %d %H:%M:%S")
    
    skirtumas = (datetime.now() - data)
    print(skirtumas(skirtumas / 30))
    print(skirtumas)
    print(f"difference in days {skirtumas.days}")


# Task 2.1
list_of_strings = []
a = input("Input your personal code: ")

# Copy with string values
for i in a:
    list_of_strings.append(i)
list_of_strings[3] = list_of_strings[3] + list_of_strings[4]
list_of_strings[5] = list_of_strings[5] + list_of_strings[6]
list_of_strings.remove(list_of_strings[4])
list_of_strings.remove(list_of_strings[5])

#Copy with integers values
list_of_integers = []
for i in a:
    list_of_integers.append(int(i))
print(list_of_integers)

#Check if the values are correct
if len(list_of_strings) == 9:
   print(" Lenth OK")
   lenth = True  
if int(list_of_strings[0]) <= 6 and int(list_of_strings[0]) > 0 :
   print("first number ok")
if int(list_of_strings[3]) < 13 and int(list_of_strings[3]) > 0:
    print("month is ok")
if int(list_of_strings[4]) < 32 and int(list_of_strings[4]) > 0:
    print("day is ok")
else: 
    print("wrong")

#Personal code contral number check

s = list_of_integers[0]*1 + list_of_integers[1]*2 + list_of_integers[2]*3 + list_of_integers[3]*4 + list_of_integers[4]*5 + list_of_integers[5]*6 + list_of_integers[6]*7 + list_of_integers[7]*8 + list_of_integers[8]*9 + list_of_integers[9]*1

if s % 11 != 10:
    k = s % 11 
    if k == list_of_integers[10]:
        print("Personal code is walid")    
else:
    s_2 = list_of_integers[0]*3 + list_of_integers[1]*4 + list_of_integers[2]*5 + list_of_integers[3]*6 + list_of_integers[4]*7 + list_of_integers[5]*8 + list_of_integers[6]*9 + list_of_integers[7]*1 + list_of_integers[8]*2 + list_of_integers[9]*3
    if s_2 == list_of_integers[10]:
        print("ok")
    else:
        print("Personal code not walid!")



# print(b)


# Sum_1()
# sum_2()
# biggest_number(list_1)
# reverse_string()
# string_info()
# prime_numbers()
# reverse_string()
# CheckLeap(Year)
# count_date()
# sorted_list()
