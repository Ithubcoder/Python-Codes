# Simple Calculator

while True:
    
    print('''..........OPERATIONS..........
    Type 1 for Addition.
    Type 2 for Subtraction.
    Type 3 for Multiplication.
    Type 4 for Division.
    Type 5 for Modulous.
    Type 6 for Floor Division.
    Type 7 for Square of a Number.
    Type 8 for Cube of a Number.
    Type 9 for Exit.''')

    val = int(input("Enter a value to perform operation : "))

    if val == 9:
        break

    if val == 7:
        a = int(input("Enter a Number : "))
        sq = a * a
        print("Square of the Number is : ", sq)

    if val == 8:
        b = int(input("Enter a Number : "))
        cub = b * b * b
        print("Cube of the Number is : ", cub)

    if val == 1:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        ad = num1 + num2
        print("Addition of the numbers is : ", ad)

    if val == 2:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        sub = num1 - num2
        print("Subtraction of the numbers is : ", sub)

    if val == 3:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        mul = num1 * num2
        print("Multiplication of the numbers is : ", mul)

    if val == 4:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        div = num1 / num2
        print("Division of the numbers is : ", div)

    if val == 5:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        mod = num1 % num2
        print("Modulous of the numbers is : ", mod)

    if val == 6:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        fd = num1 // num2
        print("Floor Division of the numbers is : ", fd)
