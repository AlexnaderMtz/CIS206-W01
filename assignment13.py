"""
CIS206 W01 4/14/2024
Alexander Martinez Leyva
Assignment 13
"""


class Employee:
   def __init__(self, firstName="N/A", lastName="N/A", jobLevel=1, annualSalary=0):
       self.firstName = firstName
       self.lastName = lastName
       self.jobLevel = jobLevel
       self.annualSalary = annualSalary
       self.shortTermBonus = self.calculateShortTermBonus()
       self.longTermBonus = self.calculateLongTermBonus()


   def calculateShortTermBonus(self):
       if self.jobLevel == 1:
           return 0.25 * self.annualSalary
       elif self.jobLevel == 2:
           return 0.20 * self.annualSalary
       elif self.jobLevel == 3:
           return 0.10 * self.annualSalary
       else:
           return 0


   def calculateLongTermBonus(self):
       return 0.10 * self.annualSalary


   def displayEmployeeInfo(self):
       print("First Name:", self.firstName)
       print("Last Name:", self.lastName)
       print("Job Level:", self.jobLevel)
       print("Annual Salary:", self.annualSalary)
       print("Short Term Bonus:", self.shortTermBonus)
       print("Long Term Bonus:", self.longTermBonus)


emp = Employee("ALEX", "LEY", 2, 60000)
emp.displayEmployeeInfo()
