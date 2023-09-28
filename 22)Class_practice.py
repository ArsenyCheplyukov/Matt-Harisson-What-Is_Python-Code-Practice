class Mario:
    """
    Class that emulates behavior
    """
    _MAXHEALTH = 4
    _SPEED = 4
    _STRENGTH = 4
    _JUMP = 4
    def __init__(self, health, coordinates=[0,0]):
        self.health = health
        self.coordinates = coordinates
    
    def add_health(self, health):
        if health < _MAXHEALTH:
            self.health += health
    
    def reduce_health(self, health):
        self.health -= health
    
    def jump(self):
        self.coordinates[1] += _JUMP
    
    def de_jump(self):
        self.coordinates[1] -= _JUMP
    
    def right(self):
        self.coordinates[0] += _SPEED
    
    def left(self):
        self.coordinates[0] -= _SPEED
    
    def information(self):
        print("This is Mario. Health points are: ", self.health, " and it is on coordinates: ", self.coordinates)

class Luigy(Mario):
    _SPEED = 3
    _STRENGTH = 5
    _JUMP = 3
    def information(self):
        print("This is Luigy. Health points are: ", self.health, " and it is on coordinates: ", self.coordinates)

class Tod(Mario):
    _SPEED = 5
    _STRENGTH = 2
    _JUMP = 5
    def information(self):
        print("This is Tod. Health points are: ", self.health, " and it is on coordinates: ", self.coordinates)

class Princess(Mario):
    _SPEED = 2
    _STRENGTH = 3
    _JUMP = 2

    def fly_to_coordinates(self, coordinates):
        self.coordinates = coordinates

    def information(self):
        print("This is Princess. Health points are: ", self.health, " and it is on coordinates: ", self.coordinates)

princess = Princess(100)
princess.fly_to_coordinates([10,29])
princess.information()