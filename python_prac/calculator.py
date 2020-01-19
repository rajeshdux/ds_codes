'''calculator 1)add,2)sub,3)mul,4)div'''

def calculator():

    while (True):
        i=input("select 1) Add\n 2)Subtract\n 3)Multiply\n 4)Division\n Choice:  ")
        s="1234"
        if i not in s:
            print("********select one of the choice**************")
        if i in s:
            break


    b = int(input("operand1: "))
    c = int(input("operand2: "))

    if i == "1":
        print(b, "+", c, "=", b + c)
    elif i == "2":
        print(b, "-", c, "=", b - c)
    elif i == "3":
        print(b, "*", c, "=", b * c)
    elif i == "4":
        print(b, "/", c, "=", b / c)



while(1):
    calculator()
    z=input("More Calculations ? [y/n]: ")
    if z=="y":
        continue
    if z=="n":
        break


