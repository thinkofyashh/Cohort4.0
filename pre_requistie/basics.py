

name: str ="Yash "
print(type(name))
print(isinstance(name ,str)) 


#immutable 
a:int = 1
b:int =a

b=2
print(b)
print(a)


#mutable 
fruits:list =["apple","banana","watermelon"]

fruit:list=fruits
fruit.append("oranges")

print(fruit)
print(fruits)


#is and in operator 
if a is 1:
    print("it is true it is damn true ")

if "oranges" in fruit:
    print("It is present in the array ")





# function checking 
def is_age(age:int)->str : 
    return "You are eligible" if(age>=18) else "Not Eligible"

print(is_age(12))