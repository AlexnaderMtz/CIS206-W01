"""
CIS206 W01 4/25/2024
Alexander Martinez Leyva
Assignment 14
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
           return self.annualSalary * 0.25
       elif self.jobLevel == 2:
           return self.annualSalary * 0.20
       elif self.jobLevel == 3:
           return self.annualSalary * 0.10


   def calculateLongTermBonus(self):
       return self.annualSalary * 0.10


   def displayEmployeeData(self):
       print("Employee Data:")
       print("First Name:", self.firstName)
       print("Last Name:", self.lastName)
       print("Job Level:", self.jobLevel)
       print("Annual Salary:", self.annualSalary)
       print("Short Term Bonus:", self.shortTermBonus)
       print("Long Term Bonus:", self.longTermBonus)




class Manager(Employee):
   def __init__(self, firstName="N/A", lastName="N/A", jobLevel=1, annualSalary=0, auto="N/A"):
       super().__init__(firstName, lastName, jobLevel, annualSalary)
       self.auto = auto


   def displayManagerData(self):
       super().displayEmployeeData()
       print("Automobile:", self.auto)


   def calculateLongTermBonus(self):
       if self.jobLevel == 1:
           return self.annualSalary * 0.50
       elif self.jobLevel == 2:
           return self.annualSalary * 0.40
       elif self.jobLevel == 3:
           return self.annualSalary * 0.35




# Instantiate Manager object
manager = Manager("Javi", "Dool", 2, 80000, "BMW")


# Display Manager data
manager.displayManagerData()
