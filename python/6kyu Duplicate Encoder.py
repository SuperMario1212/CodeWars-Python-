# --> Instructions <--

# The goal of this exercise is to convert a string to a new string 
# where each character in the new string is "(" if that character appears only once in the original string, 
# or ")" if that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a duplicate.

# Examples:
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

# <My solution>

def duplicate_encode(word):
    encoded = ""                # create a new empty string to store the encoded word
    for letter in word.lower(): # Since case insensitive, just use lower case for all
        encoded += replace(letter, word.lower())
    return encoded

def replace(letter, word):
    if word.count(letter) > 1:  # If the letter appear in the word is more than 1 
        return ")"              # add ")" into the encoded string, else add "("
    return "("
        
