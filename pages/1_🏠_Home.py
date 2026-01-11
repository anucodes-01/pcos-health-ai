"""
Home Page - Trust-building, clear value proposition, calm entry point
"""

import streamlit as st

st.set_page_config(
    page_title="PCOS Health AI - Home",
    page_icon="🏠",
    layout="wide"
)

# Hero Section
st.title("PCOS Health AI")
st.markdown("### A Safe, Explainable Women's Health Companion")
st.markdown("**Understand • Decide • Feel Supported**")

st.markdown("---")

# What We Do / Don't Do
st.markdown("### 📋 What This Tool Does")
col1, col2 = st.columns(2)

with col1:
    st.success("""
    ### ✅ What This Tool DOES
    
    - **Helps you understand** your body signals
    - **Reduces confusion** and anxiety
    - **Guides you** on when to see a doctor
    - **Provides structured** education
    - **Offers lifestyle** guidance
    - **Generates doctor-ready** summaries
    - **Supports you** emotionally
    """)

with col2:
    st.warning("""
    ### ❌ What This Tool DOES NOT Do
    
    - ❌ Provide medical diagnosis
    - ❌ Prescribe medications
    - ❌ Replace healthcare professionals
    - ❌ Store your personal data
    - ❌ Make medical claims
    """)

st.markdown("---")

# Feature Cards
st.markdown("### 🎯 Explore Our Features")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background-color: #E8D5FF; text-align: center; min-height: 150px;'>
        <h2>🔍</h2>
        <h4>Health Check</h4>
        <p>Structured assessment of your health patterns</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Health Check", key="home_hc", use_container_width=True):
        st.switch_page("pages/2_🔍_Health_Check.py")

with col2:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background-color: #FFD5E5; text-align: center; min-height: 150px;'>
        <h2>💬</h2>
        <h4>AI Assistant</h4>
        <p>Guided conversation for clarification</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to AI Assistant", key="home_ai", use_container_width=True):
        st.switch_page("pages/3_💬_AI_Assistant.py")

with col3:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background-color: #D5FFE8; text-align: center; min-height: 150px;'>
        <h2>📚</h2>
        <h4>Learn Conditions</h4>
        <p>Educational content about PCOS, PCOD, Endometriosis</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Learn More", key="home_learn", use_container_width=True):
        st.switch_page("pages/4_📚_Learn_Conditions.py")

with col4:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background-color: #FFE8D5; text-align: center; min-height: 150px;'>
        <h2>👥</h2>
        <h4>Community</h4>
        <p>Safe space for support and sharing</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Visit Community", key="home_comm", use_container_width=True):
        st.switch_page("pages/7_👥_Community.py")

st.markdown("---")

# Video Section (placeholder)
st.markdown("### 📹 How It Works")
st.info("""
🚀 **Video coming soon!** In the meantime, explore our features above to learn more about how PCOS Health AI works.
""")

# CTA Buttons
st.markdown("---")
st.markdown("### 🚀 Get Started")
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Start Health Check", type="primary", use_container_width=True, key="cta_hc"):
        st.switch_page("pages/2_🔍_Health_Check.py")

with col2:
    if st.button("💬 Talk to AI Assistant", use_container_width=True, key="cta_ai"):
        st.switch_page("pages/3_💬_AI_Assistant.py")

# Disclaimer Banner
st.markdown("---")
st.error("""
⚠️ **Disclaimer:** This tool is for awareness and support only. It does not provide medical diagnosis. 
Always consult healthcare professionals for medical advice.
""")
