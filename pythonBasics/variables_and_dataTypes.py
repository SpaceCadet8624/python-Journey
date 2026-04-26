#Author : David Okoro
#Date : 26/4/2026
#Purpose : To learn about variables and data types in Python
#Song of the day : Upside Down by Jack Johnson

#I have knowledge in c++ already and we were taught to properly comment our code 

#Variables practice:

#Practice #1 (Personal Message):
#Purpose: Declaring a variable to store a person's name and then printing a concatenated message to that person

id = "David" #Declaring a variable and initializing it with a string

#I will make use of f-strings to concatenate the  string variable with more strings
message = f"Hello {id}, would you like to learn some Python today? "

print(message) #Function to print out similar to cout output stream in c++


#Practice #2 (Name Cases):
#Purpose: Using case functions to manipulate the string variable
firstName = "John"
lastName = "Doe"
fullName = f"{firstName} {lastName}" 

#Printing in lowercase
print(fullName.lower())

#Printing in uppercase
print(fullName.upper())

#Printing in titlecase
print(fullName.title())


#Practice #3 (Concatenation and escaping characters):
#Purpose: Concatenate a qoute and who said it, and also escape double quotes within the string

quote = '"Be still. Watch and listen. I am the result of the love of thousands"' #I learnt that you can use different a form of qoutaion marks within another kind
person = 'Linda Hogan'

famousQuote = f"My favorite quote is: {quote} by {person}" #My actual favorite quote
print(famousQuote)

#Practice #4 (Stripping Names):
#Purpose : Removing whitespaces characters

#I learnt there are three functions for stripping off whitespace rstrip(), lstrip() and, strip()

secondName = "  Guy    " #\n for new line
#line  = f"Only one person is left and his name is: {secondName}"
#print(line)#Output with whitespace characters

print(f"Without strip:  {secondName}")

print(f"With strip: {secondName.strip()}")#Removing whitespace characters on both sides

print(f"With rstrip: {secondName.rstrip()}")#Removing whitespace characters on the right

print(f"With lstrip: {secondName.lstrip()}")#Removing whitespace characters on the left



