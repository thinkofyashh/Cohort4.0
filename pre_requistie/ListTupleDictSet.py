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



