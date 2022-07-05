# Importing required classes/functions
from PIL import Image
from random import randint
import numpy as np

def encode(img_path,message):
    # Converting message from string to list
    message = list(' '+message)
    img = Image.open(img_path) # Opening the image
    
    # Getting width and height of the image
    width, height = img.size
    
    # Defining no.of pixels
    pixels = width*height
    
    # Checking if message is bigger than no.of pixels
    if pixels<len(message):
        print("Your message is bigger than no.of pixels of the image.\nEncoding is not possible!")
    else:
        while True:
            skip = randint(3,209)
            if pixels//skip >= len(message):
                break
        # Convert image to numpy array
        edit_image = np.array(img)
        counter = 0
        info = False
        j = 0
        while j < pixels:
            k = j%width
            i = j//height
            if counter >= len(message):
                break
            elif j == 0 and info == False:
                edit_image[i][k][2] = len(message)-1
                edit_image[i][k+1][2] = skip
                info = True
            else:
                edit_image[i][k][2] = ord(message[counter])
                counter += 1
            j+=skip
        # Creates Pillow image object
        image = Image.fromarray(edit_image)

        # Getting image path without extension
        new_path = img_path.split('.')

        # Saving encoded image on the same path
        image.save(f'{new_path[0]}(encoded).png')
        print("Message encoded!")

def decode(img_path):
    message = ''
    img = Image.open(img_path)
    img_arr = np.array(img)
    length = img_arr[0][0][2]
    skip = img_arr[0][1][2]
    width, height = img.size
    pixels = width * height
    j = 0
    j += skip
    while j < pixels:
        k = j % width
        i = j // height
        if len(message) > length:
            break
        else:
            message += chr(img_arr[i][k][2])
        j += skip

    print(f"Your decoded message is: {message}")

print("Welcome")
task = input("Do you want to: (1)Hide message, (2)Retrieve message:")

if task == "1":
    path = input("Enter image path:")
    msg = input("Enter message to hide:")
    encode(path,msg)
elif task == "2":
    path = input("Enter image path:")
    decode(path)
else:
    print("Invalid Input!")