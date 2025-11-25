# generate_key.py
from cryptography.fernet import Fernet

# Generate a REAL, VALID Fernet key
key = Fernet.generate_key()
print("COPY THIS EXACT LINE TO YOUR .env FILE:")
print(key.decode())