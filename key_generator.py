from sympy import randprime,mod_inverse
import json
#generating large primes
p=randprime(2**8,2**9)
q=randprime(2**8,2**9)
n=p*q
o=(p-1)*(q-1)
#exponent e
e=65537
#d value 
d=mod_inverse(e,o)
# Store public key in a seperate file
public_key = {"e": e, "n": n}
with open("public_key.json", "w") as pub_file:
    json.dump(public_key, pub_file)
print("✅ Public key saved as public_key.json")

# Store private key in a separate file
private_key = {"d": d, "n": n}
with open("private_key.json", "w") as priv_file:
    json.dump(private_key, priv_file)
print("✅ Private key saved as private_key.json")