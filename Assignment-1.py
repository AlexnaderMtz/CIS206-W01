"""
CIS206 W01 1/18/2024
Alexander Martinez Leyva
Assignment 1
"""

# Problem 1: Entering the first name and last name, then displaying them in the order of last name, first name;

print("Problem 1")
print()
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
print("Answer:")
print(lastName + ", " + firstName)
print()

# Problem 2: Computing and displaying the product of 10 times 100 times 1000 times 10000;

print("Problem 2")
print()
result = 10 * 100 * 1000 * 10000
print("Result:")
print(result)
print()

# Problem 3: Creating a program that shows the numerical values of the Boolean true and false;

print("Problem 3\n")
print("Numerical value of True:", int(True))
print("Numerical value of False:", int(False))
print()

# Problem 4: Allowing a user to enter two floating-point numerical values and displaying their product;

print("Problem 4\n")
num1 = float(input("Enter the first floating-point number: "))
num2 = float(input("Enter the second floating-point number: "))
product = num1 * num2
print("The Product of the two numbers:", product)
print()

# Problem 5: Using the type function to display the data types of a string, float, and integer;

print("Problem 5\n")
dataTypes = {
    "String": type("example"),
    "Float": type(3.14),
    "Integer": type(42)
}

for data_type, value in dataTypes.items():
    print(f"{data_type}: {value}")
