from random import randint

class Tank():
    def __init__(self):
        self.tank_x = 5
        self.tank_y = 5

        self.west = 0
        self.north = 0
        self.south = 0
        self.east = 0
    
        self.tank = "\U0001F52B" 

        self.dot = " -"

        self.shot_direction = "w"

        self.points = 0 

        self.target_x = randint(0, 9)
        self.target_y = randint(0, 9)

    def move_north(self):
        if self.tank_y < 1:
                print("Cant move there!")  
        else:  
            self.tank_y -= 1
            self.shot_direction = "n"
        
    def move_east(self):
        if self.tank_x > 9:
                print("Cant move there!")  
        else:  
            self.tank_x += 1
            self.shot_direction = "e"

    def move_south(self):
        if self.tank_y > 9:
                print("Cant move there!")  
        else:  
            self.tank_y += 1
            self.shot_direction = "s"

    def move_west(self):
        if self.tank_x < 1:
                print("Cant move there!")  
        else:  
            self.tank_x -= 1
            self.shot_direction = "w"
        
    def shot(self):
        print("Shot!")
        if self.shot_direction == "w":
            self.west += 1 
            if self.target_x < self.tank_x and self.target_y == self.tank_y:
                print("You hit the target!")
                self.target_x = randint(0, 9)
                self.target_y = randint(0, 9)
                self.points += 1 
            else: 
                print("You missed the target")
        elif self.shot_direction == "n":
            self.north += 1 
            if self.target_y < self.tank_y and self.target_x == self.tank_x:
                print("You hit the target")
                self.target_x = randint(0, 9)
                self.target_y = randint(0, 9)
                self.points += 1 
            else: 
                print("You missed the target")
        elif self.shot_direction == "s":
            self.south += 1 
            if self.target_y > self.tank_y and self.target_x == self.tank_x:
                print("You hit the target")
                self.target_x = randint(0, 9)
                self.target_y = randint(0, 9)
                self.points += 1 
            else: 
                print("You missed the target")
        elif self.shot_direction == "e":
            self.east += 1 
            if self.target_x > self.tank_x and self.target_y == self.tank_y:
                print("You hit the target")
                self.target_x = randint(0, 9)
                self.target_y = randint(0, 9)
                self.points += 1 
            else: 
                print("You missed the target")
    
    def info(self):
        y_list = []
        for i in range(11):
            y_list.append(i)
        print(y_list)

        print(f"Coordinates x:{self.tank_x + 1}, y:{(y_list[-self.tank_y])}. Direction:{self.shot_direction}. Shots: n-{self.north}, e-{self.east}, s-{self.south}, w-{self.west}, total shots-{self.east + self.west + self.north + self.south}, points-{self.points} )")
        
    def grid(self):
        tank = "\U0001F52B"   
        dot = " -"
        y = 11
        x = [dot, dot, dot, dot, dot, dot, dot, dot, dot, dot, dot]
        xx1 = x.copy()
        xx2 = x.copy()
        xx3 = x.copy()

        target = " x"

        for i in range(y):
            if i == self.tank_y and i != self.target_y:
                xx1[self.tank_x] = tank
                for i in xx1:
                    print(i, end=" ")
                print()
            elif i == self.target_y and i != self.tank_y:
                xx2[self.target_x] = target
                for i in xx2:
                    print(i, end=" ")
                print()
            elif i == self.tank_y and i == self.target_y:
                xx3[self.tank_x] = tank
                xx3[self.target_x] = target
                for i in xx3:
                    print(i, end=" ")
                print()
            else:
                for i in x:
                    print(i, end=" ")
                print()
