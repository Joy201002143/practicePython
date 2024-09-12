class person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def __del__(self):
        print("Object is de constructed")

class Vector:
    def __init__(self, x, y):
        self.x= x
        self.y=y
    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)

Vector1= Vector(10,20)
Vector2= Vector(50,60)
Vector3= Vector1+Vector2
print(Vector3.x)
print(Vector3.y)
# p= person("Joy",24)
# del p
