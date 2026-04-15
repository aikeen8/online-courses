'''
Understanding Functions and Scope
==========================
Lesson consists of:
- def keyword
- Parameters and arguments
- Return values
- Local and global scope
==========================
'''

def caesar(text, shift, encrypt=True): # def keyword is used to define a function named caesar that takes three parameters: text, shift, and encrypt (with a default value of True).

    if not isinstance(shift, int): # not isinstance(shift, int) checks if the shift parameter is not an integer. If it is not an integer, the function returns a message indicating that the shift must be an integer value.
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift # If the encrypt parameter is False, the shift value is negated to reverse the direction of the shift for decryption.
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift] 
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()) # upper() method is used to convert the alphabet string to uppercase, and str.maketrans() creates a translation table that maps each letter in the original alphabet (both lowercase and uppercase) to its corresponding letter in the shifted alphabet.
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)

'''
OUTPUT:
Pbhentr vf sbhaq va hayvxryl cynprf.
'''