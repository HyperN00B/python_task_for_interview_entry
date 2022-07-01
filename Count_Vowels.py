import os
import platform
import time

# Vowels to search for in the input word/file
Vowels=["a","e","i","o","u"]

# Vowel counter set to zero as a failsafe
VowelsInInput=0

# Message for empty input
Empty="I see what you did there! But empty input is not allowed!"

def ClearScreen():
    # Check the HostOS type to decide which command to use for clearing the Command Prompt/Terminal
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")
    pass
pass

def ask_for_word_or_sentence():
    ClearScreen()
    InputParameter=input("Please enter the word you want to count the vowels in!\nYou can also type 'back' to go back to the main screen\nWord/Sentence: ")
    if not InputParameter:
        ClearScreen()
        print(Empty)
        time.sleep(3)
        ask_for_word_or_sentence()
    elif InputParameter.lower()=="back":
        FeatureSelection()
    else:
        print("There are "+count_vowels(InputParameter.lower())+" vowels found in the word or sentence:\n"+InputParameter)
pass

def ask_for_file():
    ClearScreen()
    InputParameter=input("Please enter the file you want to count the vowels in!\nYou can also type 'back' to go back to the main screen\nFile: ")
    if not InputParameter:
        ClearScreen()
        print(Empty)
        time.sleep(3)
        ask_for_file()
    elif InputParameter.lower()=="back":
        FeatureSelection()
    elif not os.path.isfile(InputParameter):
        ClearScreen()
        print("The input is either not a file, or it doesn't exist!")
        time.sleep(3)
        ask_for_file()
    else:
        OpenFile=open(InputParameter,"r")
        ReadFile=OpenFile.read()
        print("There are "+count_vowels(ReadFile.lower())+" vowels found in the input file:\n"+InputParameter)

def count_vowels(InputParameter):
# Function definition with word
    global VowelsInInput
    LettersInInput=list(InputParameter)
    # Make "number of vowels found" a global var so the return statement can actually see it's defined outside of the method.
    for i in LettersInInput:
    # Do it for every letter in the word
        for j in Vowels:
        # Do it for every letter in Vowels list
            if i==j:
            # If i-th item in input=j-th item in Vowels list:
                VowelsInInput=VowelsInInput+1
                # Increase vowel counter by 1
            pass
        pass
    pass
    return str(VowelsInInput)
    # Return the number of vowels found to the main method
pass

# Main screen for selecting work method
def FeatureSelection():
    ClearScreen()
    global LettersInInput

    Choice=input("Do you want to use a word/sentence or a file?\n1: Word/Sentence\n2: File\nYour selection: ")

    # The user chose word/sentence
    if Choice=="1":
        ask_for_word_or_sentence()

    #The user chose file
    elif Choice=="2":
        ask_for_file()

    # Invalid selection, return to Main screen
    else:
        ClearScreen()
        print("Invalid option!")
        print("The available options are:")
        print("1: Word/Sentence")
        print("2: File")
        time.sleep(3)
        FeatureSelection()
    pass
pass

FeatureSelection()
