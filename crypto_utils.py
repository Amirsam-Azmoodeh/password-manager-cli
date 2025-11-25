from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

KEY = os.getenv("KEY") # Get encryption key from environment (secure way)
fernet = Fernet(KEY.encode())

def encrypt_password(password) :
    return fernet.encrypt(password.encode())

def decrypt_password(token) :
    return fernet.decrypt(token).decode()

