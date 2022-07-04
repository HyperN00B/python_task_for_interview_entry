import os
import platform
import time

def ClearScreen():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")
    pass
pass

def menu():
    ClearScreen()
    ScriptToRun=input("Which script would you like to use/review?\n1: Count Vowels\n2: Calculator\nYour choice: ")
    if ScriptToRun=="1":
        os.system("python Count_Vowels.py")
    elif ScriptToRun=="2":
        os.system("python Calculator.py")
    else:
        ClearScreen()
        print("The script you chose doesn't exist!")
        print("Returning to the main screen...")
        time.sleep(2)
        menu()
    pass
pass

menu()