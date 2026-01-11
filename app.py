"""
PCOS Health AI - Main Entry Point
A Safe, Explainable Women's Health Companion

This is the main entry point for the Streamlit multi-page application.
Streamlit automatically creates navigation from the pages/ directory.
"""

import streamlit as st

st.set_page_config(
    page_title="PCOS Health AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page content (redirects to Home)
st.title("PCOS Health AI")
st.markdown("### A Safe, Explainable Women's Health Companion")

st.markdown("""
Welcome to PCOS Health AI - your safe space for understanding your body signals, 
reducing confusion, and making informed decisions about your health.

**Navigate using the sidebar menu to explore our features:**
- 🏠 **Home** - Overview and getting started
- 🔍 **Health Check** - Structured health assessment
- 💬 **AI Assistant** - Guided conversation for clarification
- 📚 **Learn Conditions** - Educational content
- 🌱 **Lifestyle Plan** - Personalized guidance
- 📊 **Trackers** - Symptom and cycle tracking
- 👥 **Community** - Support and sharing space
- 🩺 **Find Help** - Connect with healthcare professionals
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Go to Home", type="primary", use_container_width=True):
        st.switch_page("pages/1_🏠_Home.py")

with col2:
    if st.button("🔍 Start Health Check", use_container_width=True):
        st.switch_page("pages/2_🔍_Health_Check.py")

st.markdown("---")
st.error("""
⚠️ **Disclaimer:** This tool is for awareness and support only. 
It does not provide medical diagnosis. Always consult healthcare professionals for medical advice.
""")
