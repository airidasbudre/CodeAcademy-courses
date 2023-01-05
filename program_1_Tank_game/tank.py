class Tank():
    def __init__(self, decision):

        tank_y = 5
        tank_x = 5
        self.tank_x = tank_x
        self.tank_y = tank_y

    
        tank = "\U0001F52B" 
        self.tank = tank

        dot = " -"
        self.dot = dot

        self.decision = decision
        shot_direction = "w"
        self.shot_direction = shot_direction
        
        if self.decision == "n" or self.decision == "w" or self.decision == "e" or self.decision == "s":
            shot_direction = self.decision
            print(f"{shot_direction}")
        


    def move_north(self):
        if self.tank_y < 1:
                print("Cant move there!")  
        else:  
            self.tank_y -= 1
        
    def move_east(self):
        if self.tank_x > 9:
                print("Cant move there!")  
        else:  
            self.tank_x += 1

    def move_south(self):
        if self.tank_y > 9:
                print("Cant move there!")  
        else:  
            self.tank_y += 1

    def move_west(self):
        if self.tank_x < 1:
                print("Cant move there!")  
        else:  
            self.tank_x -= 1
        
    def shot(self):
        west = 0
        self.west = west
        north = 0
        self.north = north
        south = 0
        self.south = south
        east = 0
        self.east = east 

        if self.decision == "w":
            self.west += 1 
        elif self.decision == "n":
            self.north += 1 
        elif self.decision == "s":
            self.south += 1 
        elif self.decision == "e":
            self.east += 1 
        print("Shot!")
        print(self.east)
    
    def info(self):
        tank_x = self.tank_x 
        tank_y = self.tank_y
      
        shot_direction = "w"
        # self.shot_direction = shot_direction
        if self.decision == "e" or self.decision == "w" or self.decision == "e" or self.decision == "s":
            shot_direction = self.decision
            print("yella2")
        else:
            print("no")
        print(f"Coordinates x:{tank_x}, y:{tank_y}. Direction:{shot_direction}. )")
        
    def grid(self):
        print(self.tank_x)
        print(self.tank_y)
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
