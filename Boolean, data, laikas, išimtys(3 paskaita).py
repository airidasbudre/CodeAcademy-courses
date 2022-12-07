from datetime import timedelta, datetime


# task 1

# positive = True

# while positive == True:
#     try:
#         a = int(input("Insert the number: "))

#         if a > 0:
#             print(positive)
#         else:
#             positive = False
#             print(positive)
#     except ValueError:
#         print("Neteisingas")


# ------------------------------------------

# task 2

# time_and_date = datetime.today()
# print(time_and_date)
 
# print(time_and_date - timedelta(days=5))
# print(time_and_date + timedelta(hours=8))
# print(time_and_date.strftime("%Y %m %d, %H:%M:%S"))

# ----------------------------------------------------

# task 3

# insert_data = input("Insert date and time: ")
# data = datetime.strptime(insert_data, "%Y %m %d %H:%M:%S")
# skirtumas = (datetime.now() - data)
# print(skirtumas)
# print(f"difference in days {skirtumas.days}")

# skaicius = 4.66
# print(round(skaicius))

# print(f"difference in months {skirtumas.days / 30}")
# print(f"difference in year {skirtumas.days / 30 / 12}")
