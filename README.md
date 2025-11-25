# Password Manager CLI  
**A Secure Command-Line Password Manager**

## Project Overview

This is a fully functional, secure, and modular command-line password manager written in Python. It uses:
- **Fernet (symmetric encryption) from `cryptography` library
- SQLite for local, persistent storage
- Environment variables (.env) for secure key management

No passwords are stored in plain text.  
The encryption key is never hardcoded and is loaded securely from a `.env` file.



## Features

add -> Add a new service, username, and encrypted password |
get -> Retrieve and decrypt password by service & username |
list -> List all stored entries with decrypted passwords |
delete -> Remove entries by username |
help -> Show command guide |
exit -> Graceful shutdown |

## Files 

main.py → Main program
crypto_utils.py → Encryption
db_manager.py → Database
.env → Secret key (do not upload!)

---------------------------------------------------------------------------------

Amirsam Azmoodeh
TVTO Certified | Faradars | FreeCodeCamp

GitHub = https://github.com/Amirsam-Azmoodeh
LinkedIn = https://www.linkedin.com/in/amirsam-azmoodeh-2b9726364
email = amirsamazmoodeh@gmail.com
