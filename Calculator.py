import os
import time
import platform

def ClearScreen():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")
    pass
pass

def menu():
    ClearScreen()
    InputAction=input("Select the operation you want to do! The possible operations are:\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n5: Percentage\nYour Choice: ")
    if InputAction=="1":
        data_input(InputAction)
    elif InputAction=="2":
        data_input(InputAction)
    elif InputAction=="3":
        data_input(InputAction)
    elif InputAction=="4":
        data_input(InputAction)
    elif InputAction=="5":
        data_input(InputAction)
    else:
        invalid_operation()
    pass
pass

def invalid_operation():
    print("The selected operation doesn't exist!\nThe valid operations are:\n1:Addition\n2:Subtraction\n3:Multiplication\n4:Division\n5:Percentage\nReturning to the menu...")
    time.sleep(3)
    menu()
pass

def data_input(operation):
    ClearScreen()
    a=input("Enter the first number: ")
    b=input("Enter the second number: ")
    if not a or not b:
        print("The values cannot be empty!")
        time.sleep(3)
        data_input(operation)
    elif a.isalpha() or b.isalpha():
        print("Letters are not allowed!")
        time.sleep(3)
        data_input(operation)
    elif not a.isalnum() or not b.isalnum():
        print("Special characters are not allowed!")
        time.sleep(3)
        data_input(operation)
    elif operation=="1":
        print("The sum of "+str(a)+" and "+str(b)+" is "+Calculator.add(a,b))
        wait=input("Press Enter to return to the menu\n")
        menu()
    elif operation=="2":
        print("The subtraction of "+str(a)+" and "+str(b)+" is "+Calculator.subtract(a,b))
        wait=input("Press Enter to return to the menu\n")
        menu()
    elif operation=="3":
        print("The multiplication of "+str(a)+" and "+str(b)+" is "+Calculator.multiple(a,b))
        wait=input("Press Enter to return to the menu\n")
        menu()
    elif operation=="4":
        print("The division of "+str(a)+" and "+str(b)+" is "+Calculator.divide(a,b))
        wait=input("Press Enter to return to the menu\n")
        menu()
    elif b=="0":
        print("Sorry, but this program isn't advanced enough to divide with 0 ;-(")
        wait=input("Press Enter to return to the menu\n")
    elif operation=="5":
        print(str(a)+" is the "+Calculator.percentage(a,b)+"% of "+str(b))
        wait=input("Press Enter to return to the menu\n")
        menu()
    else:
        print("The passed operation somehow turned out to be invalid!")
        wait=input("Press Enter to return to the menu\n")
        menu()
    pass
pass

class Calculator:
    def add(a,b):
        c=float(a)+float(b)
        return str(c)
    pass

    def subtract(a,b):
        c=float(a)-float(b)
        return str(c)
    pass

    def multiple(a,b):
        c=float(a)*float(b)
        return str(c)
    pass

    def divide(a,b):
        c=float(a)/float(b)
        return str(c)
    pass

    def percentage(a,b):
        c=(float(b)/100)
        d=float(a)/float(c)
        return str(d)
    pass
pass

menu()
