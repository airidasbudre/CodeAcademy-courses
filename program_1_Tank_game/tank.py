class Tank():
    def __init__(self):
        self.tank_x = tank_x
        self.tank_y = tank_y

        tank_y = 5
        tank_x = 5
        tank = "\U0001F52B" 
        self.tank = tank
        dot = " -"
        self.dot = dot

        self.decision = decision
        shot_direction = "w"
        self.shot_direction = shot_direction
        # west = 0
        # self.west = west
        # north = 0
        # self.north = north
        # east = 0
        # self.east = east
        # south = 0
        # self.south = south
        if self.decision == "n" or self.decision == "w" or self.decision == "e" or self.decision == "s":
            shot_direction = self.decision
            print(f"{shot_direction}")
        


    def move_north(self):
        # nepersikelia if dalis
        if self.tank_x < 1:
                print("Cant move there!")  
        else:  
            return self.tank_x - 1
        
    def move_east(self):
        return self.tank_y + 1

    def move_south(self):
        return self.tank_x + 1

    def move_west(self):
        return self.tank_y - 1
        
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
        tank_x = self.tank_x 
        tank_y = self.tank_y
      
        shot_direction = "w"
        # self.shot_direction = shot_direction
        if self.decision == "e" or self.decision == "w" or self.decision == "e" or self.decision == "s":
            #  or self.decision == "w" or self.decision == "e" or self.decision == "s"
            shot_direction = self.decision
            print("yella2")
        else:
            print("no")
        print(f"Coordinates x:.tank_x}, y:{tank_y}. Direction:{shot_direction}. Shots(West:{self.west}, North:{self.north}, South:{self.south}, East:{self.east})")
        
    def grid():
        
        tank = "\U0001F52B"   
        dot = " -"
        x = 11
        y = [dot, dot, dot, dot, dot, dot, dot, dot, dot, dot, dot]
        yy = y.copy()

        for i in range(x):
            if i == tank_x:
                yy[tank_y] = tank
                for i in yy:
                    print(i, end=" ")
                print()
            else:
                for i in y:
                    print(i, end=" ")
                print()
