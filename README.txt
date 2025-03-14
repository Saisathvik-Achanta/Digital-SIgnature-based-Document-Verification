Digital Signature-Based Document Verification : Cryptography and Network Security.
Overview
This project implements a Digital Signature-Based Document Verification system using RSA encryption and SHA-256 hashing to ensure the authenticity and integrity of documents.
Features
•	Uses RSA public-private key pair for encryption and decryption.
•	Implements SHA-256 hashing for generating document fingerprints.
•	Supports file-based signature generation and verification.
•	Ensures data integrity by comparing computed and decrypted hash values.
Workflow
1. Key Generation
•	Chooses two prime numbers ppp and qqq.
•	Computes modulus n=p×qn = p \times qn=p×q and totient ϕ(n)\phi(n)ϕ(n).
•	Selects public key eee such that gcd(e, φ(n)) = 1.
•	Computes private key ddd using modular inverse.
2. Document Signing (Encryption Code)
•	Reads the file and computes SHA-256 hash.
•	Converts the hash from hexadecimal to integer.
•	Encrypts the hash using the private key ddd.
•	Stores the digital signature in a separate file (signature.sig).
3. Signature Verification (Decryption Code)
•	Computes SHA-256 hash for the received document.
•	Reads and decrypts the digital signature using the public key eee.
•	Compares the decrypted hash with the computed hash to verify authenticity.
Usage
1.	Encryption (Signing)
o	Run the encryption script to sign the document.
o	A signature file (.sig) will be generated.
2.	Decryption (Verification)
o	Run the decryption script with the document and signature file.
o	The script will confirm whether the document is authentic or tampered.
Requirements
•	Python 3
•	sympy library (for modular inverse calculation)

licensed by Achanta Saisathvik.
