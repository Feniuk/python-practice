def calculator():
    print("Calculator running")

    try:
        x = float(input("Enter an X value: "))
        y = float(input("Enter a Y value: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    
    option = input("Choose a mathimetical operation, A for Addition S for Subract M for Multiplication: ") 

    if option == 'A':
        add = x + y
        print("Result: ",add)
    elif option == 'S':
        subtract = x - y
        print("Result: ",subtract)
    elif option == 'M':
        multiply = x * y
        print("Result: ",multiply)
    else:
        print("Invalid operation!")

    print("End of calculation.")

module_name = "Simple calculator"

if __name__ == "__main__":
    print("Calculator is being run directly")
    calculator()
else:
    print("Calculator module has been imported")
