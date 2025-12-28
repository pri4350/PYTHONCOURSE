#3.create a function good_morning() that prints "Good morning, saumya".call it twice.
def good_morning():
    print("Good Morning, saumya di")
good_morning()

#4.write a function display_python() that prints "python is fun!".
def display_python():
    print("Python is fun!")
display_python()

#5.create a function learn() that prints three python topics.
def learn():
    print("1.Tuples and sets.")
    print("2.Loops concepts.")
    print("3.Conditional Statements.")
learn()

#6.createa function add-number(a,b) that prints both the sum and difference.
def add_number(a,b):
    print(f"That is sum:{a+b}")
    print(f"That is difference:{a-b}")
add_number(10,15)

#7.write a function fav_food(food) that prints "Saumya, loves <food>".
def fav_food(food):
    print(f"Saumya di , loves {food}")
fav_food("Samosa")

#8.create a function convert_to_upper(word) that return the uppercase version of the string.
def convert_to_upper(word):
    return word.upper()
uppercase = convert_to_upper("priyanka")
print(uppercase)

#9.create a function full_name(f"name, 1name) that return the full name joined with a space.
def full_name(name):
    return name
fullname = full_name("Priyanka Bhole")
print(fullname)

#10.write a function to calculate the factorial of a number.
def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    return ans
print(factorial(5))
    
#11.write a function that check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))

#12.write a function greet_user(name) that prints a personalized message for saumya singh.
def greet_user(name):
    print(f"Hello, {name}! Welcome to the program.")
greet_user("Saumya Singh")

#13.writw a function to return the largest of 3 numbers.
def largest_of_three(a, b, c):
    return max(a, b, c)
print(largest_of_three(10, 25, 15))

#14.write a function that return both the sum and average of 5 inputs.
def sum_and_average(a, b, c, d, e):
    total = a + b + c + d + e
    average = total / 5
    return total, average
total, avg = sum_and_average(10, 20, 30, 40, 50)
print(f"Sum: {total}, Average: {avg}")

#15.write a program to count vowels in a string using a function.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Priyanka bhole"))
