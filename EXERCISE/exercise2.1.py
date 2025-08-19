#"area of rectangle
length=float(input("Enter length of rectangle: "))
width=float(input("Enter the : "))
#area calculation
area=length*width
print("The area of rectangle is: "+ str(area) +"m\u00b2")

#determine whether is even or odd
num=int(input("Type a number:"))
if num%2==0:
    print("its even number")
else:
    print("its odd number")

#To fing the largest of three numbers
num1=input("First number: ")
num2=input("Second number: ")
num3=input("Thirdnumber: ")
#to pick the largest number, we will use if function
if num1>num2 and num2>num3:
    print("The largest number is :", num1)
elif num2>num1 and num2>num3:
    print("The largest number is :", num2)
else:
    print("The largest number is :", num3)

#to convet temp. into fahrenheit
temp=input("enter temp. in celsius: ")
temp=float(temp)
temp=(temp+32)
print("The temp. in fahraanheit is: ",temp)


