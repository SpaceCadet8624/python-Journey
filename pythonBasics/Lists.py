"""
Author: David Okoro
Date: 27/04/2026 (Day #3)
Purpose : Learning about lists and how to work with the elements in a list
Song of the day : Jeanine by Kwame Adu
"""

#Good idea to make the name of a list plural 

"""
Practice #1: Names
Purpose: Storing the names of people in a list and printing them individually through their index

"""
persons = ['Nolan','Mark','Oliver','Cecil','Debbie']#Using proper naming style for lists 

#Printing out the list elements
print(persons[-5])#0
print(persons[-4])#1
print(persons[-3])#2
print(persons[-2])#3
print(persons[-1])#4
#Special syntax for getting the last element in a list
print('\n')

"""
Practice #2: Greetings
Purpose: Improve the previous list to print a the names with a specialized message for each person
"""

#These are characters from invincible the prime video series
print(f"{persons[1]} you're always getting beat up for someone who's invincible")
print(f"{persons[0]} what was it like growing up on Viltrum?")
print(f"{persons[2]} bro, chill out!!!")
print(f'"{persons[3]}, I need you, {persons[3]}"- Mark') #Figured out how to print double quotes inside lists f-strings can also be f''
print(f"I can only imagine how hard it is for {persons[-1]} to see her sons leave to fight in a war in space")
print('\n')

"""
Practice #3: My own list
Purpose: Just something similar to practice #2 just to reinforce it
"""
transports = ['Car','AIRPLANE','wAlKinG']
print(f"I like going on long {transports[0].lower()} rides with family and friends")
print(f"I remember the first time I went on an {transports[1].lower()} for the first time")
print(f"When I go {transports[-1].lower()} it's usually to clear my mind")
print('\n')

"""
Practice #4: Guest List
Purpose: A little bit more complex list challenge
"""
guests = ['Jesus','Jack','Greg']
print(f"Hello {guests[0]} I'm having dinner and I wanted to send out an invite to you, I feel you could teach me a lot about myself and my faith")
print(f"Hello {guests[1]},was wondering if you would be free this saturday, I'm hosting dinner and would love for you to come")
print(f"Hello {guests[2]} dinner at my place today @7pm you still coming ? ")
print('\n')

#Just found out Greg won't be able to make it again
print(f"{guests[2]} just told me he won't be able to make it again to dinner, something urgent came up")
print('\n')

#Have to modify the list to invite someone else in his place
guests[2] = 'Bethany'
print(guests)
print(f"Hello {guests[0]} I'm having dinner and I wanted to send out an invite to you, I feel you could teach me a lot about myself and my faith")
print(f"Hello {guests[1]},was wondering if you would be free this saturday, I'm hosting dinner and would love for you to come")
print(f"Hello {guests[2]} thank you for making time for this on short notice")
print('\n')

#Just found a bigger table I can invite more guests
#Will be making use of both the insert() and append() methods to add new elements to my guestlist

guests.insert(1, 'Maria')#We have to include the index of where we want to place our element
guests.insert(0, 'Roger')
guests.append('Timmy')#append automatically adds to the end
print(guests)

#Getting the length of a list
numGuests = len(guests)
print(f"I have {numGuests} guests coming for dinner today")



print(f"{guests[0]}, will you be able to make it to dinner today?")
print(f"{guests[2]},{guests[0]} said he's coming over for dinner do you want to tag along?")

#I have no idea the number of elements now and going back would ruin my work flow so I use -1 to get the  last element
print(f"Heyy {guests[-1]}, I have a lot of friends coming over and would love to introduce you to them")
print('\n')

#Just found out my new table won't arrive on time
print('You can only invite two guest')
removedGuest = guests.pop()
print(f"Sorry about the inconvinience {removedGuest}")#Removed Timmy

removedGuest = guests.pop()
print(f"Sorry about the inconvinience {removedGuest}")#Removed Bethany

removedGuest = guests.pop(2)
print(f"Sorry about the inconvinience {removedGuest}")#Removed Maria

removedGuest = guests.pop(0)
print(f"Sorry about the inconvinience {removedGuest}")#Removed Roger

print(guests)

print(f"{guests[0]} you're still my number one guest")
print(f"{guests[-1]} you're still on the list bro")

#Deleting from the list
del guests[0]
del guests[-1]
print(guests)#Prinitng out an empty list


"""
session 2
Purpose : Learning how to order lists 
"""

"""
#Practice #1: Seeing The World
Purpose: Get comfortable using list ordering functions 

"""
destinations = ['Japan','Brazil','Spain','Jamaica','Peru']
print(destinations)#Printing list in it's original order

#The sorted() method prints the list in alphabetical order temporarily
print(sorted(destinations))
#Back to orginal order
print(destinations)

print(sorted(destinations,reverse=True))#Printing list in reverse alphabetical order but temporarily
print(destinations)

destinations.reverse()#Prints list in reverse order 
print(destinations)

destinations.reverse()#Printing back to normal order 
print(destinations)

destinations.sort()#Permanent way of sorting lists
print(destinations)

#Sorting alphabetically ordered lists to a reverse-alphabetically ordered list
destinations.sort(reverse= True)
print(destinations)

#I wonder how long this would have been in c++


