import cv2
import hashlib

# Specify the path to the encrypted image
encrypted_image_path = r"C:\Users\ambat\OneDrive\Desktop\Cyber Security\encryptedImage.jpg"

# Read the encrypted image
img = cv2.imread(encrypted_image_path)

# Check if the image is successfully loaded
if img is None:
    print("Image not found. Check the file path and make sure the image exists.")
    exit()

# Get the dimensions of the image
height, width, channels = img.shape

# Prompt the user to input the password
password = input("Enter the passcode: ")

# Hash the password using SHA-256
hash_object = hashlib.sha256(password.encode())
hashed_password = hash_object.digest()

# Initialize dictionaries for mapping ASCII values to characters
d = {}  # Character to ASCII
c = {}  # ASCII to character

# Fill the dictionaries with ASCII values (0-255)
for i in range(256):
    d[chr(i)] = i  # Character to ASCII
    c[i] = chr(i)  # ASCII to character

# Initialize variables for image coordinates and color channel
n = 0  # Row index
m = 0  # Column index
z = 0  # Color channel index

# Prepare a list to store the decoded message characters
decoded_message = []

# Decode the message from the image using the hashed password
while n < height:
    # Calculate the original pixel value to retrieve the character
    pixel_value = int(img[n, m, z])
    hashed_value = hashed_password[len(decoded_message) % len(hashed_password)]
    original_value = (pixel_value ^ hashed_value) % 256  # Ensure value is within 0-255 range
    
    # Only append printable ASCII characters (range 32-126)
    if 32 <= original_value <= 126:
        decoded_message.append(c[original_value])

    # Move to the next pixel
    m += 1
    if m >= width:
        m = 0
        n += 1

    # Cycle through the color channels (0, 1, 2)
    z = (z + 1) % 3

# Convert the list of characters into a string
decoded_message = ''.join(decoded_message)

# Print the decoded message
print("Decoded message:", decoded_message)
