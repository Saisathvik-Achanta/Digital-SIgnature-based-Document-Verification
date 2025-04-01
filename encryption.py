import hashlib
import json
#step 1: Load private key from file
private_key_path = "private_key.json"
try:
    with open(private_key_path, "r") as key_file:
        private_key = json.load(key_file)
    d = private_key["d"]
    n = private_key["n"]
    print("✅ Private key loaded successfully.")
except Exception as e:
    print(f"❌ Error loading private key: {e}")
    exit()
#step 2 : document signing
# reading file and converting it into binary data
file=r"C:\documents\cryptography and network security\project\file\rsa.py"
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
file_save_path = r"C:\documents\cryptography and network security\project\file\signature.sig"
try:
    signature_hex = hex(signature)
    with open(file_save_path, "w") as f:
        f.write(signature_hex)
    print(f"✅ Digital signature file created and saved at: {file_save_path}")
except Exception as e:
    print(f"❌ Error: {e}")
