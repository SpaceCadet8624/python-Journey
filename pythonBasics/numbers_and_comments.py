#DAY 1 session 2:
# Date: 27/04/2026 
#Purpose: Learning about numbers and how to comment on python //I only know how to do single line comments

#This is how you make a single-line comment


""""
This is how you make a multi-line comment note: Not a real comment but the interpreter knows to ignore it
"""

'''
Practice #1: Number Eight 
Purpose: Practicing python arithmetic operators by making each operation result in the number 8
'''
print(16/2) # How do I convert data types because output will be a float and I need an integer
print(int(16/2)) #Searched this up
print(4+4)
print(10-2)
print(4*2)

'''
Practice #2 : Favorite number
Purpose: Practice asking for user input and storing the result in a variable then printing the result
'''
fav_Num = input('What is your favorite number?:') #Asking for user input just like cin in c++
response = f"Your favorite number is {fav_Num}"
print(response)

'''
Practice #3 : Temperature Converter
Purpose: Prompts the user to enter the temperature in celsius then converts it to fahenreit 
'''
temp = input('What is the temperature in celsius?')#Prompting the user

conversion = float((int(temp) * 9/5) + 32) #Converting from celsuis to fahenreit 
#Had an error in line 36 I was trying to do arithmetic with a string and int values corrected it by changing str to int

print(f"{temp} degrees celsius is {conversion} in fahenreit")
