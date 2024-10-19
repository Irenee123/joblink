from PIL import Image
import numpy as np
from colorama import init, Fore

# change 'path_to_your_image/image.jpg' with your image file path
image_path = 'img_1.png'

# Image opening
img = Image.open(image_path)

# Convert the image to grayscale
img = img.convert('L')

# change the image to  better fit the terminal window
new_width = 130  # Desired width for the output in the terminal
new_height = 10

img = img.resize((new_width, new_height))

# look the image data as a numpy array
img_array = np.array(img)

# Define ASCII characters used for different intensity levels
ASCII_CHARS = '######## '

# Define corresponding ANSI color codes for different intensity levels
COLORS = [
    Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.CYAN,
    Fore.LIGHTGREEN_EX, Fore.GREEN, Fore.LIGHTRED_EX, Fore.RED,
    Fore.LIGHTRED_EX, Fore.RED, Fore.LIGHTMAGENTA_EX, Fore.MAGENTA,
    Fore.LIGHTWHITE_EX, Fore.WHITE, Fore.LIGHTBLACK_EX, Fore.RED
]
# Initialize colorama for terminal color support
init(autoreset=True)

# Convert the image to colored ASCII art
ascii_str = ''
for row in img_array:
    for pixel_value in row:
        # Normalize pixel value to range [0, 15] (number of ASCII characters - 1)
        intensity_index = min(int((pixel_value / 250) * 15), len(ASCII_CHARS) - 1)
        ascii_str += COLORS[intensity_index] + ASCII_CHARS[intensity_index]  # Apply colour
    ascii_str += '\n'

# Display the colored ASCII art in the terminal


def logo():
    print(ascii_str)