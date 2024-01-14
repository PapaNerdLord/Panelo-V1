import tkinter as tk
from tkinter.tix import WINDOW
# Wanting to build a menu screen but have a screen that appears before the menu to get basic info
# such as Name, DoB, Usage Type, all basic and none essential. Then use the Name they entered as 
# as a way to personalize it, other later usages. 

root = tk.Tk()
root.title("PaNeLo BudgetFinance Program: Welcome name*") # * I want to have the user name implemented here through the prior window listing a set of needed and optional inputs to personalize it
root.geometry("600x600")  # For now Set it to what ever works for you want to add a way to make it native/scaling and changable. 

label = tk.Label(root, text="Hello, (Name) select a Menu that you want to work on!") # Theres gonna be different options to go into and work on specific things... Lets say you got a paycheck and just need to enter the amount of earning income
                                                                                     #  you can select Got Paid! and itll prompt its own window of things thats are skippable optional like hours and taxes, and some needed for completion like a amount earned.
label.pack()

root.mainloop()