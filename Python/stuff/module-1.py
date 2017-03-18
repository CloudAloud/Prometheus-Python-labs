__author__ = 'minin'

import sys

userInput = sys.argv[1]
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
keyArray = []
codeArray = []
alphabetArray = []
messageArray = []

for n in range(len(key)):
    keyArray.append(key[n])

for n in range(len(alphabet)):
    alphabetArray.append(alphabet[n])

for n in range(len(alphabet)):
    codeArray.append(keyArray[n:n+5])

for letter in userInput:
    if alphabet.count(letter) == 1:
         messageArray.append("a")
    elif alphabet.upper().count(letter) == 1:
        messageArray.append("b")

messageArray = messageArray[:len(messageArray)-len(messageArray)%5]

word = ""
for position in range(len(messageArray)/5):
    word = word + alphabet[codeArray.index(messageArray[position*5:position*5+5])]
print word

