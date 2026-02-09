from enum import Enum 


class Color(Enum):
    Red=1
    Green=2
    Blue=3

print(Color.Blue) #Color.Blue
print(Color.Blue.name) #it will print Blue
print(Color.Blue.value) # it will print 3 .
print(list(Color))



