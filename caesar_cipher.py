def caesar_cipher(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            start=ord('A')if char.isupper()else ord('a')
            end =ord('Z')if char.isupper()else ord ('z')
            new_char=chr(end -(ord(char)-start))
            print(ord(char))
            result+=new_char
        else:
            result+=char
    return result
message="hello"
shift=25
encrypted=caesar_cipher(message,shift)
print("Encrypted:",encrypted)
decrypted=caesar_cipher(encrypted,-shift)
print("decrypted:",decrypted)
