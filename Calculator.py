try:
    A=float(input("enter first no.:"))
    B=input("operator:")
    C=float(input("enter second no.:"))
    if B == "+":
        cal=A + C
        print(cal)
    elif B== "-":
        cal=A-C
        print(cal)
    elif B== "*":
        cal=A*C
        print(cal)
    elif B == "/":
        if C !=0:
            cal=A/C
            print(cal)
        else:
            print("Error")
    else:
        print("invalid , Enter any one from + - * /")
except ValueError:
    print("Please enter a valid number")
  