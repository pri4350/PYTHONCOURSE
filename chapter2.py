#write a program that taken numbers and prints: .their sum, difference and product
#whether the first number is greater than secounde
sum = int(input("Enter the number 1:"))
difference = int(input("Enter the number 2:"))
print("Sum:", sum + difference)
print("Difference", sum - difference)
print("Product:", sum * difference)

great = sum > difference
print("The greater than value:", great)

#write are data types in python ? list any 4 with examples.
#example 
age = 20
area = 10.1
name = "priyanka"
num = 10 > 11 
print("The age:", age ,type(age))
print("The area:", area, type(area))
print("Name is :", name , type(name))
print("The num is : ", num, type(num))

#what is the difference between implicit and explicit type conversion?give one example of each.
num1=10
num2=10.5
result = num1 + num2
print("The implicit and explicit value:", result)
print(type(result))

#what are operators in python? Explain any three types with example.
x = 10
y = 15
print("The Arithmetic value : ", x + y)
print("The Comparison value :", x == y)
print("The Logical value :", x or y)

#smart temperature Canverter
c = int(input("Enter temperature in Celsius:"))
fahrenheif = (c*9/5) + 32
kelvin = c + 273.15
print("The Fahreheit:", fahrenheif)
print("The Kelvin:", kelvin)

#Bill split Calculator
total = float(input("Total bill:"))
friends = int(input("Friends:"))
pay = total / friends
print("Total Bill:",type (total))
print("The friends:", type(friends))
print("The bill on pay:", type(pay))

#Section c:-Application /output-based 
x=5
y=2.0
print(x//y)
print(x**y)