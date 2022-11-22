import secrets
from collections import deque

# Creates four lists for special characters, number characters, upper case letter, and lower case letters. No backslash or space
specialCharacters = ["!", "\"", "#", "$", "%", "&", "\'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", 
                     "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]
numberCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lowercaseLetterCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", 
                             "v", "w", "x", "y", "z"]
uppercaseLetterCharacters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", 
                             "V", "W", "X", "Y", "Z"]

# Prompts user for the length of their desired password as well as the number of special characacters, number characters, and uppercase 
# letter characters that the user requires.
passwordLengthStr = input("Length Of Password (I recommend at least 16 digits): ")
numOfSpecialCharactersStr = input("# Of Special Characters Required: ")
numOfNumberCharactersStr = input("# Of Number Characters Required: ")
numOfUppercaseLetterCharactersStr = input("# Of Uppercase Letter Characters Required: ")

# Converts the required lengths into integer values.
passwordLength = int(passwordLengthStr)
numOfSpecialCharacters = int(numOfSpecialCharactersStr)
numOfNumberCharacters = int(numOfNumberCharactersStr)
numOfUppercaseLetterCharacters = int(numOfUppercaseLetterCharactersStr)
numOfLowercaseLetterCharacters = passwordLength - numOfSpecialCharacters - numOfNumberCharacters - numOfUppercaseLetterCharacters

# Creates an empty deque to represent the unsorted password.
unsortedValuesForPassword = deque()

# Adds values based on the requirements to the password list.
def addToList(count, list, charactersList):
    for i in range(count):
        randomNum = secrets.randbelow(len(charactersList))
        list.append(charactersList[randomNum])
    return list

# Adds all the characters to the deque, unsorted.
unsortedValuesForPassword = addToList(numOfSpecialCharacters, unsortedValuesForPassword, specialCharacters)
unsortedValuesForPassword = addToList(numOfNumberCharacters, unsortedValuesForPassword, numberCharacters)
unsortedValuesForPassword = addToList(numOfUppercaseLetterCharacters, unsortedValuesForPassword, uppercaseLetterCharacters)
unsortedValuesForPassword = addToList(numOfLowercaseLetterCharacters, unsortedValuesForPassword, lowercaseLetterCharacters)
print(unsortedValuesForPassword)

# Mixes the values up and concatenates each character to the password String.
password = ""
for i in range(passwordLength):
    randomNum = secrets.randbelow(len(unsortedValuesForPassword))
    for j in range(randomNum):
        temp = unsortedValuesForPassword.popleft()
        unsortedValuesForPassword.append(temp)
    value = unsortedValuesForPassword.popleft()
    password += value

# Prints out mixed up password.
print(password)
