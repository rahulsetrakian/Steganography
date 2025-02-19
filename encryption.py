# import the liabraries
import cv2
import os
import hashlib

# Specify the path to the input image
image_path = r"C:\Users\ambat\OneDrive\Desktop\Cyber Security\encoded.jpeg"

# Read the input image wr have to set the variable 
img = cv2.imread(image_path)

# Check if the image is successfully loaded
if img is None:
    print("Image not found. Check the file path and make sure the image exists.")
    exit()

# Get the dimensions of the image
height, width, channels = img.shape

# Prompt the user to input the secret message
msg = input("Enter secret message: ")

# Prompt the user to input the password
password = input("Enter a passcode: ")

# Hash the password using SHA-256
hash_object = hashlib.sha256(password.encode())
hashed_password = hash_object.digest()

# Initialize dictionaries for mapping characters to their ASCII values and vice versa
d = {}
c = {}

# Fill the dictionaries with ASCII values (0-255)
for i in range(256):
    d[chr(i)] = i  # Character to ASCII
    c[i] = chr(i)  # ASCII to character

# Initialize variables for image coordinates and color channel
n = 0  # Row index
m = 0  # Column index
z = 0  # Color channel index

# Encode the secret message into the image using the hashed password
for i in range(len(msg)):
    # Ensure the calculation stays within the 0-255 range
    new_value = (int(img[n, m, z]) + d[msg[i]] + hashed_password[i % len(hashed_password)]) % 256
    img[n, m, z] = new_value
    
    # Move to the next pixel
    m += 1
    
    # If the column index exceeds the image width, reset it and move to the next row
    if m >= width:
        m = 0
        n += 1
    
    # If the row index exceeds the image height, stop encoding (message too large for image)
    if n >= height:
        print("Image too small to hold the entire message.")
        break
    
    # Cycle through the color channels (0, 1, 2) for RGB
    z = (z + 1) % 3

# Save the modified image to a new file
encrypted_image_path = os.path.join(os.path.dirname(image_path), "encryptedImage.jpg")
cv2.imwrite(encrypted_image_path, img)

# Open the newly saved encrypted image
os.startfile(encrypted_image_path)

print(f"Message has been encoded into '{encrypted_image_path}'.")
