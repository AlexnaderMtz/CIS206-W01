"""
CIS206 W01 2/22/2024
Alexander Martinez Leyva
Assignment 6 - Strings
"""

# 1- Cap Names

def capitalizeNames(firstName, lastName):
    capitalizedFirstName = firstName.capitalize()
    capitalizedLastName = lastName.capitalize()
    return capitalizedFirstName, capitalizedLastName

# Input
print("Cap Names")
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")

# Call - to capitalize names
capitalizedFirstName, capitalizedLastName = capitalizeNames(firstName, lastName)

# Display
print("Capitalized Name:", capitalizedFirstName, capitalizedLastName)
print()

# 2- Initials

def getInitials(fullName):
    initials = [name[0].upper() + '.' for name in fullName.split()]
    return ' '.join(initials)

# input
print("Initials")
fullName = input("Enter the full name: ")

# Call - to get initials
initials = getInitials(fullName)

# Display
print("Initials:", initials)
print()

# 3- Telephone Number

def translateTelephoneNumber(telephoneNumber):
    translatedNumber = ''
    for char in telephoneNumber:
        if char.isdigit():
            translatedNumber += char
        elif char.isalpha():
            if char.lower() in 'abc':
                translatedNumber += '2'
            elif char.lower() in 'def':
                translatedNumber += '3'
            elif char.lower() in 'ghi':
                translatedNumber += '4'
            elif char.lower() in 'jkl':
                translatedNumber += '5'
            elif char.lower() in 'mno':
                translatedNumber += '6'
            elif char.lower() in 'pqrs':
                translatedNumber += '7'
            elif char.lower() in 'tuv':
                translatedNumber += '8'
            elif char.lower() in 'wxyz':
                translatedNumber += '9'
    return translatedNumber

# INPUT
print("Telephone Number")
telephoneNumber = input("Enter telephone number: ")

# Call - to translate the telephone number
translatedNumber = translateTelephoneNumber(telephoneNumber)

# Display
print("Translated Number:", translatedNumber)
print()

# 4- Vowels and cons

def countVowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def countConsonants(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

# Input
print("Vowels and Consonants")
string = input("Enter a string: ")

# Call - to count vowels and consonants
vowelCount = countVowels(string)
consonantCount = countConsonants(string)

# Display
print("Number of vowels:", vowelCount)
print("Number of consonants:", consonantCount)
