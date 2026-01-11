"""
Language switcher component for top right corner
"""

import streamlit as st
from utils.translations import set_language, get_language

def render_language_switcher():
    """Render language switcher in top right corner"""
    current_lang = get_language()
    
    # Create columns to push to right
    col1, col2 = st.columns([10, 1])
    
    with col2:
        lang_options = {
            'English': 'en',
            'Hindi': 'hi'
        }
        
        selected = st.selectbox(
            "🌐",
            options=list(lang_options.keys()),
            index=0 if current_lang == 'en' else 1,
            key="lang_switcher",
            label_visibility="collapsed"
        )
        
        if lang_options[selected] != current_lang:
            set_language(lang_options[selected])
            st.rerun()
