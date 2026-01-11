"""
User Dashboard - Advanced analytics and insights
"""

import streamlit as st
from utils.auth import is_authenticated, get_current_user
from utils.language_switcher import render_language_switcher
from utils.community_storage import load_posts
from utils.ui_components import create_info_card, create_progress_card
from datetime import datetime, timedelta

st.set_page_config(
    page_title="PCOS Health AI - Dashboard",
    page_icon="📊",
    layout="wide"
)

# Language switcher
render_language_switcher()

# Check authentication
if not is_authenticated():
    st.warning("Please login to access your dashboard")
    if st.button("Go to Login"):
        st.switch_page("pages/0_🔐_Authentication.py")
    st.stop()

user = get_current_user()

st.title("Your Health Dashboard")
st.markdown(f"### Welcome back, {user['name']}!")

# Health Check History
st.markdown("---")
st.markdown("### Recent Health Checks")

if 'health_check_result' in st.session_state:
    result = st.session_state.get('health_check_result', {})
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Risk Level", result.get('risk_level', 'N/A'))
    
    with col2:
        st.metric("Risk Score", result.get('risk_score', 0))
    
    with col3:
        st.metric("Confidence", f"{result.get('confidence', 0)}%")
    
    with col4:
        st.metric("Pattern", result.get('pcos_type', 'N/A')[:20] + "..." if len(result.get('pcos_type', '')) > 20 else result.get('pcos_type', 'N/A'))
    
    # Visual progress indicators
    if 'signals' in result:
        signals = result['signals']
        st.markdown("### Signal Analysis")
        
        create_progress_card("Cycle Irregularity", signals.get('cycle', 0), 10, "#D9469F")
        create_progress_card("Stress Level", signals.get('stress', 0), 10, "#C77A9E")
        create_progress_card("Metabolic/Insulin", signals.get('insulin', 0), 10, "#9B7EDE")
        create_progress_card("Androgen Symptoms", signals.get('androgen', 0), 10, "#8B4A6B")
        create_progress_card("Inflammation", signals.get('inflammation', 0), 10, "#D9469F")
    
    if st.button("View Full Health Check"):
        st.switch_page("pages/2_🔍_Health_Check.py")
else:
    create_info_card(
        "No Health Check Yet",
        "Complete a health check to see your personalized dashboard with insights and recommendations.",
        "💡",
        "#D9469F"
    )
    if st.button("Start Health Check", type="primary"):
        st.switch_page("pages/2_🔍_Health_Check.py")

# Community Activity
st.markdown("---")
st.markdown("### Your Community Activity")

posts = load_posts()
user_posts = [p for p in posts if p.get('author_email') == user.get('email')]

if user_posts:
    st.metric("Your Posts", len(user_posts))
    st.markdown(f"You've shared {len(user_posts)} post(s) in the community")
    if st.button("View Community"):
        st.switch_page("pages/7_👥_Community.py")
else:
    st.info("You haven't posted in the community yet. Share your experiences to help others!")
    if st.button("Go to Community"):
        st.switch_page("pages/7_👥_Community.py")

# Quick Actions
st.markdown("---")
st.markdown("### Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📋 New Health Check", use_container_width=True, type="primary"):
        st.switch_page("pages/2_🔍_Health_Check.py")

with col2:
    if st.button("💬 AI Assistant", use_container_width=True):
        st.switch_page("pages/3_💬_AI_Assistant.py")

with col3:
    if st.button("👥 Community", use_container_width=True):
        st.switch_page("pages/7_👥_Community.py")

# Insights and Recommendations
st.markdown("---")
st.markdown("### Personalized Insights")

if 'health_check_result' in st.session_state:
    result = st.session_state.get('health_check_result', {})
    
    if result.get('doctor_needed'):
        create_info_card(
            "Medical Consultation Recommended",
            "Based on your health check, we recommend consulting with a healthcare professional. Download your report to share with your doctor.",
            "🩺",
            "#FF6B6B"
        )
    else:
        create_info_card(
            "Lifestyle Management",
            "Your current patterns suggest lifestyle-focused management may be appropriate. Check out your personalized lifestyle plan.",
            "🌱",
            "#4ECDC4"
        )
    
    if st.button("View Lifestyle Plan"):
        st.switch_page("pages/5_🌱_Lifestyle_Plan.py")
