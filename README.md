# Genryptor

Genryptor is a Django-based password management application that combines password generation and encryption into a single platform. Users can generate strong random passwords, encrypt them using a personal secret key, store encrypted credentials, and decrypt them later when needed.

## Features

* Generate secure random passwords of custom lengths
* Encrypt passwords using Fernet symmetric encryption
* Derive encryption keys securely with PBKDF2-HMAC-SHA256
* Store encrypted credentials in a database
* Decrypt stored passwords using the correct secret key
* Search and filter saved accounts

## Built With

* Python
* Django
* Cryptography (Fernet)
* SQLite (default Django database)

Genryptor is designed as a simple and lightweight tool for learning about password management, encryption, and web application development with Django.
