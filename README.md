# Genryptor

Genryptor is a Django web application for generating passwords and encrypting
them with a user-provided secret key. Encrypted entries can be saved locally,
searched by account name, and decrypted later with the same key.

This is a personal, educational project exploring Django and symmetric
encryption. It is not intended to replace a production password manager.

## Features

- Generate passwords with a configurable length
- Encrypt passwords using Fernet symmetric encryption
- Derive encryption keys with PBKDF2-HMAC-SHA256
- Save encrypted entries in a local SQLite database
- Search saved entries by account name
- Decrypt entries using the original secret key

## Tech stack

- Python 3.12+
- Django 6
- `cryptography`
- SQLite
- HTML and CSS

## Local setup

1. Clone the repository:

   ```bash
   git clone https://github.com/imaadShadab/Genryptor.git
   cd Genryptor
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create your local environment file:

   **Windows PowerShell**

   ```powershell
   Copy-Item .env.example .env
   ```

   **macOS/Linux**

   ```bash
   cp .env.example .env
   ```

5. Generate a Django secret key:

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

   Replace the placeholder value in `.env` with the generated key.

6. Create the local database:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open <http://127.0.0.1:8000/> in your browser.

## Project structure

```text
.
├── core/                  # Django project settings and URL configuration
├── encryptor/             # Application views, models, templates, and static files
├── .env.example           # Environment variable template
├── manage.py              # Django command-line utility
└── requirements.txt       # Python dependencies
```

## Security notes

- `.env` and `db.sqlite3` are intentionally excluded from Git.
- The secret used to encrypt an entry is not stored by the application.
- Anyone with access to the running application can currently view the list of
  encrypted entries because user authentication has not been implemented.
- The current password generator and key-derivation configuration are
  educational implementations and have not received a security audit.
- Do not store real or sensitive credentials in this project.

## Running checks

```bash
python manage.py check
python manage.py test
```

## Contributing

Suggestions and pull requests are welcome. For substantial changes, open an
issue first to discuss the proposed improvement.
