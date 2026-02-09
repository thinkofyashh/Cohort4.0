fruits:list=["oranges","apple","banana","guava"]

for fruit in fruits:
    if(fruit=="apple"):
        print(fruit)
        break


print("for loop ended and we git our apple ")



name: str="hello my name is yash rawat"



# it will print the llo my name is yash rawat 
print(name[2:])


# it will print the l
print(name[2:3])

# it will print the a starting from last index and then doing -- minus .
print(name[:-2])

name2="hello my name is yash rawat \n And my a Software Engineer at Samsung Electronics "

name3=[]

if name3:
    print("yes")
else :
    print("No")
print(name2)


done="True"

print(type(done)==str)


# all and any keyword

book_1_read=True
book_2_read=True
any_book_read=any([book_1_read,book_2_read])



all_book_read=all([book_2_read,book_1_read])

print(all_book_read)
print(any_book_read)



# we can also express the complex number in the pyhton using complex keyword


#where two is the imaginary part (j)
num=complex(2,3)

print(num.real,num.imag)
 
# round , abs built-in function 

num2=abs(-393)
print(num2)

num1=round(5.4)
print(num1)




