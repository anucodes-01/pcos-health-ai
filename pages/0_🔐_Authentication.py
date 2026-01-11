"""
Authentication Page - Login and Registration
"""

import streamlit as st
from utils.auth import register_user, login_user, is_authenticated, logout_user
from utils.translations import t, get_language

st.set_page_config(
    page_title="PCOS Health AI - Authentication",
    page_icon="🔐",
    layout="centered"
)

# Initialize language if not set
if 'language' not in st.session_state:
    st.session_state['language'] = 'en'

# If already authenticated, redirect
if is_authenticated():
    st.success(f"Welcome, {st.session_state['user']['name']}!")
    if st.button("Go to Home"):
        st.switch_page("pages/1_🏠_Home.py")
    if st.button("Logout"):
        logout_user()
        st.rerun()
    st.stop()

# Tab selection
tab1, tab2 = st.tabs(["Login", "Register"])

# Login Tab
with tab1:
    st.markdown("### Login to Your Account")
    
    with st.form("login_form"):
        email = st.text_input("Email", placeholder="your.email@example.com")
        password = st.text_input("Password", type="password")
        submit_login = st.form_submit_button("Login", type="primary")
        
        if submit_login:
            if email and password:
                success, message, user_data = login_user(email, password)
                if success:
                    st.session_state['authenticated'] = True
                    st.session_state['user'] = user_data
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.warning("Please fill in all fields")

# Registration Tab
with tab2:
    st.markdown("### Create New Account")
    
    with st.form("register_form"):
        name = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="your.email@example.com")
        phone = st.text_input("Phone Number", placeholder="+91 1234567890")
        password = st.text_input("Password", type="password", help="Minimum 6 characters")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit_register = st.form_submit_button("Register", type="primary")
        
        if submit_register:
            if not all([name, email, phone, password, confirm_password]):
                st.warning("Please fill in all fields")
            elif password != confirm_password:
                st.error("Passwords do not match")
            else:
                success, message = register_user(email, phone, password, name)
                if success:
                    st.success(message)
                    st.info("You can now login with your credentials")
                else:
                    st.error(message)
