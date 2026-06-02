import math

#Task 5: Extending a Class

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return (self.x == value.x) and (self.y == value.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance(self, value):
        return math.sqrt((value.x - self.x)**2 + (value.y - self.y)**2)


#Create a class called Vector which is a subclass of Point and uses the same __init__() method. 
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f"/{self.x}, {self.y}/"
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)


#point
p1 = Point(1,2)
p2 = Point(3,2)

print(p1)
print(p1 == p2)
print(p1.distance(p2))


#vector
v1 = Vector(2,4)
v2 = Vector(1,3)

v3 = v1 + v2
print(v3)
print(v3.distance(v1))







    