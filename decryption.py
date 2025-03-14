#license - Achanta Saisathvik
import random 
from sympy import mod_inverse
import math
import hashlib
#for insatnce know the public key of sender
e=7
n=19781
# Step 1: compute sha-256 hash for the received document
file_path_received=r"" # path of the received file should be given in double quotes eg:C:\Users\achan\Downloads\file\rsa.py
def generate_sha256_hash(file_path_received):
    with open(file_path_received, "rb") as f:
        file_data = f.read()
    sha256_hash = hashlib.sha256(file_data)  # mapped object
    hash_hex = sha256_hash.hexdigest() # Raw binary hash
    return hash_hex
document_hash = generate_sha256_hash(file_path_received)
print("SHA-256 Hash:",document_hash)
#step 2: converting hexadecimal hash into integer
hash_int = int(document_hash, 16)  # Convert hex to decimal integer
print("Computed Hash Integer:", hash_int)
#step 3: read the siganture in signature.sig
sig_path=r"" # path of the received signature file should be given eg:C:\Users\achan\Downloads\file\signature.sig
with open(sig_path, "r") as file:
    signature_hex = file.read().strip()
#step 4: convert the hexadecimal back to integer
signature_int = int(signature_hex, 16) 
print("Recovered Signature Integer:", signature_int)
# Step 5: decrypt the signature using sender's public key
decrypted_hash = pow(signature_int, e, n)  
print("Decrypted Hash Integer:", decrypted_hash)

# Final Step: Verify Integrity
if decrypted_hash == hash_int%n:
    print("✅ Signature is valid! Document is authentic.")
else:
    print("❌ Signature is invalid! Document may be tampered.")