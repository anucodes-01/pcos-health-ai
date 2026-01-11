"""
Home Page - Trust-building, clear value proposition, calm entry point
"""

import streamlit as st
from utils.auth import is_authenticated, get_current_user, logout_user
from utils.language_switcher import render_language_switcher
from utils.translations import t, get_language

st.set_page_config(
    page_title="PCOS Health AI - Home",
    page_icon="🏠",
    layout="wide"
)

# Initialize language
if 'language' not in st.session_state:
    st.session_state['language'] = 'en'

# Language switcher
render_language_switcher()

# Authentication status
col1, col2, col3 = st.columns([8, 1, 1])
with col1:
    if is_authenticated():
        user = get_current_user()
        st.markdown(f"**{t('welcome')}, {user['name']}!**")
with col2:
    if is_authenticated():
        if st.button(t('logout'), use_container_width=True):
            logout_user()
            st.rerun()
    else:
        if st.button(t('login'), use_container_width=True):
            st.switch_page("pages/0_🔐_Authentication.py")

# Hero Section
st.title("PCOS Health AI")
st.markdown("### A Safe, Explainable Women's Health Companion")
st.markdown("**Understand • Decide • Feel Supported**")

st.markdown("---")

# What We Do / Don't Do
st.markdown("### What This Tool Does")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background: linear-gradient(135deg, #FFE5F1 0%, #F8E8F0 100%); border-left: 4px solid #D9469F;'>
        <h3 style='color: #8B4A6B; margin-top: 0;'>What This Tool Does</h3>
        <ul style='color: #2D1B3D;'>
            <li><strong>Helps you understand</strong> your body signals</li>
            <li><strong>Reduces confusion</strong> and anxiety</li>
            <li><strong>Guides you</strong> on when to see a doctor</li>
            <li><strong>Provides structured</strong> education</li>
            <li><strong>Offers lifestyle</strong> guidance</li>
            <li><strong>Generates doctor-ready</strong> summaries</li>
            <li><strong>Supports you</strong> emotionally</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background: linear-gradient(135deg, #FFF0F5 0%, #FFE5F1 100%); border-left: 4px solid #C77A9E;'>
        <h3 style='color: #8B4A6B; margin-top: 0;'>What This Tool Does Not Do</h3>
        <ul style='color: #2D1B3D;'>
            <li>Provide medical diagnosis</li>
            <li>Prescribe medications</li>
            <li>Replace healthcare professionals</li>
            <li>Store your personal data</li>
            <li>Make medical claims</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Feature Cards
st.markdown("### Explore Our Features")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style='padding: 24px; border-radius: 12px; background: linear-gradient(135deg, #F8E8F0 0%, #FFE5F1 100%); text-align: center; min-height: 180px; box-shadow: 0 2px 8px rgba(217, 70, 159, 0.1); border: 1px solid #FFD5E5;'>
        <h3 style='color: #D9469F; margin-top: 0;'>Health Check</h3>
        <p style='color: #2D1B3D;'>Structured assessment of your health patterns</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Health Check", key="home_hc", use_container_width=True):
        st.switch_page("pages/2_🔍_Health_Check.py")

with col2:
    st.markdown("""
    <div style='padding: 24px; border-radius: 12px; background: linear-gradient(135deg, #FFE5F1 0%, #F8E8F0 100%); text-align: center; min-height: 180px; box-shadow: 0 2px 8px rgba(217, 70, 159, 0.1); border: 1px solid #FFD5E5;'>
        <h3 style='color: #D9469F; margin-top: 0;'>AI Assistant</h3>
        <p style='color: #2D1B3D;'>Guided conversation for clarification</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to AI Assistant", key="home_ai", use_container_width=True):
        st.switch_page("pages/3_💬_AI_Assistant.py")

with col3:
    st.markdown("""
    <div style='padding: 24px; border-radius: 12px; background: linear-gradient(135deg, #F0E5F5 0%, #F8E8F0 100%); text-align: center; min-height: 180px; box-shadow: 0 2px 8px rgba(217, 70, 159, 0.1); border: 1px solid #E8D5F0;'>
        <h3 style='color: #D9469F; margin-top: 0;'>Learn Conditions</h3>
        <p style='color: #2D1B3D;'>Educational content about PCOS, PCOD, Endometriosis</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Learn More", key="home_learn", use_container_width=True):
        st.switch_page("pages/4_📚_Learn_Conditions.py")

with col4:
    st.markdown("""
    <div style='padding: 24px; border-radius: 12px; background: linear-gradient(135deg, #FFE5F1 0%, #F0E5F5 100%); text-align: center; min-height: 180px; box-shadow: 0 2px 8px rgba(217, 70, 159, 0.1); border: 1px solid #FFD5E5;'>
        <h3 style='color: #D9469F; margin-top: 0;'>Community</h3>
        <p style='color: #2D1B3D;'>Safe space for support and sharing</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Visit Community", key="home_comm", use_container_width=True):
        st.switch_page("pages/7_👥_Community.py")

st.markdown("---")

# How It Works Section
st.markdown("---")
st.markdown("### How It Works")
st.markdown("""
<div style='padding: 24px; border-radius: 12px; background: linear-gradient(135deg, #FFF5F8 0%, #F8E8F0 100%); border-left: 4px solid #D9469F;'>
    <p style='color: #2D1B3D; margin: 0;'>Our platform uses explainable AI to help you understand your health patterns. 
    Start with a comprehensive health check, get personalized insights, and access educational resources 
    to make informed decisions about your health.</p>
</div>
""", unsafe_allow_html=True)

# CTA Buttons
st.markdown("---")
st.markdown("### Get Started")
col1, col2 = st.columns(2)

with col1:
    if st.button("Start Health Check", type="primary", use_container_width=True, key="cta_hc"):
        st.switch_page("pages/2_🔍_Health_Check.py")

with col2:
    if st.button("Talk to AI Assistant", use_container_width=True, key="cta_ai"):
        st.switch_page("pages/3_💬_AI_Assistant.py")

# Disclaimer Banner
st.markdown("---")
st.markdown("""
<div style='padding: 16px; border-radius: 8px; background-color: #FFE5F1; border-left: 4px solid #D9469F;'>
    <p style='color: #8B4A6B; margin: 0;'><strong>Disclaimer:</strong> This tool is for awareness and support only. 
    It does not provide medical diagnosis. Always consult healthcare professionals for medical advice.</p>
</div>
""", unsafe_allow_html=True)
