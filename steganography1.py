import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from PIL import Image
def text_to_binary(text):
    return ''.join(format(ord(char),'08b')for char in text)
def encode_image(image_path,secret_message,output_path):
    image = Image.open(image_path)
    binary_message = text_to_binary(secret_message) + '1111111111111110'
    data = list(image.getdata())
    new_data=[]
    msg_index=0
    for pixel in data:
        pixel=list(pixel)
        for i in range(3):
            if msg_index < len(binary_message):
                pixel[i]=pixel[i]&~1|int (binary_message[msg_index])
                msg_index+=1
        new_data.append(tuple(pixel))
    image.putdata(new_data)
    image.save(output_path)
    print(f"message encoded and save as{output_path}")
encode_image(
    r"D:\SWEATHA\temple.jpg",
    "hello world",
    r"D:\SWEATHA\encoded.png"
)
