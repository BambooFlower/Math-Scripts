# This is a python implementation of the Vigenere Cipher, it employs a form of polyalphabetic substitution and remained unbreakable for three centuries 
# Reference can be found at: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

# In this implementaion we will use the keyword: LEMON

import math

def encryption():
    # This function encrypts the plaintext into ciphertext using the Vigenere Cipher
    # It follows the standard set by the Tabula Reacta

    keyword = 'LEMON'
    plaintext = 'ATTACK AT DAWN'
    # Removes the spaces in the plaintext
    noSpaces = plaintext.replace(" ", "")

    # Preallocates space for efficiency
    cipherArray = [0]*len(noSpaces)
    numberPlain = [0]*len(noSpaces)
    numberKeyword = [0]*len(noSpaces)


    for i in range(0, len(noSpaces)):
        # Converts each character into a number
        numberPlain[i] = ord(noSpaces[i]) - 64
        # It counts the number of times we have to repeat the keyword
        count = math.floor(i/len(keyword))

        # A minus 1 is required to be consistent with Tabula Reacta
        numberKeyword[i] = (ord(keyword[i -(count*len(keyword))]) - 64) -1

        # Performs the encryption
        if ((numberPlain[i] + numberKeyword[i]) %26) == 0:
            cipherArray[i] = 'Z'
        else:
            cipherArray[i] = chr(((numberPlain[i] + numberKeyword[i]) %26) +64)

    ciphertext = ''.join(cipherArray)

    print('The original plaintext is: ', plaintext)
    print('The encrypted ciphertext is: ', ciphertext)
    return(ciphertext)



def decrytpion():
    # This function decrypts the ciphertext into plaintext using the Vigenere Cipher
    # It follows the standard set by the Tabula Reacta

    keyword = 'LEMON'
    ciphertext = encryption()
    noSpaces = ciphertext.replace(" ", "")

    # Preallocates space for efficiency
    plainArray = [0]*len(noSpaces)
    numberCipher = [0]*len(noSpaces)
    numberKeyword = [0]*len(noSpaces)


    for i in range(0, len(noSpaces)):
        # Converts each character into a number
        numberCipher[i] = ord(noSpaces[i]) - 64
        # It counts the number of times we have to repeat the keyword
        count = math.floor(i/len(keyword))

        # A minus 1 is required to be consistent with Tabula Reacta
        numberKeyword[i] = (ord(keyword[i -(count*len(keyword))]) - 64) -1

        # Performs the encryption
        if ((numberCipher[i] - numberKeyword[i]) %26) == 0:
            plainArray[i] = 'Z'
        else:
            plainArray[i] = chr(((numberCipher[i] - numberKeyword[i]) %26) +64)

    plaintext = ''.join(plainArray)
    print('The dencrypted plaintext is: ', plaintext)




# Examples:
# encryption()
decrytpion()

