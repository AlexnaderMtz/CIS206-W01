"""
CIS206 W01 1/24/2024
Alexander Martinez Leyva
Assignment 2 - If Statements
"""

# Problem 1 - Right Triangle
print("Enter lengths for the sides of the right triangle")
x = float(input("Enter the length of side X: "))
y = float(input("Enter the length of side Y: "))
z = float(input("Enter the length of side Z: "))

# Check if it's a right triangle by using the Pythagorean theorem (c^2 = a^2 + b^2)
if x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")

# Problem 2 - Mimics Calculator
print()
print("Simple fake calculator!\n")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
operator = input("Enter the operation symbol (+, -, *, /): ")

# math operations and handle division by zero
result = 0
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero.")
        exit()

print()
print(f"{num1} {operator} {num2} = {result}")
print()

# Problem 3 - Estimated Earnings based on options for a novel
print("Novel deals")
netPrice = float(input("Enter the net price of each copy of the novel: "))
estimatedCopies = int(input("Enter the estimated number of copies to be sold: "))
print()

fixedRoyalty1 = 20000
royaltyRate2 = 0.125
royaltyRate3_1 = 0.10
royaltyRate3_2 = 0.14
copiesThreshold = 4000

royalties_option1 = fixedRoyalty1
royalties_option2 = estimatedCopies * netPrice * royaltyRate2
royalties_option3 = min(estimatedCopies, copiesThreshold) * netPrice * royaltyRate3_1 + max(0, estimatedCopies - copiesThreshold) * netPrice * royaltyRate3_2

best_option = max(royalties_option1, royalties_option2, royalties_option3)

print(f"Royalties under option 1: ${royalties_option1:.2f}")
print(f"Royalties under option 2: ${royalties_option2:.2f}")
print(f"Royalties under option 3: ${royalties_option3:.2f}")
print()

if best_option == royalties_option1:
    print("Option 1 is the best choice!!!")
elif best_option == royalties_option2:
    print("Option 2 is the best choice!!!")
else:
    print("Option 3 is the best choice!!!")

# Problem 4 - Leap year teller
print()
print("Leap year finder")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year!!!")
else:
    print(f"{year} is not a leap year.")
