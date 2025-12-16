#create a tuple of your favorite 5 fruits.then print:
#the total number of fruits. the index of one selected fruit.
fruitstuple = ("Mango", "Orange", "Banana", "Grape", "Apple")
print(len(fruitstuple))
print("The selected fruit:", fruitstuple[2])

#ask the user for their 3 favorite movies and store them in a list 

movies = input("Enter a three favorite movies:")
liststore = []
liststore.append(movies)
print(liststore)
print(type(liststore))

#create a tuple of marks(87, 64,33,95,76) and print the highest and lowest marks using max() and min()
newtuple = (87,64,33,95,76)
print("The max value:",max(newtuple))
print("The min value:",min(newtuple))

#write a program to check grade based on marks(A/B/C/D) USING if-elif-else
marks = 99
if(marks >= 90):
    print("A", marks)
elif(marks >= 70):
    print("B", marks)
elif(marks >= 50 ):
    print("C", marks)
elif(marks >= 30):
    print("D", marks)
else:
    print("fail")
   