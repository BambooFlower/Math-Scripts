# This is a python implementation of the Caesar Cipher, one of the most famous substitution cipher
# Reference can be found at: https://en.wikipedia.org/wiki/Caesar_cipher

def encryption(shift):
    # This function encrypts the plaintext into ciphertext using the Caesar Cipher
    # The input 'shift' is the number of positions down the alphabet each character is moved 

    plaintext = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
    # Removes the spaces in the plaintext
    noSpaces = plaintext.replace(" ", "")
    # Preallocates space for efficiency
    cipherArray = [0]*len(noSpaces)
    numberPlain = [0]*len(noSpaces)

    # Performs the encryption
    for i in range(0, len(noSpaces)):
        numberPlain[i] = ord(noSpaces[i]) - 64

        if ((numberPlain[i] - shift) %26) == 0:
            cipherArray[i] = 'Z'
        else:
            cipherArray[i] = chr(((numberPlain[i] - shift) %26) +64)


    ciphertext = ''.join(cipherArray)

    print('The original plaintext is: ', plaintext)
    print('The encrypted ciphertext is: ', ciphertext)
    return(ciphertext)



def decryption(shift):
    # This function decrypts the ciphertext into plaintext using the Caesar Cipher
    # The input 'shift' is the number of positions down the alphabet each character is moved 

    ciphertext = encryption(shift)
    noSpaces = ciphertext.replace(" ", "")
    plainArray = [0]*len(noSpaces)
    numberCipher = [0]*len(noSpaces)

    # Performs the decryption
    for i in range(0, len(noSpaces)):
        numberCipher[i] = ord(noSpaces[i]) - 64

        if ((numberCipher[i] + shift) %26) == 0:
            plainArray[i] = 'Z'
        else:
            plainArray[i] = chr(((numberCipher[i] + shift) %26) +64)

    plaintext = ''.join(plainArray)
    print('The decrypted plaintext is: ', plaintext)



# Examples:
# encryption(3)
decryption(3)