"""
Authentication system for user registration, login, and logout
Uses email and phone number for authentication
"""

import streamlit as st
import hashlib
import json
import os
from pathlib import Path

# File to store user data (simple JSON-based storage)
USERS_FILE = "data/users.json"

def init_users_file():
    """Initialize users file if it doesn't exist"""
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump({}, f)

def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Load users from JSON file"""
    init_users_file()
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    """Save users to JSON file"""
    init_users_file()
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def register_user(email, phone, password, name):
    """
    Register a new user
    
    Args:
        email: User email
        phone: User phone number
        password: User password
        name: User name
    
    Returns:
        tuple: (success: bool, message: str)
    """
    users = load_users()
    
    # Validate email format
    if '@' not in email or '.' not in email.split('@')[1]:
        return False, "Invalid email format"
    
    # Validate phone (basic check)
    if not phone or len(phone) < 10:
        return False, "Invalid phone number"
    
    # Validate password
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    
    # Check if user already exists
    if email in users:
        return False, "Email already registered"
    
    # Check if phone already exists
    for user_email, user_data in users.items():
        if user_data.get('phone') == phone:
            return False, "Phone number already registered"
    
    # Create new user
    users[email] = {
        'email': email,
        'phone': phone,
        'password_hash': hash_password(password),
        'name': name,
        'created_at': str(Path(USERS_FILE).stat().st_mtime) if os.path.exists(USERS_FILE) else ""
    }
    
    save_users(users)
    return True, "Registration successful!"

def login_user(email, password):
    """
    Login user
    
    Args:
        email: User email
        password: User password
    
    Returns:
        tuple: (success: bool, message: str, user_data: dict or None)
    """
    users = load_users()
    
    if email not in users:
        return False, "Email not found", None
    
    user = users[email]
    
    if user['password_hash'] != hash_password(password):
        return False, "Incorrect password", None
    
    # Return user data (without password hash)
    user_data = {
        'email': user['email'],
        'phone': user['phone'],
        'name': user.get('name', 'User')
    }
    
    return True, "Login successful!", user_data

def logout_user():
    """Logout current user"""
    if 'user' in st.session_state:
        del st.session_state['user']
    if 'authenticated' in st.session_state:
        st.session_state['authenticated'] = False

def is_authenticated():
    """Check if user is authenticated"""
    return st.session_state.get('authenticated', False) and 'user' in st.session_state

def get_current_user():
    """Get current authenticated user"""
    if is_authenticated():
        return st.session_state.get('user')
    return None
