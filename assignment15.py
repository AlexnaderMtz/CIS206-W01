"""
CIS206 W01 5/02/2024
Alexander Martinez Leyva
Assignment 15
"""


import tkinter as tk
from tkinter import messagebox


# Funct. to perform the calculation
def calculateResult():
   # get data from text-boxes
   textData = textEntry.get()
   numericData = numericEntry.get()


   # Validate numeric data
   if not numericData.isdigit() or textData.strip() == "":
       messagebox.showerror("Error", "Please enter a valid text and a numeric value.")
       return


   # Perform calculation
   result = int(numericData) * 2  # Example calculation


   # Display
   resultLabel.config(text=f"Result: {result}")


def clearFields():
   textEntry.delete(0, tk.END)
   numericEntry.delete(0, tk.END)
   resultLabel.config(text="")


# Create the main application window
app = tk.Tk()
app.title("Data Entry and Calculation")


# Design the form with text boxes, labels, and a button
tk.Label(app, text="Text Entry:").pack()
textEntry = tk.Entry(app)
textEntry.pack()


tk.Label(app, text="Numeric Entry:").pack()
numericEntry = tk.Entry(app)
numericEntry.pack()


calculateButton = tk.Button(app, text="Calculate", command=calculateResult)
calculateButton.pack()


clearButton = tk.Button(app, text="Clear", command=clearFields)
clearButton.pack()


resultLabel = tk.Label(app, text="")
resultLabel.pack()


# Run the application
app.mainloop()
