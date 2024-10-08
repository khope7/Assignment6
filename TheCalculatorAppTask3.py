#Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

#Copying code from TheCalculatorAppTask2

#Used while loop to repeat the question after incorrect entries

#Asking the user what operation would they like to perform and catching for any answer other than mentioned operations
while True:
    print("Which operation would you like to perform? Please choose: addition, subtraction, multiplication, or division: ")
    choice = input()

    if choice.lower() != "addition" and choice.lower() != "subtraction" and choice.lower() != "multiplication" and choice.lower() != "division":
        print("Unable to proceed, choice must be one of the mentioned operations. Please try again.")
    else:
        break

#Printing choice
print(f"Thank you! Your choice is \'{choice}\'.")
      
#Asking user for variable entries and catching for all other entries https://stackoverflow.com/questions/8075877/converting-string-to-int-using-try-except-in-python for reference
while True:
    try:
        print("Please enter your first number to calculate: ")
        a = entry1 = float(input())
        break
    except ValueError:
        print("Unable to proceed, your first choice must be a number. Please try again.")

while True:
    try:
        print("Please enter your second number to calculate: ")
        b = entry2 = float(input())

#Including catch statement for user entry 0 for b
        if b == 0.0 and b == 0:
            print("Cannot divide by zero, yet. (perhaps if the world could agree on a variable specific to this equation then the answer would have a value... and break everything of course!)")
        else:
            break
    except ValueError:
        print("Unable to proceed, your second choice must be a number. Please try again.")


#Writing code for each arithmetic operation
addition = (a + b)
subtraction = (a - b)
multiplication = (a * b)
division = (a / b)

#Creating if then statements to catch for user entry for lowercase choice of arithmetic operation, calculating and printing with 2 decimal limit
if choice.lower() == "addition":
    answer = addition
    print(f"Here is the {choice.lower()} of your two numbers:" , f"{answer:.2f}")
elif choice.lower() == "subtraction":
    answer = subtraction
    print(f"Here is the {choice.lower()} of your two numbers:" , f"{answer:.2f}")
elif choice.lower() == "multiplication":
    answer = multiplication
    print(f"Here is the {choice.lower()} of your two numbers:" , f"{answer:.2f}")
elif choice.lower() == "division":
    answer = division
    print(f"Here is the {choice.lower()} of your two numbers:" , f"{answer:.2f}")