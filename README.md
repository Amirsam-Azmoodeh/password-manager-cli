# Password Manager CLI
#### Video Demo: <https://youtu.be/your_video_url>
#### Description:

## Project Overview
This is a secure, command-line password manager written in Python. The program allows users to store, retrieve, list, and delete passwords for various online services. All passwords are encrypted using the Fernet symmetric encryption from the cryptography library before being stored in a local SQLite database. The encryption key is stored securely in a .env file using environment variables, ensuring that the key is never hardcoded in the source code.

## Features and Functionality
The application provides six main commands:

**add**: This command allows users to add a new password entry. The program prompts for the service name, username, and password. The password is immediately encrypted using Fernet and then stored in the database along with the service and username.

**get**: Users can retrieve a stored password by providing the service name and username. The program searches the database and if found, decrypts the password and displays it along with the entry's ID.

**list**: This command displays all stored password entries. The program fetches all records from the database and decrypts each password before displaying the complete list with IDs, service names, usernames, and passwords.

**delete**: Users can delete an entry by providing the username. All entries with that username will be removed from the database.

**help**: Displays a summary of all available commands and their usage.

**exit**: Gracefully terminates the program.

## Technical Implementation
The project is structured into three main modules:

**crypto_utils.py**: This module handles all encryption and decryption operations. It uses the Fernet symmetric encryption algorithm from the cryptography library. The module loads the encryption key from environment variables using python-dotenv, ensuring secure key management. The encrypt_password function takes a plain text password and returns encrypted bytes, while decrypt_password takes encrypted bytes and returns the original plain text password.

**db_manager.py**: This module manages all database operations using SQLite. It provides functions for adding, retrieving, deleting, and listing password entries. The database connection is handled using context managers (with statements) to ensure proper resource management. The database schema includes an auto-incrementing ID, service name, username, and encrypted password.

**main.py**: This is the main entry point of the application. It implements a command-line interface with a loop that continuously accepts user commands. The main function coordinates between the user input and the other modules. Each command is wrapped in try-except blocks for robust error handling.

## Testing Strategy
The project includes comprehensive unit tests in test_project.py using pytest. The test suite covers:

- **Encryption tests**: Verify that encryption and decryption work correctly, that encrypted data is in bytes format, and that the encryption key exists in environment variables.

- **Database tests**: Test adding, retrieving, deleting, and listing entries using a temporary database fixture to avoid affecting the production database.

- **Command handler tests**: Use mocking to test the add, get, and delete command handlers without actually interacting with the database or encryption functions.

- **Edge cases**: Test scenarios like retrieving non-existent entries, handling empty lists, and ensuring proper error messages are displayed.

## Design Decisions and Challenges

**Why SQLite?** SQLite was chosen for its simplicity and zero-configuration setup. It's lightweight and perfect for a local password manager that doesn't require a separate database server.

**Why Fernet?** Fernet provides symmetric encryption with built-in authentication, ensuring both confidentiality and integrity of the stored passwords. It's part of the cryptography library, which is well-maintained and secure.

**Why environment variables?** Storing the encryption key in a .env file prevents hardcoding sensitive information in the source code. This is a security best practice and allows users to easily change their key without modifying the code.

**Error handling**: All user interactions are wrapped in try-except blocks to provide friendly error messages instead of cryptic tracebacks. This improves user experience and makes the program more robust.

## Future Improvements
Potential enhancements for the future include:
- Adding password generation functionality
- Implementing master password protection
- Adding export/import capabilities
- Creating a graphical user interface
- Supporting multiple users with different encryption keys

## Installation and Usage
To use this password manager:

1. Install dependencies: `pip install -r requirements.txt`
2. Create a .env file with your encryption key: `KEY=your_generated_key`
3. Run the program: `python main.py`
4. Use the available commands to manage your passwords

## Conclusion
This password manager demonstrates secure password storage practices, modular code organization, comprehensive testing, and a user-friendly command-line interface. It meets all the requirements for the CS50P final project while providing practical functionality for everyday use.

---

Created by Amirsam Azmoodeh
GitHub: https://github.com/Amirsam-Azmoodeh
LinkedIn: https://www.linkedin.com/in/amirsam-azmoodeh-2b9726364
Email: amirsamazmoodeh@gmail.com
