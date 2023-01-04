from random import randint
from tank import Tank


decision = None
direction = None

tankas = Tank()

while True:
    yy[gun_y] = dot
    
    # input algorythm
    
    decision = input("Whats next? ")

    if decision == "off":
        break
    elif decision == "info":
        tankas.info()
    else:
        if decision == "n":
            tankas.move_north()
        elif decision == "w":
            if gun_y < 1:
                print("Cant move there!")  
            else:
                gun_y = tankas.move_west()      
        elif decision == "s":
            if gun_x > 9:
                print("Cant move there!")  
            else:
                gun_x = tankas.move_south()
        elif decision == "e":
            if gun_y > 9:
                print("Cant move there!")  
            else:
                gun_y = tankas.move_east()
        elif decision == "q":
            tankas.shot()
            
        else:
            print("Wrong command")
    
    
    
    # grid print
    # for i in range(x):
    #     if i == gun_x:
    #         yy[gun_y] = gun
    #         for i in yy:
    #             print(i, end=" ")
    #         print()
    #     else:
    #         for i in y:
    #             print(i, end=" ")
    #         print()