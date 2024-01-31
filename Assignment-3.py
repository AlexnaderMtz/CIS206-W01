"""
CIS206 W01 1/31/2024
Alexander Martinez Leyva
Assignment 3 - Functions!
"""

# 1- rewards problem
print()
print("problem 1\n")
def calculateRewards(points, redemptionCode):
    if redemptionCode == 'C':
        rewards = 2 * points
    elif redemptionCode == 'X':
        rewards = 3 * points
    else:
        rewards = 1.5 * points

    print(f"Points: {points}, Redemption Code: {redemptionCode}, Rewards Points: {rewards}")

# Example or user
calculateRewards(100, 'C')
calculateRewards(150, 'X')
calculateRewards(80, 'A')

"""
userPoints = float(input("Enter the number of points: "))
userCode = input("Enter the redemption code: ")
calculateRewards(userPoints, userCode)
"""

# 2- operation with error system
print()
print("problem 2\n")
def performOperation(num1, num2, operationCode):
    result = 0
    message = ""

    try:
        if operationCode == 'A':
            result = num1 + num2
        elif operationCode == 'S':
            result = num1 - num2
        elif operationCode == 'M':
            result = num1 * num2
        elif operationCode == 'D':
            if num2 != 0:
                result = num1 / num2
            else:
                result = -999
                message = "Syntax Error."

        print(f"Number 1: {num1}, Number 2: {num2}, Operation Code: {operationCode}, Result: {result}")
        if message:
            print(message)

    except Exception as e:
        print("Error occurred:", str(e))

# Example or user input
performOperation(10, 5, 'M')
performOperation(8, 0, 'D')

"""
userNum1 = float(input("Enter the first number: "))
userNum2 = float(input("Enter the second number: "))
userOperation = input("Enter the operation code (A, S, M, D): ")
performOperation(userNum1, userNum2, userOperation)
"""

# 3- Package calculation.
print()
print("problem 3\n")
def calculatePostage(weight, zipCode, weightCharge, areaCharge):
    weightCharge[0] = weight * weightCharge[0]
    if zipCode == 60171:
        areaCharge[0] = 2.00
    elif zipCode == 60172:
        areaCharge[0] = 2.50
    elif zipCode == 60635:
        areaCharge[0] = 3.00
    else:
        areaCharge[0] = 5.00

    postage = weightCharge[0] + areaCharge[0]
    print(f"Area Charge: ${areaCharge[0]:.2f}, Weight Charge: ${weightCharge[0]:.2f}, Postage: ${postage:.2f}")

# Example OR USER
weightCharge = [0.05]
areaCharge = [0]
calculatePostage(75, 60635, weightCharge, areaCharge)

"""
userWeight = float(input("Enter the weight of the package: "))
userZipCode = int(input("Enter the zip code: "))
weightCharge = [0.05]
areaCharge = [0]
calculatePostage(userWeight, userZipCode, weightCharge, areaCharge)
"""

# 4- Points to money calculation
print()
print("problem 4\n")
def calculateRewardsAndDollarValue(points, redemptionCode):
    if redemptionCode == 'C':
        rewards = 2 * points
    elif redemptionCode == 'X':
        rewards = 3 * points
    else:
        rewards = 1.5 * points

    dollarValue = rewards * 1.50
    print(f"Points: {points}, Redemption Code: {redemptionCode}, Rewards Points: {rewards}, Dollar Value: ${dollarValue:.2f}")

# Example OR USER
calculateRewardsAndDollarValue(100, 'C')
calculateRewardsAndDollarValue(150, 'X')
calculateRewardsAndDollarValue(80, 'A')

"""
userPoints = float(input("Enter the number of points: "))
userCode = input("Enter the redemption code: ")
calculateRewardsAndDollarValue(userPoints, userCode)
"""
