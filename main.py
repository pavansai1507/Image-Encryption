pip install numpy opencv-python
import cv2
import numpy as np

def img_encrypt(img_path, key):
    # Load image
    img = cv2.imread(img_path)

    # Convert image to NumPy array
    img_array = np.array(img, dtype=np.uint8)

    # XOR encryption
    for i in range(len(img_array)):
        for j in range(len(img_array[0])):
            img_array[i, j] = img_array[i, j] ^ key

    # RGB to BGR conversion
    img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # Save encrypted image
    cv2.imwrite("encrypted_image.png", img_array)

def img_decrypt(encrypted_path, key):
    # Load encrypted image
    encrypted_img = cv2.imread(encrypted_path)

    # Convert image to NumPy array
    encrypted_array = np.array(encrypted_img, dtype=np.uint8)

    # XOR decryption
    for i in range(len(encrypted_array)):
        for j in range(len(encrypted_array[0])):
            encrypted_array[i, j] = encrypted_array[i, j] ^ key

    # RGB to BGR conversion
    encrypted_array = cv2.cvtColor(encrypted_array, cv2.COLOR_RGB2BGR)

    # Save decrypted image
    cv2.imwrite("decrypted_image.png", encrypted_array)

if _name_ == "_main_":
    # Replace "image.jpg" with the desired image's file name
    img_encrypt("image.jpg", 27
