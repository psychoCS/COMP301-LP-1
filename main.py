from student import Student
from vector2d import Vector2D

tom = Student("Tom", 30, 301110875)

tom.saysHello()
tom.studies()

position1 = Vector2D(20.0, 30.1)
position2 = Vector2D(10.0, 10.0) 
position3 = Vector2D(100.3, 87.4)

position1 = position1 + position2

print(position1)

position4 = position3 - position2

print(position4)


#distance = Vector2D.Distance(position4, position2)
#print(distance)
