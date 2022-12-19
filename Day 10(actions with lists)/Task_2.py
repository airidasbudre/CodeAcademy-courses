from statistics import mean, median

# Sukurti programą, kuri:

# + Sukurtų sąrašą iš skaičių nuo 0 iki 50
# + Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
# + Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
# + Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
# + Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
# + Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
# Patarimai:

# Naudoti map, filter arba comprehension, sum, min, max, mean, median, %
# from statistics import mean, median


list_1 = [x for x in range(0, 51)]
print(list_1)

list_2 = map( lambda x: x*10, list_1)
print(list(list_2))

list_3 = filter((lambda x: x % 7 == 0), list_1)
print(list(list_3))

list_4 = [x ** 2 for x in list_1]
print(list(list_4))

print(sum(list_4))
print(min(list_4))
print(max(list_4))
print(mean(list_4))
print(median(list_4))

list_4.sort(reverse = True)
print(list_4)

