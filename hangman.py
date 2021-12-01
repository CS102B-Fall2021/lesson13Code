# Hangman Game
#
# The classic game of Hangman.  The computer picks a random word
# and the player wrong to guess it, one letter at a time.  If the player
# can't guess the word in time, the little stick figure gets hanged.

# imports
import random

# constants
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

WORDS = ("HAPPY THANKSGIVING", "MERRY CHRISTMAS")

# initialize variables
word = random.choice(WORDS)   # the word to be guessed
so_far = "-" * len(word)      # one dash for each letter in word to be guessed

print(WORDS)
print(word)
print(so_far)
new = ""
for i in range(len(word)):
    if word[i] == " ":
        new += " " 
    else: 
        new += so_far[i]
so_far = new

wrong = 0                     # number of wrong guesses player has made
used = []                     # letters already guessed


print(word)
print(so_far)

while so_far != word and wrong < MAX_WRONG:
    letter = input("Choose a letter: ")
    letter = letter.upper()
    print(letter)
    """
    print(letter in word)
    print(type(letter))
    print(type(word))
    print(type(so_far))
    """
    new = ""
    if letter in word:
        print("HERE: " + letter)
        for i in range(len(word)):
            print("i = ", i)
            if word[i] == " ":
                new += " "
            elif word[i] == letter:
                new += letter
            else: 
                if so_far[i] != "-":
                    new += so_far[i]
                else: 
                    new += "-"
        so_far = new
    else: 
        wrong += 1
        print(HANGMAN[wrong])
    print(so_far)
