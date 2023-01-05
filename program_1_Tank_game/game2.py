from random import randint
from tank import Tank


decision = None
tankas = Tank(decision)

while True:
    decision = input("Whats next? ")
    if decision == "off":
        break
    elif decision == "info":
        tankas.info()
    else:
        if decision == "n":
            tankas.move_north()
        elif decision == "w":
            tankas.move_west()      
        elif decision == "s":
            tankas.move_south()
        elif decision == "e":
            tankas.move_east()
        elif decision == "q":
            tankas.shot()
            
        else:
            print("Wrong command")
    tankas.grid()
    