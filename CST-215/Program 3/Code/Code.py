# Matthew Powers
# This is my own work

def Encrypt_Cesar_Cipher(string, shift):
    string = string.lower()
    new_string = ''
    for char in string:
        ascii_val = ord(char)
        # makes ascii value a base of 0 and then adds in the shift, once modded
        # by 26 that returns the value it increased or decreased by and adds it 
        # to ascii value starting at 97 in instance of modding a negative, it returns 26 - the num being modded
        new_string += chr(((ascii_val - 97 + shift) % 26) +97)
    return new_string

def Decrypt_Cesar_Cipher(string, shift):
    string = string.lower()
    new_string = ''
    for char in string:
        ascii_val = ord(char)
        # makes ascii value a base of 0 and then adds in the shift, once modded
        # by 26 that returns the value it increased or decreased by and adds it 
        # to ascii value starting at 97 in instance of modding a negative, it returns 26 - the num being modded
        new_string += chr(((ascii_val - 97 - shift) % 26) +97)
    return new_string

def Encrypt_Vigenere_Cipher(text, key):
    text = text.lower()

    encrypted_text = ''

    key_index = 0
    for i in range(0,len(text)):
        # this ensure only a-z are changed and everything else is preserved
        if (ord(text[i]) >= ord('a')) and (ord(text[i]) <= ord('z')):
                                        # have to do mod so it is always in range of the key
            shift = abs(ord('a')-ord(key[key_index%len(key)]))
            new_letter = Encrypt_Cesar_Cipher(text[i], shift)
            key_index += 1
        else:
            new_letter = text[i]
        encrypted_text = encrypted_text + new_letter
    return encrypted_text

def Decrypt_Vigenere_Cipher(text, key):
    text = text.lower()

    decrypted_text = ''

    key_index = 0
    for i in range(0,len(text)):
        # this ensure only a-z are changed and everything else is preserved
        if (ord(text[i]) >= ord('a')) and (ord(text[i]) <= ord('z')):
                                        # have to do mod so it is always in range of the key
            shift = abs(ord('a')-ord(key[key_index%len(key)]))
            new_letter = Decrypt_Cesar_Cipher(text[i], shift)
            key_index += 1
        else:
            new_letter = text[i]
        decrypted_text = decrypted_text + new_letter
    return decrypted_text

print()
key = 'applesauce'
text = 'last project of the year, this is really cool!!'
print("Original text...\n" + text, end="\n\n")

encrypted_text = Encrypt_Vigenere_Cipher(text, key)
print("Encoded text...\n" + encrypted_text, end="\n\n")

decrypted_text = Decrypt_Vigenere_Cipher(encrypted_text, key)
print("Decoded text...\n" + decrypted_text, end="\n\n")