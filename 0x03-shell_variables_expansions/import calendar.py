#import all modules needed for encryption
from Crypto.Cipher import AES
import base64
import hashlib
import sys
import os
import time
from Crypto.Cipher import AES
import os

# Generate a random secret key
secret = os.urandom(16)

# Create an instance of the AES cipher object
cipher = AES.new(secret)

# Data to be encrypted
plaintext = b'This is a secret message.'

# Encrypt the plaintext data
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext data
decrypted_text = cipher.decrypt(ciphertext)

print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decrypted text: ", decrypted_text)

    