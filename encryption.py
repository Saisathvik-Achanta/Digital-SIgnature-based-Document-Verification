#license - Achanta Saisathvik
import random 
from sympy import isprime
from sympy import mod_inverse
import math
import hashlib
# step 1 : creation of public and private keys
p=131
q=151
n=p*q
print("n=",n)
o=(p-1)*(q-1)
print("o=",o)
gcds=[]
for i in range(2,o):
    if math.gcd(i,o)==1:
        e=i
        break
print("e=",e)
#computing value d×e≡1 mod(o)
d = mod_inverse(e, o)
print("d=",d)
#step 2 :document signing
# reading file and converting it into binary data
file=r"" # file path to be given in double quotes eg:C:\documents\cryptography and network security\project\file\rsa.py
def generate_sha256_hash(file_path):
    with open(file_path, "rb") as f:
        file_data = f.read()
    sha256_hash = hashlib.sha256(file_data)  # mapped object
    hash_hex = sha256_hash.hexdigest() # Raw binary hash
    return hash_hex
document_hash = generate_sha256_hash(file)
print("SHA-256 Hash:",document_hash)
# we got sha 256 hash in hexadecimal format and  will convert binary to integer
#using in-built function to do the same
hash_int = int(document_hash, 16)
print("hexadecimal hash converted into integer:",hash_int)
# step 3: encrypting sha 256 hash with private key
signature= pow(hash_int%n,d,n)
print('signature:',signature)
#step 4: now creating a signature file to my document
file_save_path = r"" #a path should be given in double quotes to save the signature file eg:C:\documents\cryptography and network security\project\file\signature.sig
try:
    signature_hex = hex(signature)
    with open(file_save_path, "w") as f:
        f.write(signature_hex)
    print(f"✅ Digital signature file created and saved at: {file_save_path}")
except Exception as e:
    print(f"❌ Error: {e}")