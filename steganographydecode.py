from PIL import Image

def binary_to_text(binary):
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text

def decode_image(image_path):
    image = Image.open(image_path)

    data = list(image.getdata())

    binary_message = ""

    for pixel in data:
        for i in range(3):
            binary_message += str(pixel[i] & 1)

    end_marker = "1111111111111110"
    end_index = binary_message.find(end_marker)

    if end_index != -1:
        binary_message = binary_message[:end_index]

    secret_message = binary_to_text(binary_message)

    print("Decoded Message:", secret_message)

decode_image(r"D:\SWEATHA\encoded.png")
