"""
Find Help - Connect with healthcare professionals with location-based search
"""

import streamlit as st
from utils.doctors_data import get_doctors_by_location
from utils.translations import t, get_language
from utils.language_switcher import render_language_switcher

st.set_page_config(
    page_title="PCOS Health AI - Find Help",
    page_icon="🩺",
    layout="wide"
)

# Initialize language
if 'language' not in st.session_state:
    st.session_state['language'] = 'en'

# Language switcher
render_language_switcher()

st.title("Find Help")
st.markdown("### Connect with Healthcare Professionals")

# When to See a Doctor Section
st.markdown("### 🚨 When to See a Doctor")

col1, col2 = st.columns(2)

with col1:
    st.error("""
    **Seek immediate medical attention if you experience:**
    - Severe pelvic pain
    - Heavy bleeding that soaks through pads/tampons hourly
    - Signs of infection (fever, unusual discharge)
    - Severe mood changes or thoughts of self-harm
    """)

with col2:
    st.warning("""
    **Schedule an appointment if you experience:**
    - Irregular periods for 3+ months
    - Persistent symptoms affecting daily life
    - Concerns about fertility
    - Unexplained weight changes
    - New or worsening symptoms
    """)

# Location Input
st.markdown("---")
st.markdown("### Find Doctors Near You")
location = st.text_input(
    "Enter your city name (e.g., Mumbai, Delhi, Bangalore)",
    placeholder="Enter city name",
    key="doctor_location"
)

# Get doctors based on location
if location:
    doctors = get_doctors_by_location(location)
    
    st.markdown("---")
    st.markdown(f"### Nearby Doctors in {location.title()}")
    
    st.markdown("""
    <div style='padding: 12px; border-radius: 8px; background-color: #FFE5F1; border-left: 4px solid #D9469F; margin-bottom: 20px;'>
        <p style='color: #8B4A6B; margin: 0;'><strong>Disclaimer:</strong> The following listings are demo/example data only. 
        They are not endorsements. Please research and verify any healthcare provider independently.</p>
    </div>
    """, unsafe_allow_html=True)
    
    for i, doctor in enumerate(doctors, 1):
        with st.expander(f"{doctor['name']} - {doctor['distance']} away | Rating: {doctor.get('rating', 'N/A')}"):
            st.markdown(f"**Specialization:** {doctor['specialization']}")
            st.markdown(f"**Location:** {doctor['location']}")
            if 'phone' in doctor:
                st.markdown(f"**Contact:** {doctor['phone']}")
            if 'rating' in doctor:
                st.markdown(f"**Rating:** {doctor['rating']}/5.0")
            st.caption("Contact information available through healthcare directories")
else:
    st.info("Enter a city name above to find nearby doctors")

# Teleconsult Options
st.markdown("---")
st.markdown("### 💻 Teleconsult Options")

st.markdown("""
**Consider teleconsultation for:**
- Initial consultations
- Follow-up visits
- Non-urgent concerns
- Accessibility needs

**Popular Teleconsult Platforms:**
- Platform 1 - General healthcare (research independently)
- Platform 2 - Specialized women's health (research independently)
- Platform 3 - Endocrinology focus (research independently)

*Note: Verify platform credentials and your insurance coverage.*
""")

# Preparation Tips
st.markdown("---")
st.markdown("### 📋 Preparing for Your Appointment")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **What to Bring:**
    - List of symptoms and concerns
    - Medication list (if any)
    - Previous test results
    - Health Check summary (download from Health Check page)
    - Questions you want to ask
    """)

with col2:
    st.markdown("""
    **Questions to Ask:**
    - What tests might be helpful?
    - What are my treatment options?
    - What lifestyle changes are recommended?
    - When should I follow up?
    - Are there specialists I should see?
    """)

# Self-Advocacy Tips
st.markdown("### 💪 Advocating for Yourself")

st.markdown("""
- **Be specific** about your symptoms and how they affect you
- **Bring notes** - it's easy to forget details during appointments
- **Ask for clarification** if something isn't clear
- **Get a second opinion** if you don't feel heard
- **Trust your instincts** - you know your body best
""")

# Link to Health Check Report
if 'health_check_result' in st.session_state:
    st.markdown("---")
    st.info("💡 **Tip:** Download your Health Check summary to bring to your appointment.")
    if st.button("📄 Go to Health Check Report", type="primary", use_container_width=True):
        st.switch_page("pages/2_🔍_Health_Check.py")

# Disclaimer
st.markdown("---")
st.error("""
⚠️ **Important Disclaimer:** 
- Demo listings are examples only, not endorsements
- Always verify healthcare provider credentials
- Research and choose providers that are right for you
- In emergencies, call emergency services immediately
""")
