#create a dictionary storing meanings of 3 english words.
storingmeaning = {
    "Ephemeral": "Lasting for a veery short time;fleeting.",
    "Resilient":  "Able to withstand or recover quickly from difficult conditions.",
    "Eloquent": "Fluents or persuasive in speaking or writing."
}
print(f"{storingmeaning}")
print("\n")
#create a set of numbers and show union and intersection with another set.
setnum1 = {1,2,3,4,5}
setnum2 = {6,7,5,8,9,10}
Unionset = setnum1 | setnum2
intersection = setnum1 & setnum2
print("\nUnion :", Unionset.union())
print("\nIntersection: ", intersection.intersection())

#try to add both integer 9 and float 9.0 to a set and observe what happens.
mixedset = {9, 9.0}
print("set with 9 and 9.0:", mixedset)