class Tank():
    def __init__(self, gun_xx, gun_yy):
        self.gun_x = gun_xx
        self.gun_y = gun_yy

    def move_north(self):
        return self.gun_x - 1
        
    def move_east(self):
        return self.gun_y + 1

    def move_south(self):
        return self.gun_x + 1

    def move_west(self):
        return self.gun_y - 1
        

    def shot(self):
        print("Shot!")

    def info(self):
        print("Information about your tank.")
        # print(decision)

      
gun_y = 5
gun_x = 5


# tankas = Tank(gun_x, gun_y)
    
gun = "\U0001F52B"   
dot = " -"
target = "x"
x = 11
y = [dot, dot, dot, dot, dot, dot, dot, dot, dot, dot, dot]
yy = y.copy()


while True:
    yy[gun_y] = dot
    
    tankas = Tank(gun_x, gun_y)
    # input algorythm
    
    decision = input("Whats next? ")
    if decision == "off":
        break
    elif decision == "info":
        print("info")
    else:
        if decision == "north":
            gun_x = tankas.move_north()

        elif decision == "west":
            gun_y = tankas.move_west()
             
        elif decision == "south":
            gun_x = tankas.move_south()

        elif decision == "east":
            gun_y = tankas.move_east()

        else:
            print("Wrong command")
    
    yy[gun_y] = gun

    # grid print
    for i in range(x):
        if i == gun_x:
            for i in yy:
                print(i, end=" ")
            print()
        else:
            for i in y:
                print(i, end=" ")
            print()

