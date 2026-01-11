"""
Find Help - Connect with healthcare professionals (demo listings)
"""

import streamlit as st

st.set_page_config(
    page_title="PCOS Health AI - Find Help",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Find Help")
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

# Nearby Gynecologists (Demo Data)
st.markdown("---")
st.markdown("### 🏥 Nearby Gynecologists (Demo Data)")

st.error("""
⚠️ **Disclaimer:** The following listings are demo/example data only. 
They are not endorsements. Please research and verify any healthcare provider independently.
""")

# Demo Listings
doctors = [
    {
        "name": "Dr. Sarah Johnson",
        "specialization": "Reproductive Health, PCOS",
        "location": "Downtown Medical Center",
        "distance": "2.5 miles"
    },
    {
        "name": "Dr. Maria Rodriguez",
        "specialization": "Women's Health, Endocrinology",
        "location": "City Health Clinic",
        "distance": "3.8 miles"
    },
    {
        "name": "Dr. Priya Patel",
        "specialization": "Gynecology, Hormonal Disorders",
        "location": "Community Hospital",
        "distance": "5.2 miles"
    },
    {
        "name": "Dr. Emily Chen",
        "specialization": "Reproductive Endocrinology",
        "location": "Women's Health Center",
        "distance": "6.1 miles"
    },
    {
        "name": "Dr. Jennifer Williams",
        "specialization": "Gynecology, PCOS Management",
        "location": "Regional Medical Center",
        "distance": "7.5 miles"
    }
]

for i, doctor in enumerate(doctors, 1):
    with st.expander(f"👩‍⚕️ {doctor['name']} - {doctor['distance']} away"):
        st.markdown(f"**Specialization:** {doctor['specialization']}")
        st.markdown(f"**Location:** {doctor['location']}")
        st.caption("🔗 Contact information available through healthcare directories")

# Location Input (Future Scope)
st.markdown("---")
st.markdown("### 📍 Find Doctors Near You")
location = st.text_input("Enter your city or ZIP code (Future feature)")
st.info("🚀 **Coming Soon:** Real-time location-based doctor search")

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
