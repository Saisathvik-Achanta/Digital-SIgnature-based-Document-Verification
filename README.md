Digital Signature Verification Using SHA-256 in Cryptography
Abstract
This project implements a digital signature verification system using the SHA-256 hashing algorithm and RSA encryption.
It allows a sender to sign a document using their private key and provides the receiver with the ability to verify the authenticity and integrity of the document using the sender’s public key.
The system ensures the document has not been tampered with during transmission.

Pre-requisites
To run and understand this project, you will need the following:
Python 3.x installed on your system.
SymPy library for mathematical computations (install with pip install sympy).
hashlib module for SHA-256 hashing (pre-installed with Python).
Basic understanding of RSA encryption, digital signatures, and hashing.

What is SHA-256 Hashing?
SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that produces a 256-bit hash value from any given input. Even a small change in the input will result in a drastically different hash value. 
This makes SHA-256 extremely useful for data integrity checks.

Why Use SHA-256?
Collision resistance: It's very difficult to find two different inputs that result in the same hash.
Pre-image resistance: It's infeasible to reverse a hash back into its original input.
Widely adopted: It is used in numerous cryptographic protocols such as digital signatures, certificates, and blockchain.
In this project, SHA-256 is used to create a fixed-size representation of a document, which is then signed with the sender’s private key to ensure authenticity.

Generating Public and Private Keys
RSA Key Generation Overview
Choose two large prime numbers p and 𝑞.
Compute 𝑛=𝑝×𝑞 and 𝑜=(𝑝−1)×(𝑞−1).
Choose a public exponent 𝑒 such that 1<𝑒<𝑜 and gcd(e,o)=1.
Compute the private key d such that d×e≡1modo.
The public key is a pair (e,n), and the private key is a pair (d,n).

Signing a Document (Encryption Process)
Step 1: Load the Private Key
The sender loads their private key from a file, which will be used for signing the document.
Step 2: Hash the Document
The sender computes a SHA-256 hash of the document. This produces a unique fixed-size representation of the document.
Step 3: Sign the Hash
The sender encrypts the hash using their private key. This step is the digital signature of the document.
Step 4: Save the Signature
The digital signature is saved to a file and can be sent to the receiver along with the document.

Verifying the Document (Decryption Process)
Step 1: Load the Public Key
The receiver loads the sender's public key from a file, which will be used to verify the signature.
Step 2: Hash the Received Document
The receiver computes the SHA-256 hash of the received document to obtain its unique representation.
Step 3: Read the Signature
The receiver reads the signature from the file that was sent along with the document.
Step 4: Decrypt the Signature
The receiver decrypts the signature using the sender's public key. This will recover the original hash value signed by the sender.
Step 5: Verify the Integrity
Finally, the receiver compares the decrypted hash with the hash of the received document. If they match, the document is verified to be authentic and untampered with.

Workflow
Sender generates RSA keys (public and private) and stores them in files (private_key.json, public_key.json).
The sender signs the document using their private key. The signature is saved in signature.sig.
The receiver loads the public key and verifies the integrity of the document using the signature provided by the sender.
If the decrypted signature matches the hash of the received document, the document is authentic and has not been tampered with.

Conclusion
This project effectively demonstrates the process of digital signature generation and verification using SHA-256 and RSA encryption. 
By leveraging the properties of hashing and RSA, this method ensures the integrity and authenticity of digital documents.
For detailed code, please refer to the respective Python scripts in this repository.
