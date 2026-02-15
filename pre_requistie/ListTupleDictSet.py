import dog
from dog import bark
#from lib import dogss
from lib import dogsss
from lib.dogsss import yo
from functools import reduce 

#list

dogs:list=["German","Syberian Husky",1,"Lebra",True,7]

print(dogs[-2])
print(dogs[2:4])
print(dogs[:3])
print(dogs[3:])
print(len(dogs))

dogs.append("Pitbull")
print(dogs)
dogs.remove("German")
print(dogs)
dogs.extend(["German","Rotwelier"])
print(dogs)
dogs+=["Desi Dog"]
print(dogs)

dogs.insert(3,"shizu")
print(dogs)

# if you want to put multiple items in the list . so for that we have to use slice .

dogs[1:1]=["test1","test2"]
print(dogs)

#sorting the list 
names:list =["Raju","Panver","Yash","Rawat","yashu","chaudhary"]

names.sort(key=str.lower)
print(names)

#if you want that list to be returned new. it should not return the modified list .

sorted_names=sorted(names,key=str.lower)
print(sorted_names)


#tuples - it cant be modified .

colors:tuple=("Green","yellow","pink","Brown")

newColors=sorted(colors,key=str.lower)

colors1=colors+("Blue","White","black")
print(colors1)

print(newColors)



#dictionary 

students={
    "Name":"Yash",
    "Branch":"CSE",
    "age":"24"
}

#if you want to access the value stored in the key .
print(students["Name"])

#if you want to set certain key a default value or a safer way to extract value .
students.get("Marks",0)
print(students.get("Name"))
print(students)

#adding and updating the Dict
print("After adding into the dictionary")
students["Marks"]=27
print(students)

print("After updating the dictionary ")
students["age"]=18

print(students)

#removing the key from the dictionary 

del students["age"]
students.pop("Marks")

print(students)

#students.clear()


print(students)

#dict with for loop

for key in students:
    print(key,students[key])


print(students.values())
print(students.keys())
print(students.items())

for key,value in students.items():
    print(key,value)

#chekcing if the key exists or not .

if "Name" in students:
    print("Key exists")

#copying into the dictionary 

new_info=students.copy()

print(new_info)

print("Copied dict")
print(new_info)

#merging of dict 

dict1={"address":"7A"}
dict2={"city":"New delhi"}

result = dict1 | dict2

print(result)


#set  - it can store only the unique element .

set1={"Roger","daniel","Luna"}

set2={"Luna"}

mod= set1-set2

print(mod)

res=set1 |set2
print(res)

result=set1 & set2
print(result)

#functions - lets talk about the function .


def hello(name="My friends"):
    print("Hello "+ name)


hello("yash")
hello()

# if the object passed is immutable .

def change(value):
    value=32

val=23
change(val)
print(val)

#if the object passed is unmutable .

def change1(value):
    value["name"]="Chaudhary"

value={"name":"Yash"}
change1(value)
print(value)

# return function 

def hello(name):
    print("hello my name is "+ name)
    return name,"beaue",8

print(hello("yash"))


# global variable 

age=10

def test():
    print(age)


print(age)
test()

# nested function 

def talk(phrase):
    def say(word):
        print(word)

    words=phrase.split(" ")
    for word in words:
        say(word)

talk("hello my name is Yash Rawat .")


#closures in the function 

def outer():
    count=0

    def inner():
        nonlocal count
        count+=1
        return count    
    return inner

fn=outer()
print(fn())
print(fn())
print(fn())


#objects 

age =12

print(age.real)
print(age.imag)

print(age.bit_length())
print(id(age))


#loops 


i=0
while i<5:
    print(i)
    i=i+1


items:list=[1,2,3,4]

print("for loop ")

for item in items:
    print(item)

#for loop with the range function 
print("for loop with the range function ")
for item in range(14):
    print(item)

# if you want to print enumerateor (means with the index)

for index,item in enumerate(items):
    print(index,item)    



 #classes 


class Dog:


    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def bark(self):
        print("Woof !")


roger=Dog("German",12)
print(roger)

print(roger.name)
print(roger.age)
roger.bark()




dog.bark()


bark()

#dogss.barking()

dogsss.yo()

yo()


#lambda function 

multiply=lambda a,b : a*b

print(multiply(1,2))

#map -> when you want to run fn for every item in the list 

numbers:list = [1,2,3]

result=map(lambda a: a*2,numbers)

print(list(result))

#filter -> when you want to filter in the list based on certain condtion 

result1=filter(lambda a : a%2==0,numbers)
print(list(result1))

#reduce 

nums:list=[1,2,3,4]

result=reduce(lambda x,y: x*y,nums)
print(result)

#resursion 
print("recursion")
def fact(n):
    if(n==1):
        return 1
    
    return n*fact(n-1)

print(fact(4))


#decorator 

def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper()    

def say_hello():
    print("Hello There my Name is Yash Rawat")

func=my_decorator(say_hello)   
print(func)