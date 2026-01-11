"""
Language switcher component for top right corner
"""

import streamlit as st
from utils.translations import set_language, get_language

def render_language_switcher():
    """Render language switcher in top right corner"""
    # Initialize language if not set
    if 'language' not in st.session_state:
        st.session_state['language'] = 'en'
    
    current_lang = st.session_state.get('language', 'en')
    
    # Create columns to push to right
    col1, col2 = st.columns([10, 1])
    
    with col2:
        lang_options = {
            'English': 'en',
            'Hindi': 'hi'
        }
        
        # Get current selection index
        current_index = 0 if current_lang == 'en' else 1
        
        selected = st.selectbox(
            "🌐",
            options=list(lang_options.keys()),
            index=current_index,
            key="lang_switcher_select",
            label_visibility="collapsed"
        )
        
        selected_lang = lang_options[selected]
        
        # Update language if changed
        if selected_lang != current_lang:
            st.session_state['language'] = selected_lang
            st.rerun()
