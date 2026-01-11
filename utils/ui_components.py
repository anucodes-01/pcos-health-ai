"""
Advanced UI components for the application
"""

import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

def render_header_with_auth():
    """Render header with authentication status and language switcher"""
    from utils.auth import is_authenticated, get_current_user, logout_user
    from utils.language_switcher import render_language_switcher
    
    # Top bar with auth and language
    col1, col2, col3 = st.columns([8, 1, 1])
    
    with col1:
        if is_authenticated():
            user = get_current_user()
            st.markdown(f"**Welcome, {user['name']}!**")
    
    with col2:
        if is_authenticated():
            if st.button("Logout", use_container_width=True):
                logout_user()
                st.rerun()
        else:
            if st.button("Login", use_container_width=True):
                st.switch_page("pages/0_🔐_Authentication.py")
    
    with col3:
        render_language_switcher()

def create_progress_card(title, value, max_value, color="#D9469F"):
    """Create a progress card visualization"""
    percentage = min((value / max_value) * 100, 100)
    
    st.markdown(f"""
    <div style='padding: 20px; border-radius: 12px; background: linear-gradient(135deg, #FFF5F8 0%, #F8E8F0 100%); 
                border-left: 4px solid {color}; margin-bottom: 15px;'>
        <h4 style='color: {color}; margin-top: 0;'>{title}</h4>
        <div style='background-color: #E8D5F0; border-radius: 8px; height: 25px; margin: 10px 0;'>
            <div style='background-color: {color}; height: 25px; width: {percentage}%; border-radius: 8px; 
                        display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;'>
                {value}/{max_value} ({percentage:.1f}%)
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_info_card(title, content, icon="ℹ️", color="#D9469F"):
    """Create an information card"""
    st.markdown(f"""
    <div style='padding: 20px; border-radius: 12px; background: linear-gradient(135deg, #FFF5F8 0%, #F8E8F0 100%); 
                border-left: 4px solid {color}; margin-bottom: 15px;'>
        <h4 style='color: {color}; margin-top: 0;'>{icon} {title}</h4>
        <p style='color: #2D1B3D;'>{content}</p>
    </div>
    """, unsafe_allow_html=True)

def create_stats_dashboard(stats_dict):
    """Create a statistics dashboard"""
    cols = st.columns(len(stats_dict))
    
    for idx, (key, value) in enumerate(stats_dict.items()):
        with cols[idx]:
            st.metric(
                label=key,
                value=value
            )

def render_navigation_menu():
    """Render navigation menu"""
    pages = [
        ("Home", "pages/1_🏠_Home.py"),
        ("Health Check", "pages/2_🔍_Health_Check.py"),
        ("AI Assistant", "pages/3_💬_AI_Assistant.py"),
        ("Learn Conditions", "pages/4_📚_Learn_Conditions.py"),
        ("Lifestyle Plan", "pages/5_🌱_Lifestyle_Plan.py"),
        ("Trackers", "pages/6_📊_Trackers.py"),
        ("Community", "pages/7_👥_Community.py"),
        ("Find Help", "pages/8_🩺_Find_Help.py"),
        ("Resources & FAQ", "pages/9_📖_Resources_FAQ.py")
    ]
    
    st.sidebar.markdown("### Navigation")
    for page_name, page_path in pages:
        if st.sidebar.button(page_name, use_container_width=True, key=f"nav_{page_name}"):
            st.switch_page(page_path)
