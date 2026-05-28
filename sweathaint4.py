def caesar_cipher(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            start =ord('A')if char.isupper() else ord('a')
            new_char= chr((ord(char)-start +shift)%26 +start)
            result +=new_char
        else:
            result += char
    return result
message=" this is important message for you "
shift=5
encrypted = caesar_cipher(message,shift)
print("Encryted:",encrypted)
decrypted= caesar_cipher (encrypted, -shift)
print("Decrypted:",decrypted)
