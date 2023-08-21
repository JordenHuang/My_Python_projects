import numpy as np
import PIL.Image

# open the source image
image = PIL.Image.open('../cat_img.png', 'r')
# image_info = image.info

# turn it into numpy array
img_array = np.array(list(image.getdata()))

if image.mode == "P":  # P means, 8-bit pixels, mapped to any other mode using a color palette
    raise "Not Supported!"

# count the channels
channels = 4 if image.mode == 'RGBA' else 3

width, height = image.size

# the number of pixles in the image
pixels = img_array.size // channels

# get the secret message from user
# secret_msg = input('Enter the secret message: ')
secret_msg = "Wow! You find the SECRET MESSAGE!\nai'you'bu'cuo',bei'ni'jie'chu'lai'le'\ntranslator: https://translate.google.com/?hl=zh-HK&sl=auto&tl=zh-TW&op=translate"


# add the stop indicator to show where the msg stopped when decoding
stop_indicator = "$EoM$"
stop_indicator_len = len(stop_indicator)

secret_msg += stop_indicator


# turn the secret msg into bit string
byte_msg = ''.join(f"{ord(c):08b}" for c in secret_msg)
bits_of_byte_msg = len(byte_msg)

# if not enough space, don't add secret msg in the image
if bits_of_byte_msg > pixels:
    print("Not enough space")

# else, change the R, G, B 's least significent bit to the secret bit string one by one
else:
    index = 0
    for i in range(pixels):
        for j in range(0, 3):
            if index < bits_of_byte_msg:
                # print(img_array[i][j], end='\n ')
                img_array[i][j] = int(bin(img_array[i][j])[2:-1] + byte_msg[index], 2)
                index += 1
                # print(img_array[i][j])


# print(img_array)
# print('----------------------')
# reshape the numpy array
img_array = img_array.reshape((height, width, channels))
# print(img_array)

# save the encoded image
result = PIL.Image.fromarray(img_array.astype('uint8'), mode=image.mode)
result.save('encoded.png')