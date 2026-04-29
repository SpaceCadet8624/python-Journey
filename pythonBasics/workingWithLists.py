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
pizzas = ['pepperoni','cheese','hawaian']

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

print('Any of these animals would make a great pet')


"""
Session #2
Making Numerical Lists
"""
#Do later today
