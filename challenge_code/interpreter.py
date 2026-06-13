'''
    While Loop
        INPUT 
        # Prompt the user to enter the expression until valid

        PROCESS
        # Validate the following:
        # Spaces between X, Y, and Z
        #     Split the input into three parts (X, Y, and Z) using spaces
        #         If len(list) != 3, print format error

        # X and Z must be integers
        #     Use a try block that converts X and Z to int values
        #         If either conversion causes an exception, print integer error
        
        # Y must be in {+,-,*,/}
        #     Make a set of operators to determine if Y is a valid operator
        #         If Y is not a valid operator, print operator error
        
        # Cannot divide by zero
        #     Use an IF statement to check if Y == "/" and Z == 0
        #         If True, print divide by zero error

    # OUTPUT
    # Print the output to the user rounded to 1 decimal place
    '''

def get_expression():
    while True:
        expression = input("Expression: ")
        data = expression.split(" ")
        valid_operators = {"+", "-", "*", "/"}
        
        if len(data) != 3:
            print("ERROR: Incorrect format")
            continue

        try:
            x = int(data[0])
            z = int(data[2])
        except:
            print("ERROR: X and Z must be integers")
            continue

        y = data[1]
        if y not in valid_operators:
            print("ERROR: Y must be a valid operator (+, -, *, /)")
            continue

        if y == "/" and z == 0:
            print("ERROR: Cannot divide by 0")
            continue

        data = [x, y, z]
        return data

def main():
    while True:
        expression = get_expression()
        if expression[1] == "+":
            result = float(expression[0] + expression[2])
        elif expression[1] == "-":
            result = float(expression[0] - expression[2])
        elif expression[1] == "*":
            result = float(expression[0] * expression[2])
        else:
            result = float(expression[0] / expression[2])

        print(f"{result:.1f}")

        if input("Would you like to enter a new expression (enter 'y' to continue): ") != "y":
            break

main()