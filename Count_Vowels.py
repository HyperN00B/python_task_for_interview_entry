Vowels=["a","e","i","o","u"]
# Vowels to search for in the input word/file
VowelsInInput=0
# Vowel counter set to zero as a failsafe
InputWord=input("Please enter the word you want to count the vowels in: ")
# Ask for the input word
LettersInInput=list(InputWord)
# Load the input word into a list of individual characters

def count_vowels(InputWord):
# Function definition with word
    global VowelsInInput
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

VowelsFound=count_vowels(InputWord)
# Call the method to do the actual counting
print("")
# A newline to make the output a little more spaced
print("The number of vowels in the given word is: "+VowelsFound)
# The result of the method