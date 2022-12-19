# Sukurti programą, kuri:

# Prie kiekvieno sakinio "The Zen of Python" žodžio pridėtų šauktuką ir atspausdintų naują sakinį.
# Patarimai:

# Naudoti map (su lambda) arba comprehension, " ".join()

a = "The Zen of Python"

b = a.split()
c = map(lambda x: x+"!" , b)


print(list(c))
a.join(c)
print(a)
