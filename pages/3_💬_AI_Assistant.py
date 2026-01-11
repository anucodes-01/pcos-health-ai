"""
AI Health Assistant - Guided chatbot for clarification & emotional support
"""

import streamlit as st
from utils.chat_engine import generate_response
from utils.prompt_library import get_questions_for_category

st.set_page_config(
    page_title="PCOS Health AI - AI Assistant",
    page_icon="💬",
    layout="wide"
)

st.title("💬 AI Health Assistant")
st.markdown("### Guided Conversation for Clarification & Support")

# Initialize session state
if 'chat_step' not in st.session_state:
    st.session_state.chat_step = 1
if 'age_group' not in st.session_state:
    st.session_state.age_group = None
if 'concern_category' not in st.session_state:
    st.session_state.concern_category = None
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Step 1: Age Group Selection
if st.session_state.chat_step == 1:
    st.markdown("### Step 1: Tell us about yourself")
    st.markdown("Select your age group:")
    
    age_groups = ["Teenager (13-18)", "Young Adult (19-30)", "Adult (31-45)"]
    
    selected_age = st.radio("Age Group", age_groups, key="age_select")
    
    if st.button("Continue", type="primary"):
        st.session_state.age_group = selected_age.split("(")[0].strip().lower().replace(" ", "_")
        st.session_state.chat_step = 2
        st.rerun()

# Step 2: Concern Category
elif st.session_state.chat_step == 2:
    st.markdown("### Step 2: What would you like to discuss?")
    
    categories = {
        "Menstrual Issues": "menstrual",
        "Pain & Discomfort": "pain",
        "Hormonal Changes": "hormonal",
        "Mood & Mental Health": "mood",
        "Weight & Metabolism": "weight",
        "Other Concerns": "other"
    }
    
    selected_category = st.radio(
        "Category",
        list(categories.keys()),
        key="category_select"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back"):
            st.session_state.chat_step = 1
            st.rerun()
    with col2:
        if st.button("Continue", type="primary"):
            st.session_state.concern_category = categories[selected_category]
            st.session_state.chat_step = 3
            st.rerun()

# Step 3: Guided Questions
elif st.session_state.chat_step == 3:
    st.markdown("### Step 3: Answer a few questions")
    
    questions = get_questions_for_category(
        st.session_state.age_group,
        st.session_state.concern_category,
        limit=5
    )
    
    for i, q in enumerate(questions):
        if q.get('type') == 'radio':
            answer = st.radio(q['text'], q['options'], key=f"q_{i}")
        elif q.get('type') == 'selectbox':
            answer = st.selectbox(q['text'], q['options'], key=f"q_{i}")
        elif q.get('type') == 'slider':
            answer = st.slider(q['text'], q['options'][0], q['options'][1], key=f"q_{i}")
        else:
            answer = st.text_input(q['text'], key=f"q_{i}")
        
        st.session_state.answers[q['id']] = answer
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back"):
            st.session_state.chat_step = 2
            st.rerun()
    with col2:
        if st.button("Get Response", type="primary"):
            st.session_state.chat_step = 4
            st.rerun()

# Step 4: Response
elif st.session_state.chat_step == 4:
    st.markdown("### Step 4: Here's what we found")
    
    response = generate_response(
        st.session_state.age_group,
        st.session_state.concern_category,
        st.session_state.answers
    )
    
    st.info(response['clarification'])
    
    if response.get('is_normal') is not None:
        if response['is_normal']:
            st.success("✅ This is within the range of normal variation.")
        else:
            st.warning("⚠️ This may warrant further attention.")
    
    st.markdown("### Next Steps")
    for step in response['next_steps']:
        st.markdown(f"- {step}")
    
    if response.get('suggest_health_check'):
        st.markdown("---")
        if st.button("🔍 Take Full Health Check", type="primary", use_container_width=True):
            st.switch_page("pages/2_🔍_Health_Check.py")
    
    st.markdown("---")
    if st.button("🔄 Start New Conversation", use_container_width=True):
        # Reset session state
        for key in ['chat_step', 'age_group', 'concern_category', 'answers']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# Disclaimer
st.markdown("---")
st.info("⚠️ This assistant provides guidance only. It does not diagnose conditions.")
