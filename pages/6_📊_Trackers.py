"""
Trackers - Basic symptom and cycle tracking (session-based only)
"""

import streamlit as st
from datetime import date

st.set_page_config(
    page_title="PCOS Health AI - Trackers",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Trackers")
st.markdown("### Basic Symptom & Cycle Tracking")

# Initialize session state
if 'period_logs' not in st.session_state:
    st.session_state.period_logs = []
if 'cycle_notes' not in st.session_state:
    st.session_state.cycle_notes = {}

# Period Tracker Section
st.markdown("### 📅 Period Tracker")
st.caption("Track your menstrual cycle (data stored in session only)")

col1, col2 = st.columns(2)
with col1:
    period_date = st.date_input("Last Period Start Date", value=date.today())
with col2:
    period_length = st.slider("Period Length (days)", 1, 10, 5)

if st.button("📝 Log Period", type="primary"):
    log_entry = {
        "date": period_date,
        "length": period_length
    }
    st.session_state.period_logs.append(log_entry)
    st.success(f"Period logged for {period_date.strftime('%B %d, %Y')}")
    st.rerun()

# Display logged periods
if st.session_state.period_logs:
    st.markdown("#### Recent Periods")
    for i, log in enumerate(reversed(st.session_state.period_logs[-5:])):  # Last 5
        st.write(f"📅 {log['date'].strftime('%B %d, %Y')} - {log['length']} days")
    
    # Calculate cycle length if multiple entries
    if len(st.session_state.period_logs) >= 2:
        dates = sorted([log['date'] for log in st.session_state.period_logs])
        if len(dates) >= 2:
            cycle_lengths = [(dates[i+1] - dates[i]).days for i in range(len(dates)-1)]
            avg_cycle = sum(cycle_lengths) / len(cycle_lengths)
            st.info(f"📊 Average cycle length: {avg_cycle:.0f} days")

# Cycle Logging Section
st.markdown("---")
st.markdown("### 📝 Cycle Notes")
note_date = st.date_input("Date for Note", value=date.today(), key="note_date")

col1, col2 = st.columns(2)
with col1:
    pain_level = st.slider("Pain Level (1-5)", 1, 5, 1)
with col2:
    mood = st.selectbox("Mood", ["Good", "Okay", "Low", "Anxious", "Irritated"])

symptoms = st.multiselect(
    "Symptoms",
    ["Cramps", "Bloating", "Headache", "Fatigue", "Mood swings", "Other"]
)

notes = st.text_area("Additional Notes (optional)", height=100)

if st.button("💾 Save Note", type="primary"):
    note_entry = {
        "date": note_date,
        "pain_level": pain_level,
        "mood": mood,
        "symptoms": symptoms,
        "notes": notes
    }
    st.session_state.cycle_notes[str(note_date)] = note_entry
    st.success("Note saved!")
    st.rerun()

# Display recent notes
if st.session_state.cycle_notes:
    st.markdown("---")
    st.markdown("#### Recent Notes")
    sorted_notes = sorted(
        st.session_state.cycle_notes.items(),
        key=lambda x: x[0],
        reverse=True
    )[:5]
    
    for date_str, note in sorted_notes:
        with st.expander(f"📅 {date_str} - Pain: {note['pain_level']}/5 - {note['mood']}"):
            st.write(f"**Symptoms:** {', '.join(note['symptoms']) if note['symptoms'] else 'None'}")
            if note['notes']:
                st.write(f"**Notes:** {note['notes']}")

# Future Scope Note
st.markdown("---")
st.info("""
🚀 **Coming Soon:** Advanced tracking features including:
- Visual cycle charts
- Trend analysis
- Exportable tracking data
- Reminders and predictions
""")

# Disclaimer
st.markdown("---")
st.warning("⚠️ **Note:** Tracking data is stored in your browser session only. It is not saved permanently.")
