"""
CIS206 W01 2/27/2024
Alexander Martinez Leyva
Assignment 7 - Files
"""

import csv

def computeGrossPay(hours, rate):
    # Regular pay
    if hours <= 40:
        regularPay = hours * rate
        overtimePay = 0
    # Overtime pay
    else:
        regularPay = 40 * rate
        overtimePay = (hours - 40) * (rate * 1.5)
    return regularPay + overtimePay

def formatEmail(first_name, last_name):
    return f"{first_name[0].lower()}{last_name.lower()}@gm.com"

def processEmployeeData(inputFile, outputFile):
    try:
        with open(inputFile, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            with open(outputFile, 'w', newline='') as output:
                fieldnames = ['Last_Name', 'First_Name', 'Gross_Pay', 'Email']
                writer = csv.DictWriter(output, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    hours = float(row['Hours'])
                    rate = float(row['Rate'])
                    gross_pay = computeGrossPay(hours, rate)
                    email = formatEmail(row['First_Name'], row['Last_Name'])
                    writer.writerow({'Last_Name': row['Last_Name'], 'First_Name': row['First_Name'], 'Gross_Pay': f"{gross_pay:.2f}", 'Email': email})
        print("Output file created successfully!")
    except FileNotFoundError:
        print("Input file not found. Please make sure the file exists.")
    except ValueError:
        print("Invalid data in input file. Please check the format of the data.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    inputFile = "C:/Users/amley/Downloads/EmpData.csv"
    outputFile = "output.csv"
    processEmployeeData(inputFile, outputFile)
