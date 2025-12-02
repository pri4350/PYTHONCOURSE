#write a program that: take a sentence as input converts it to lowercase replace all space "" with underscores "_"
#prints the new string
sentence = input("Enter the sentence:")
print(sentence.lower())
print(sentence.replace(" ", "_"))

#1.write a program that takes a sentence : total characters(len())
#uppercase version, lowercase version
sentence2 = ("Blue is a Sky")
total = len(sentence2)
print(total)
print(sentence2.upper())
print(sentence2.lower())

#2.write a python program that taken any word or sentence as input and prints. the fist character
#the last charcter , the total number of characters
word = input("Enter a statement:")
print("The first character:", word[0])
print("The last character:", word[-1])
print("The Total character:", len(word))
