"""
CIS206 W01 2/07/2024
Alexander Martinez Leyva
Assignment 4 - Loooooops!
"""

# 1- Accepting an Integer and Displaying
print()
print("problem 1\n")

while True:
    try:
        num = int(input("Enter integer (10 to 20): "))
        if 10 <= num <= 20:
            break
        else:
            print("Input is invalid. Please enter an integer between 10 and 20.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

for i in range(num + 1):
    print(i)

# 2- Loop with 3 Chance
print()
print("problem 2\n")

attempts = 0
while attempts < 3:
    try:
        num = int(input("Enter a # between 10 and 20: "))
        if 10 <= num <= 20:
            break
        else:
            print("Input not accepted. Please enter between 10 and 20.")
            attempts += 1
    except ValueError:
        print("Invalid input. Please enter an integer.")
        attempts += 1

if attempts == 3:
    print("You have reached the max number of tries.")
else:
    for i in range(num + 1):
        print(i)

# 3- Repeatedly Check if
print()
print("problem 3\n")

favorite_names = ["Jensen", "Alex", "Emma", "Javier", "Dali", "kat", "Beth", "Leslie", "Erika", "Teo"]

while True:
    name = input("Enter a name: ")
    if name in favorite_names:
        print(f"{name} is in the list!!!")
        break
    else:
        print(f"{name} is not in the list. Please try again.")

# 4- Display List Using Two Different loops
print()
print("problem 4\n")

# Using a for loop
print("Using a ''for loop'':")
for name in favorite_names:
    print(name)

# Using a while loop
print("\nUsing a ''while loop'':")
i = 0
while i < len(favorite_names):
    print(favorite_names[i])
    i += 1

# 5- Program for Exam Scores
print()
print("problem 5\n")

while True:
    choice = input("Do you want to do the program? (Yes/No): ").lower()
    if choice in ['yes', 'y']:
        try:
            score1 = float(input("Enter the first exam score (0-100): "))
            score2 = float(input("Enter the second exam score (0-100): "))
            if 0 <= score1 <= 100 and 0 <= score2 <= 100:
                total_points = 0.6 * score1 + 0.4 * score2
                print(f"Total points: {total_points}")
            else:
                print("Scores must be within the range of 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    elif choice in ['no', 'n']:
        print("Program ended.")
        break
    else:
        print("Invalid input. Please enter Yes or No.")
