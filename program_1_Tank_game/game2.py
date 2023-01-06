from tank import Tank


tankas = Tank()


tankas.grid()
while True:
    decision = input("Whats next? Moves: w, e, n, s. Turn off: off. Information: info: ")
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