#print number from 1 to 100 usinga for loop.
for i in range(1,101):
    print(i)

#print numbers from 100 to 1 using a while loop.
num = 100
while num >= 1:
    print(num)
    num -= 1

#print all numbers between 1 and 50 except multiples of 5.
for j in range(1, 51):
    if j % 5 == 0:
        continue
    print(j, end=" ")

#create a program that asks the user for 5 favorite foods and prints them one by one.
favorite_food=[]
print("\nPlease enter your 5 favorite foods:")
for i in range(5):
    food = input(f"{i+1}.")
favorite_food.append(food)
print("\nHere are your favorite foods:")
for food in favorite_food:
    print(f"-{food}")

#print the sum of first 10 natural numbers using a while loop.
total_sum = 0 
i=1
while i <= 10:
    total_sum += i
    i += 1
print("The sum of the first 10 natural number is: ", total_sum)



