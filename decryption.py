import hashlib
import json
#step 0:  Load public key from file
public_key_path = "public_key.json"
try:
    with open(public_key_path, "r") as key_file:
        public_key = json.load(key_file)
    e = public_key["e"]
    n = public_key["n"]
    print("✅ Public key loaded successfully.")
except Exception as e:
    print(f"❌ Error loading public key: {e}")
    exit()
# Step 1: compute sha-256 hash for the received document
file_path_received=r"C:\documents\cryptography and network security\project\file\rsa.py"
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
sig_path=r"C:\documents\cryptography and network security\project\file\signature.sig"
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