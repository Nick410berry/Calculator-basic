def question():
    try:
        Number1 = float(input('Type a number:'))
        Number2 = float(input('Type a second number:'))
    except ValueError:
        print("Error, please type a number")
        return question()
    
    operator = input("Select an operator: + / x - :")
    if operator == "+":
        Sum = Number1 + Number2
        print("Your Result is:")
        print(Sum)
    elif operator == "/":
        if Number2 != 0:
            Div = Number1 / Number2
            print("Your Result is:")
            print(Div)
        else:
            print("Error, cannot divide by zero")
            return question()
    elif operator == "x":
        Mult = Number1 * Number2
        print("Your Result is:")
        print(Mult)
    elif operator == "-":
        Dif = Number1 - Number2
        print("Your Result is:")
        print(Dif)
    else:
        print("Error, please select a valid operator")
        return question()

question()