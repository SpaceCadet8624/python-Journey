"""
Author: David Okoro
Date: 28/04/2026 (Day #4)
Purpose : Learning how to loop through lists
Song of the day :  Cassette by Daniel Leggs
"""

#I am so tired but we keep on grinding

#for loop errors
#forgetting to indent, forgetting to indent additional lines, unnecessary indent, indenting after the for loop, forgetting the colon(:)
#Learn errors in python in c++ it's semantic error but in python it's logical error


"""
Practice #1a: Pizzas
Purpose: Getting familiar with using for loop in lists
"""
#Creating a list to store different kinds of pizza then printing them with a for loop
pizzas = ['pepperoni','cheese','hawaiian']

for pizza in pizzas:#for loop syntax
    print(pizza.title())
    print(f"I like {pizza} pizza \n") #Modifying list with f-string to print out pizza type in a sentence

#Indentation will controls the code block for the loop
print(f"{pizzas[2]} is my favorite kind of pizza\n")
print(f"The first kind of pizza I ever tried was {pizzas[0]} pizza \n")
print(f"I like cheese so I would definitely like {pizzas[1]} pizza \n")

print('In short I really really like pizza!!!')

"""
Practice #1b: Animals
"""
animals = ['dog','cat','parrot']

for animal in animals:
    print(animal.title())
    print('\n')

print(f"A {animals[0]} is usually energetic \n")
print(f"I used to be dislike {animals[1]}s growing up but that changed \n")
print(f"{animals[-1]}s have a really interesting trait\n")

print('Any of these animals would make a great pet \n')


"""
Session #2
Making Numerical Lists
Date: 29/04/2026
Sonng of the day:Famous by French Montana
"""
"""
Practice #1: Counting to twenty
Purpose: Using for loop to print out a list of numbers from 1 to 20 (mastering range function)
"""

digits = range(1,21)#off by one behaviour causes range to be lastVal - 1
for digit in range(1,21):
   print(digit,'\n')


"""
Practice #2: One Million
Purpose: Practicing min(),max(),sum() functions
"""
millions = list(range(1, 1000001))


print(min(millions))#Function to get the minimum value in a list
print(max(millions))#Function to get the maximum value in a list
print(sum(millions))#Function to get the sum of the values in a list
print('\n')

"""
Practice #3: Odd numbers
Purpose: Diving deeper into range function by using third arguement
code snippet that goes through a list of number and prints out the odd numbers
"""
oddNums= range(1,21,2)#range includes(start, last value, amount to skip)
for oddNum in oddNums:
    print(oddNum)
    print('\n')

#Practice 4
#Code snippet to use for loop to print multiples of 3 to 30
threes = []#Created an empty list
for three in range(3,31,3):#for loop to go through list starting from 3 ending at 30 and skipping 2 digits
   threes.append(three)#adding values of three to the empty list

print(threes)#printing the updated list

#Practice 5
#Using for loop and range functions to print out the cubes of number 1 to 10
cubes = []
for cube in range(1,11):
    cubes.append(cube ** 3)
    print(f"The cube of {cube} is {cube ** 3}")

 #writing code above in one line
cubes = [cube ** 3 for cube in range(1,11)]#List compprehension
print(cubes)
