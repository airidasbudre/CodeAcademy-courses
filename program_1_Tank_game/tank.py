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

        if self.shot_direction == "w":
            self.west += 1 
        elif self.shot_direction == "n":
            self.north += 1 
        elif self.shot_direction == "s":
            self.south += 1 
        elif self.shot_direction == "e":
            self.east += 1 
        print("Shot!")
    
    def info(self):
        print(f"Coordinates x:{self.tank_x}, y:{self.tank_y}. Direction:{self.shot_direction}.Shots: n-{self.north}, e-{self.east}, s-{self.south}, w-{self.west} )")
        
    def grid(self):
        tank = "\U0001F52B"   
        dot = " -"
        y = 11
        x = [dot, dot, dot, dot, dot, dot, dot, dot, dot, dot, dot]
        xx = x.copy()

        for i in range(y):
            if i == self.tank_y:
                xx[self.tank_x] = tank
                for i in xx:
                    print(i, end=" ")
                print()
            else:
                for i in x:
                    print(i, end=" ")
                print()