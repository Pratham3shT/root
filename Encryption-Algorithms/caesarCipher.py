def input_encrypt():
    print("Enter your plain text: ", end="")
    plain_text = str(input())
    print("Enter the shift key: ", end="")
    key = int(input())
    print("The encrypted text in caesar cipher format is",
          cipherText(plain_text, key))


def input_decrypt():
    print("Enter your cipher text: ", end="")
    cipher_text = str(input())
    print("Enter the shift key: ", end="")
    key = int(input())
    print("The plain text after decryption from caesar cipher format is",
          plainText(cipher_text, key))


def cipherText(plain_text, key):
    cipher_text = ""

    for i in range(len(plain_text)):
        char = plain_text[i]

        if (char.isupper()):
            cipher_text += chr((ord(char) + key - 65) % 26 + 65)

        else:
            cipher_text += chr((ord(char) + key - 97) % 26 + 97)

    return cipher_text


def plainText(cipher_text, key):
    plain_text = ""

    for i in range(len(cipher_text)):
        char = cipher_text[i]

        if (char.isupper()):
            plain_text += chr((ord(char) - key - 65) % 26 + 65)

        else:
            plain_text += chr((ord(char) - key - 97) % 26 + 97)

    return plain_text


def caesarCipher():

    print("Do you want to encrypt or decrypt the data ? ", end="")
    flag = str(input())

    if (flag.lower() == "encrypt"):
        input_encrypt()
        again()
    elif (flag.lower() == "decrypt"):
        input_decrypt()
        again()
    else:
        print("Kindly type encrypt or decrypt: ")
        caesarCipher()
        again()


def again():
    print("Do you want to use our program again? ", end="")
    ag = str(input())

    if (ag.lower() == "yes"):
        caesarCipher()
    elif (ag.lower() == "no"):
        print("Thank you for using our program.")
    else:
        print("Kindly type yes or no: ",end="")
        again()


print("$$ CAESAR CIPHER ENCRYPTION AND DECRYPTION BY Pratham3shT $$")
caesarCipher()

"""
Output:

$$ CAESAR CIPHER ENCRYPTION AND DECRYPTION BY Pratham3shT $$
Do you want to encrypt or decrypt the data ? encrypt
Enter your plain text: prathamesh
Enter the shift key: 54
The encrypted text in caesar cipher format is rtcvjcoguj
Do you want to use our program again? yes
Do you want to encrypt or decrypt the data ? decrypt
Enter your cipher text: rtcvjcoguj
Enter the shift key: 54
The plain text after decryption from caesar cipher format is prathamesh
Do you want to use our program again? nope
Kindly type yes or no: Do you want to use our program again? no
Thank you for using our program.
"""