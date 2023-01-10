def Encrypt_Cesar_Cipher(string, shift = -3):
    string = string.lower()
    new_string = ''
    for char in string:
        ascii_val = ord(char)
        # makes ascii value a base of 0 and then adds in the shift, once modded
        # by 26 that returns the value it increased or decreased by and adds it 
        # to ascii value starting at 97 in instance of modding a negative, it returns 26 - the num being modded
        new_string += chr(((ascii_val - 97 + shift) % 26) +97)
    return new_string

def Dencrypt_Cesar_Cipher(string, shift = 3):
    string = string.lower()
    new_string = ''
    for char in string:
        ascii_val = ord(char)
        # makes ascii value a base of 0 and then adds in the shift, once modded
        # by 26 that returns the value it increased or decreased by and adds it 
        # to ascii value starting at 97 in instance of modding a negative, it returns 26 - the num being modded
        new_string += chr(((ascii_val - 97 - shift) % 26) +97)
    return new_string

# Cipher shifted left 3
shift = -3

string = 'abcdefghijklmnopqrstuvwxyz'
print("String: " + string, end= "\n\n" )
Encrypted_Word = Encrypt_Cesar_Cipher(string, shift)
print("String Encrypted: " + Encrypted_Word, end= "\n\n" )
Dencrypted_Word = Dencrypt_Cesar_Cipher(Encrypted_Word, shift)
print("String Decrypted: " + Dencrypted_Word, end= "\n\n" )

