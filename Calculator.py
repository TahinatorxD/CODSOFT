print('\n')
print("     ***  This is a Non Scintefic Calculator  ***    ")

First_Number = input("Enter The First Number:  ")
Second_Number = input("Enter The Second Number:  ")
Operator_chosed = input("Enter the Arthimethic Operation to execute (+ , - , * , / ): ")

def Addition(First_Number, Second_Number):
    print("Answer = ",int(First_Number) + int(Second_Number))

def Subtraction(First_Number, Second_Number):
    print("Answer = ",int(First_Number) - int(Second_Number))

def Multiplication(First_Number, Second_Number):
    print("Answer = ",int(First_Number) * int(Second_Number))

def Division(First_Number, Second_Number):
    print("Answer = ",int(First_Number) / int(Second_Number))


if Operator_chosed == "+":
    Addition(First_Number, Second_Number)

if Operator_chosed == "-":
    Subtraction(First_Number, Second_Number)

if Operator_chosed == "*":
    Multiplication(First_Number, Second_Number)

if Operator_chosed == "/":
    Division(First_Number, Second_Number)
