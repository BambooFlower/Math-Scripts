# This is a python implementation of the Solitaire Cipher, a key-generator encryption/decryption Algorithm based on a deck of french cards developed by Bruce Schneier 
# Reference can be found at: https://www.schneier.com/academic/solitaire/

# This algorithm uses the bridge order of suits: clubs, diamonds, hearts and spades
# If the card is a club, it is the value shown
# If the card is a diamond, it is the value plus 13
# If it is a heart, it is the value plus 26
# If it is a spade, it is the value plus 39
# Either joker is a 53
# Therefore clubs are numbers from 1 to 13, diamonds are cards from 14 to 26, hearts are cards from 27 to 39 and spades are cards from 40 to 52

import random
from random import shuffle

def keystream():
    # This function generates the keystream for the encryption/decryption


    # GENERATING THE KEY
    Deck = list(range(1, 53))
    # 'A' & 'B' represent the two different jockers
    Deck.extend(['A','B'])
    shuffle(Deck)
 	# a & b are the position of the two jockers

    # Changing the position of the first jocker A
    a = Deck.index('A')

    if a != 53:
        Deck[a] = Deck[a+1]
        Deck[a+1] = 'A'
    else:
        Deck[53] = Deck[0]
        Deck[0] = 'A'

    # Changing the position of the second jocker B
    b = Deck.index('B')

    if b != 53 and b != 52:
        Deck[b] = Deck[b+1]
        Deck[b+1] = Deck[b+2]
        Deck[b+2] = 'B'
    elif b == 52:
        Deck[52] = Deck[53]
        Deck[53] = Deck[0]
        Deck[0] = 'B'
    else:
        Deck[53] = Deck[0]
        Deck[0] = Deck[1]
        Deck[1] = 'B'

    # Checking the new position of the two jockers
    a = Deck.index('A')
    b = Deck.index('B')

    # Checking which jocker appears first 
    if a < b:
        First = a
        Second = b
    else:
        First = b
        Second = a

    # Performing the triple cut
    Section1 = Deck[:First]
    Center = Deck[First:Second+1]
    Section2 = Deck[Second+1:]
    Deck = Section2 + Center + Section1

    # Performing a card count using the bridge order of suits: clubs, diamonds, hearts, and spades
    if Deck[53] == 'A':
        Deck = Deck
    elif Deck[53] == 'B':
        Deck = Deck
    else:
        Part1 = Deck[:Deck[53]]
        Part2 = Deck[Deck[53]:53]
        lastCard = Deck[53]
        Deck = Part2 + Part1 
        Deck.append(lastCard)

    # Finding the output card, which gives the output number
    if Deck[0] == 'A' or Deck[0] == 'B':
        if Deck[53] == 'A' or Deck[53] == 'B':
            return keystream();
        else:
            if Deck[53] <= 26:
                outputNumber = Deck[53]
            else:
                outputNumber = Deck[53] - 26
    else:
        if Deck[Deck[0]] == 'A' or Deck[Deck[0]] == 'B':
            return keystream();
        else:
            if Deck[Deck[0]] <= 26:
                outputNumber = Deck[Deck[0]]
            else:
                outputNumber = Deck[Deck[0]] - 26

    return outputNumber


def encryption(length):
    # This function encrypts the plaintext into ciphertext using the Solitaire Cipher
    # The first input is the outputNumber from the keystream function, each outputNumber encrypts a single character
    # The second input is the number of characters after which to put a space


    plaintext = 'DO NOT USE PC' # THIS IS FOR TEST PURPOSES ONLY, YOU CAN USE ANY TEXT
    # removes the spaces in the plaintext
    noSpacesPlain = plaintext.replace(" ", "")
    # equally spaces out the plaintext
    plaintext = ' '.join(noSpacesPlain[i:i+length] for i in range(0,len(noSpacesPlain),length))
 
    # Preallocate space 
    keystreamArray = [0]*len(noSpacesPlain)
    keystreamNumber = [0]*len(noSpacesPlain)

    # Generate the individual output cards/numbers
    for i in range(1, len(keystreamArray)+1):
        keystreamNumber[i-1] = keystream()
        keystreamArray[i-1] = chr(keystreamNumber[i-1]+64)
    
    # equally spaces out the keystream
    noSpacesKey = ''.join(keystreamArray)
    keystreamText = ' '.join(noSpacesKey[i:i+length] for i in range(0,len(noSpacesKey),length))

    # Creates the ciphertext
    numberPlain = [0]*len(noSpacesPlain)
    numberCipher = [0]*len(noSpacesPlain)
    textCipher = [0]*len(noSpacesPlain)
    for j in range(1, len(numberPlain)+1):
        numberPlain[j-1] = ord(noSpacesPlain[j-1]) -64
        numberCipher[j-1] = numberPlain[j-1] + keystreamNumber[j-1]
        if numberCipher[j-1] <= 26:
            textCipher[j-1] = chr(numberCipher[j-1] +64)
        else:
            textCipher[j-1] = chr((numberCipher[j-1] -26) +64)

    # gets the ciphertext in the same format as the plaintext
    noSpacesCipher = ''.join(textCipher)
    ciphertext = ' '.join(noSpacesCipher[i:i+length] for i in range(0,len(noSpacesCipher),length))

    print("The original plaintext is: ", plaintext)
    print("The encrypted ciphertext is: ", ciphertext)
    return (numberCipher, keystreamNumber)



def decryption(length):
	# This function decrypts the ciphertext into plaintext using the Solitaire Cipher
    # The input is the number of characters after which to put a space


    KeyStream = encryption(length)
    numberCipher = KeyStream[0]
    keystreamNumber = KeyStream[1]

    # Preallocate the space 
    numberPlain = [0]*len(numberCipher)
    plaintext = [0]*len(numberCipher)

    # Creates the plaintext
    for k in range(1,len(numberCipher) +1):
    	if numberCipher[k-1] < keystreamNumber[k-1]:
    		numberPlain[k-1] = (numberCipher[k-1] +26) -keystreamNumber[k-1]
    	else:
    		numberPlain[k-1] = numberCipher[k-1] -keystreamNumber[k-1]

    	plaintext[k-1] = chr(numberPlain[k-1] +64)

    noSpaces = ''.join(plaintext)
    plaintext = ' '.join(noSpaces[i:i+length] for i in range(0,len(noSpaces),length))

    print("The decrypted plaintext is: ", plaintext)


# Examples: 
# encryption(5)
decryption(5)


