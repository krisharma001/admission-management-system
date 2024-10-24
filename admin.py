import os
import hashlib
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_admin_credentials():
    return {
        'username': os.getenv('ADMIN_USERNAME'),
        'password_hash': os.getenv('ADMIN_PASSWORD_HASH')
    }

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def admin_login(username, password):
    admin_creds = get_admin_credentials()
    
    if not admin_creds['username'] or not admin_creds['password_hash']:
        raise ValueError("Admin credentials are not properly set in the environment variables.")
    
    return username == admin_creds['username'] and hash_password(password) == admin_creds['password_hash']

# def setup_admin_credentials(username, password):
#     password_hash = hash_password(password)
#     print(f"ADMIN_USERNAME={username}")
#     print(f"ADMIN_PASSWORD_HASH={password_hash}")
#     print("Add these to your .env file")

# setup_admin_credentials('root', 'app@project')
