def caesar_cipher(text,shift):
    result=""
    for char in text:
        if char.isalpha():
             
            start=ord('z')if char.isupper()else ord('a')
            new_char=chr ((ord(char)- start +shift)%26+ start)
            result+=new_char
        else:
            result+=char
    return result
message="a"
shift=3
encrypted=caesar_cipher(message,shift)
print("Enceypted:",encrypted)
decrypted=caesar_cipher(encrypted,-shift)
print("decrypted:",decrypted)
