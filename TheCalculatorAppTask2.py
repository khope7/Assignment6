#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

#Copying code from TheCalculatorAppTask1
#Asking the user what operation would they like to perform and catching user input for choice
print("Which operation would you like to perform? Please choose: addition, subtraction, multiplication, or division: ")
choice = input()

#Asking the user for number entries
print(f"Thank you! Your choice is \'{choice}\'. Please enter your first number to calculate: ")
a = entry1 = input()
print("Please your second number to calculate: ")
b = entry2 = input()

#Instantiating variables for arithmetic operation
a = float(entry1)
b = float(entry2)

#Writing code for each arithmetic operation
addition = (a + b)
subtraction = (a - b)
multiplication = (a * b)
division = (a / b)

#Creating if then statements to catch for user entry for lowercase choice of arithmetic operation, calculating and printing with 2 decimal limit
if choice.lower() == "addition":
    answer = addition
    print(f"Here is the {choice} of your two numbers:" , f"{answer:.2f}")
elif choice.lower() == "subtraction":
    answer = subtraction
    print(f"Here is the {choice} of your two numbers:" , f"{answer:.2f}")
elif choice.lower() == "multiplication":
    answer = multiplication
    print(f"Here is the {choice} of your two numbers:" , f"{answer:.2f}")
elif choice.lower() == "division":
    answer = division
    print(f"Here is the {choice} of your two numbers:" , f"{answer:.2f}")