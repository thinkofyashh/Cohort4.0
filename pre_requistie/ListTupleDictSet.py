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




