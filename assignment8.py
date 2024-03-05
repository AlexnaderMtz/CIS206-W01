"""
CIS206 W01 3/5/2024
Alexander Martinez Leyva
Assignment 8
"""

# 1-Rainfall Statistics

print("1-Rainfall Statistics")
print()
def rainfallStatistics():
    # Store rainfall for each month
    rainfall = []
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Input
    for month in months:
        rainfall.append(float(input(f"Enter the rainfall (inches) for {month}: ")))

    # Calculate
    totalRainFall = sum(rainfall)
    averageRainFall = totalRainFall / len(rainfall)

    # highest and lowest
    maxRainfallMonth = months[rainfall.index(max(rainfall))]
    minRainfallMonth = months[rainfall.index(min(rainfall))]

    # Display
    print(f"Total rainfall for the year: {totalRainFall} inches")
    print(f"Average monthly rainfall: {averageRainFall} inches")
    print(f"Highest rainfall Month: {maxRainfallMonth}")
    print(f"Lowest rainfall Month: {minRainfallMonth}")

rainfallStatistics()
print()

# 2-Number Analysis Program:

print("2-Number Analysis Program")
print()
def numberAnalysis():
    # Input of 20 numbers for a list
    numbers = [float(input(f"Enter number {i+1}: ")) for i in range(20)]

    # Calculate
    lowestNumber = min(numbers)
    highestNumber = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    # Display
    print(f"Lowest number: {lowestNumber}")
    print(f"Highest number: {highestNumber}")
    print(f"Total of the numbers: {total}")
    print(f"Average of the numbers: {average}")

numberAnalysis()
print()

# 3-Tuples:
print("3-Tuples")
print()
# Represent coordinates (x, y)
point = (3, 5) # tuple for representing a point
# Accessing a tuple
xCoordinate = point[0] # acces for the first element
yCoordinate = point[1] # acces for the first element
print()

# 4-Sets:
print("4-Sets")
print()
# Predefined sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Set containing elements from set1 and set2
set3 = set1.intersection(set2)
print(set3)
print()

# 5-Dictionaries:

import random

print("5-Dictionaries")
print()
def capitalQuiz():
    # Dictionary containing states and capitals
    statesCapitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Massachusetts': 'Boston',
        'Ohio': 'Columbus',
        'Indiana': 'Indianapolis',
        'Oregon': 'Salem',

    }

    correctAnswers = 0
    incorrectAnswers = 0

    # Shuffle
    statesList = list(statesCapitals.keys())
    random.shuffle(statesList)

    # Quiz
    for state in statesList:
        capital = input(f"What is the capital of {state}? ")
        if capital.lower() == statesCapitals[state].lower():
            print("Correct!")
            correctAnswers += 1
        else:
            print(f"Incorrect. The capital of {state} is {statesCapitals[state]}.")
            incorrectAnswers += 1

    # Display
    print(f"\nQuiz Results:")
    print(f"Correct answers: {correctAnswers}")
    print(f"Incorrect answers: {incorrectAnswers}")

capitalQuiz()
print()

