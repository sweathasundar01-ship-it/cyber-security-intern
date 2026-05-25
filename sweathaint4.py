'''a= int(input("Enter the year:"))
if (a % 4 == 0 ):
    print(a,"it is leap year")
else:
    print(a,"it not leap year")

a=int(input("Enter the value:"))
if a % 2 !=0:
    print(a,"is even")
else:
    print(a,"is odd")



age=int(input("Age:"))
if age < 5:
    print("free for kids")
elif age >= 5 and age <  15:
    print("your entry amount is 300")
elif age >= 15  and age < 35:
    print("Your entry amount is 400")
elif age >=35 and age < 60:
    print("Your entry amount is 500")
elif age >=60 and age < 80:
    print("Your entry amount is 600")
else:
    print("You are not allowed for the themepark")

age=int(input("Enter the age:"))
test=input("you are already take the test?(yes/no):")
if age <18:
    print("you are under 18")
elif age >= 18 and test =="yes":
    print("you are eligible for license")
elif age >=18 and test=="no":
    print("You are not eligible for lincense")

mark=int(input("Enter the mark:"))
attendance=int(input("Enter the attendance percentage:"))
if mark >=50 and attendance >= 75:
    print("You are passed with good attendance!")
elif mark >= 50:
    print("You are passed but attendaance is low!")
elif mark <=50:
    print("you are fail but attendance is good")
else:
    print("both is low")
'''

a=int(input("Enter the mark1:"))
b=int(input("Enter the mark2:"))
c=int(input("enter the mark3:"))
print("person1",a)
print("person2",b)
print("person3",c)
total=a+b+c
print("total=",total)
if a >= b and a >= c:
    print("Person1 is greater")
elif b >= a and b >= c:
    print("Person2 is greater")
else:
    print("Person3 is greater")

