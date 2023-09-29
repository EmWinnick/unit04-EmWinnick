
# convert letter paramter into an integer using ord()
# add shift value to int letter value
# use ASCII function to convert product value into a character
# return final character value

def is_alphabetic(character):
    code = ord(character)
    return code >= 65 and code <= 90

def encrypt_letter(letter, shift):
    if is_alphabetic():
        code = ord(letter)
        shifted = code + shift
        encrypted = chr(shifted)
        return encrypted
    else:
        return ""
    
def decrypt_letter(message, shift=3):
    ciphertext = ""
    #code = ord(letter)
    #shifted = code - shift
   # if is_alphabetic():
       # decrypted = chr(shifted)
        #return decrypted
    #else:
        #return ""
    for letter in message:
        letter = decrypt_letter(letter, shift)
        ciphertext = ciphertext + letter
    return ciphertext

def encrypt_message(message, shift=3):
    ciphertext = ""
    for index in range(len(message)):
        letter = encrypt_letter(message[index], shift)
        ciphertext = ciphertext + letter
    #ciphertext = ciphertext + encrypt_letter(message [0], shift)
    #ciphertext = ciphertext + encrypt_letter(message [1], shift)
   # ciphertext = ciphertext + encrypt_letter(message [2], shift)
   # ciphertext = ciphertext + encrypt_letter(message [3], shift)
    #ciphertext = ciphertext + encrypt_letter(message [4], shift)
    return ciphertext
    


def main():
    #message = input("enter a letter: ")
    #print(encrypt_letter (message, 3))
    #print(encrypt_letter)
    message = input ("enter a phrase: ")
    tokens = message.split()
    for token in tokens:
        ciphertext = encrypt_message(token)
        print(ciphertext)

if __name__ == "__main__":
    main()

