import secrets

# Creates three lists for special characters, number characters, and lower case letters.
specialCharacters = ["!", "\"", "#", "$", "%", "&", "\'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", 
                     "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
numberCharactera = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letterCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", 
                    "x", "y", "z"]

# Prompts user for the length of their desired password as well as the number of special characacters, number characters, and uppercase 
# letter characters that the user requires.
passwordLengthStr = input("Length Of Password (I recommend at least 16 digits): ")
numOfSpecialCharactersStr = input("# Of Special Characters Required: ")
numOfNumberCharactersStr = input("# Of Number Characters Required: ")
numOfUppercaseLetterCharactersStr = input("# Of Uppercase Letter Characters Required: ")

# Converts the required lengths into integer values.
passwordLength = int(passwordLengthStr)
numOfSpecialCharacters = int(passwordLengthStr)
numOfNumberCharacters = int(numOfNumberCharactersStr)
numOfUppercaseLetterCharacters = int(numOfUppercaseLetterCharactersStr)

# Creates two empty lists to represent the password and each type of the digits.
password = []
indexOfType = []

# Creates a for loop to insert placeholder values in indexOfType before modifiyng them to the type of requirement
for i in range(passwordLength):
    indexOfType.append("X")
    
# Assigns each "X" in indexOfType with a type of character.
while i < passwordLength:
    randomNum1 = secrets.randbelow(passwordLength)
    randomNum2 = secrets.randbelow(3)
    
    if randomNum2 == 0:
        randomNum3 = secrets.randbelow(len(specialCharacters))
        indexOfType.remove()


# Creates a while loop that iterates as long as the length of the length of the desired password from the user.
j = 0
while j < passwordLength:
    j = j + 1