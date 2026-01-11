# PCOS Health AI – Detailed Pages Specification

This document provides detailed UI layouts, component specifications, and implementation guidance for each page.

---

## 📄 Page 1: HOME (`pages/1_🏠_Home.py`)

### Layout Structure

```python
# Hero Section
st.title("PCOS Health AI")
st.markdown("### A Safe, Explainable Women's Health Companion")
st.markdown("**Understand • Decide • Feel Supported**")

# What We Do / Don't Do
col1, col2 = st.columns(2)
with col1:
    st.success("### ✅ What This Tool DOES")
    st.markdown("""
    - Helps you understand body signals
    - Reduces confusion and anxiety
    - Guides you on when to see a doctor
    - Provides structured education
    - Offers lifestyle guidance
    - Generates doctor-ready summaries
    """)
    
with col2:
    st.warning("### ❌ What This Tool DOES NOT Do")
    st.markdown("""
    - Provide medical diagnosis
    - Prescribe medications
    - Replace healthcare professionals
    - Store your personal data
    - Make medical claims
    """)

# Feature Cards (4 columns)
st.markdown("### 🎯 Explore Our Features")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background-color: #E8D5FF; text-align: center;'>
        <h2>🔍</h2>
        <h4>Health Check</h4>
        <p>Structured assessment of your health patterns</p>
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background-color: #FFD5E5; text-align: center;'>
        <h2>💬</h2>
        <h4>AI Assistant</h4>
        <p>Guided conversation for clarification</p>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background-color: #D5FFE8; text-align: center;'>
        <h2>📚</h2>
        <h4>Learn Conditions</h4>
        <p>Educational content about PCOS, PCOD, Endometriosis</p>
    </div>
    """, unsafe_allow_html=True)
    
with col4:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background-color: #FFE8D5; text-align: center;'>
        <h2>👥</h2>
        <h4>Community</h4>
        <p>Safe space for support and sharing</p>
    </div>
    """, unsafe_allow_html=True)

# Video Section
st.markdown("### 📹 How It Works")
# YouTube embed (placeholder)
st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")

# CTA Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 Start Health Check", type="primary", use_container_width=True):
        st.switch_page("pages/2_🔍_Health_Check.py")
        
with col2:
    if st.button("💬 Talk to AI Assistant", use_container_width=True):
        st.switch_page("pages/3_💬_AI_Assistant.py")

# Disclaimer Banner
st.markdown("---")
st.info("""
⚠️ **Disclaimer:** This tool is for awareness and support only. 
It does not provide medical diagnosis. Always consult healthcare professionals for medical advice.
""")
```

### Key Components

1. **Hero Section**: Clear title, subtitle, tagline
2. **Feature Cards**: 4-column grid with icons
3. **Video Embed**: YouTube iframe (placeholder)
4. **CTA Buttons**: Primary and secondary actions
5. **Disclaimer**: Persistent banner

---

## 📄 Page 2: HEALTH CHECK (`pages/2_🔍_Health_Check.py`)

### Layout Structure

```python
import streamlit as st
from utils.decision_engine import analyze_pcos_signals
from utils.report_generator import generate_summary

st.title("🔍 Health Check")
st.markdown("### Structured Assessment of Your Health Patterns")

# Step 1: Personal & Cycle Information
with st.expander("Step 1: Personal & Cycle Information", expanded=True):
    age = st.slider("Age", 13, 50, 22)
    
    cycle_length = st.selectbox(
        "How regular is your menstrual cycle?",
        ["Regular (25–35 days)", "Irregular (varies frequently)", "Absent for months"]
    )
    
    period_pain = st.radio(
        "Do you experience severe period pain?",
        ["No", "Sometimes", "Often"]
    )
    
    missed_periods = st.radio(
        "Have you missed periods in the last 6 months?",
        ["No", "Occasionally", "Frequently"]
    )

# Step 2: Metabolic & Physical Signals
with st.expander("Step 2: Metabolic & Physical Signals"):
    weight_change = st.selectbox(
        "Have you experienced unexplained weight changes?",
        ["No", "Weight gain", "Weight loss", "Fluctuates"]
    )
    
    sugar_cravings = st.radio(
        "Do you experience strong sugar cravings?",
        ["No", "Occasionally", "Frequently"]
    )
    
    facial_hair = st.radio(
        "Do you notice excess facial/body hair growth?",
        ["No", "Mild", "Noticeable"]
    )
    
    acne = st.radio(
        "Do you experience acne?",
        ["No", "Mild", "Moderate", "Severe"]
    )
    
    hair_loss = st.radio(
        "Have you noticed hair thinning or loss?",
        ["No", "Mild", "Noticeable"]
    )

# Step 3: Mental & Stress Signals
with st.expander("Step 3: Mental & Stress Signals"):
    stress_level = st.slider("Average stress level (last 3 months)", 0, 10, 5)
    
    sleep_quality = st.selectbox(
        "How is your sleep quality?",
        ["Good", "Disturbed", "Insomnia / very poor"]
    )
    
    mood_changes = st.radio(
        "Do you notice mood swings or emotional burnout?",
        ["No", "Occasionally", "Frequently"]
    )
    
    anxiety = st.radio(
        "Do you experience anxiety?",
        ["No", "Occasionally", "Frequently"]
    )

# Step 4: Lifestyle Factors
with st.expander("Step 4: Lifestyle Factors"):
    activity_level = st.selectbox(
        "Physical activity level",
        ["Sedentary", "Lightly active", "Moderately active", "Very active"]
    )
    
    diet_pattern = st.selectbox(
        "Diet pattern",
        ["Balanced", "High sugar / processed", "Low-carb / controlled", "Irregular"]
    )

# Step 5: Optional Family History
with st.expander("Step 5: Optional - Family History"):
    family_history = st.radio(
        "Is there a history of PCOS/PCOD in your family?",
        ["No", "Not sure", "Yes"]
    )

# Analysis Button
if st.button("🔍 Analyze My Health Patterns", type="primary", use_container_width=True):
    # Collect all inputs
    user_inputs = {
        "age": age,
        "cycle_length": cycle_length,
        "period_pain": period_pain,
        "missed_periods": missed_periods,
        "weight_change": weight_change,
        "sugar_cravings": sugar_cravings,
        "facial_hair": facial_hair,
        "acne": acne,
        "hair_loss": hair_loss,
        "stress_level": stress_level,
        "sleep_quality": sleep_quality,
        "mood_changes": mood_changes,
        "anxiety": anxiety,
        "activity_level": activity_level,
        "diet_pattern": diet_pattern,
        "family_history": family_history
    }
    
    # Call decision engine
    result = analyze_pcos_signals(**user_inputs)
    
    # Store in session state
    st.session_state['health_check_result'] = result
    st.session_state['user_inputs'] = user_inputs
    st.session_state['doctor_needed'] = result.get('doctor_needed', False)
    
    # Display Results
    display_results(result)
    
    # Generate and display report
    reports = generate_summary(result, user_inputs)
    display_reports(reports)

def display_results(result):
    """Display health check results"""
    # Risk Level
    risk_level = result['risk_level']
    risk_score = result['risk_score']
    
    # Color coding
    if risk_level == "Low Risk":
        color = "green"
        icon = "✅"
    elif risk_level == "Moderate Risk":
        color = "orange"
        icon = "⚠️"
    else:
        color = "red"
        icon = "🔴"
    
    st.markdown(f"## {icon} Risk Assessment: {risk_level}")
    st.progress(min(risk_score / 20, 1.0))
    
    # PCOS Type
    st.markdown(f"## 🔍 Detected Pattern: {result['pcos_type']}")
    st.info(result['explanation'])
    st.markdown(f"**AI Confidence:** {result['confidence']}%")
    st.progress(result['confidence'] / 100)
    st.caption("Confidence derived from transparent clinical signal weighting.")
    
    # Contributing Factors
    st.markdown("### 🔎 Key Contributing Factors")
    signals = result['signals']
    factors = []
    
    if signals['cycle'] >= 3:
        factors.append("Significant menstrual irregularity")
    if signals['insulin'] >= 4:
        factors.append("Strong metabolic/insulin signals")
    if signals['stress'] >= 6:
        factors.append("High stress and adrenal load")
    if signals['androgen'] >= 3:
        factors.append("Noticeable androgen-related symptoms")
    if signals['inflammation'] >= 3:
        factors.append("Pain and inflammation indicators")
    
    for factor in factors:
        st.markdown(f"- {factor}")
    
    # Doctor Consultation
    st.markdown("### 🩺 Medical Consultation Guidance")
    if result.get('doctor_needed', False):
        st.error("**Medical Consultation Recommended**")
        reasons = result.get('doctor_reasons', [])
        st.write(f"Based on: {', '.join(reasons)}")
    else:
        st.success("**Medical Consultation Not Urgent**")
        st.write("Lifestyle-focused management may be appropriate.")

def display_reports(reports):
    """Display and download reports"""
    st.markdown("### 📄 Health Summary")
    
    tab1, tab2 = st.tabs(["User Report", "Doctor Summary"])
    
    with tab1:
        st.text_area("Preview", reports['user_report'], height=300)
        st.download_button(
            "📥 Download User Report",
            reports['user_report'],
            "pcos_health_summary.txt",
            "text/plain"
        )
    
    with tab2:
        st.text_area("Preview", reports['doctor_summary'], height=300)
        st.download_button(
            "📥 Download Doctor Summary",
            reports['doctor_summary'],
            "pcos_clinical_summary.txt",
            "text/plain"
        )

# Disclaimer
st.markdown("---")
st.info("⚠️ This tool is for awareness only. It does not provide medical diagnosis.")
```

### Key Features

1. **Multi-step Form**: Expandable sections for organized input
2. **Comprehensive Inputs**: All signals collected
3. **Result Display**: Visual indicators, clear explanations
4. **Report Generation**: User and doctor summaries
5. **Session State**: Store results for use in other pages

---

## 📄 Page 3: AI ASSISTANT (`pages/3_💬_AI_Assistant.py`)

### Layout Structure

```python
import streamlit as st
from utils.chat_engine import generate_response, get_questions_for_category
from utils.prompt_library import PROMPTS

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
        st.session_state.concern_category
    )
    
    for i, q in enumerate(questions[:5]):  # Limit to 5 questions
        if q['type'] == 'radio':
            answer = st.radio(q['text'], q['options'], key=f"q_{i}")
        elif q['type'] == 'selectbox':
            answer = st.selectbox(q['text'], q['options'], key=f"q_{i}")
        else:
            answer = st.slider(q['text'], q['options'][0], q['options'][1], key=f"q_{i}")
        
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
            st.success("This is within the range of normal variation.")
        else:
            st.warning("This may warrant further attention.")
    
    st.markdown("### Next Steps")
    for step in response['next_steps']:
        st.markdown(f"- {step}")
    
    if response.get('suggest_health_check'):
        if st.button("🔍 Take Full Health Check", type="primary"):
            st.switch_page("pages/2_🔍_Health_Check.py")
    
    if st.button("🔄 Start New Conversation"):
        # Reset session state
        for key in ['chat_step', 'age_group', 'concern_category', 'answers']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# Disclaimer
st.markdown("---")
st.info("⚠️ This assistant provides guidance only. It does not diagnose conditions.")
```

### Key Features

1. **Step-by-Step Flow**: Clear progression through 5 steps
2. **Guided Questions**: From prompt_library
3. **Response Generation**: Rule-based from chat_engine
4. **Session State Management**: Track conversation flow
5. **Next Steps**: Clear action items

---

## 📄 Page 4: LEARN CONDITIONS (`pages/4_📚_Learn_Conditions.py`)

### Layout Structure

```python
import streamlit as st

st.title("📚 Learn About Conditions")
st.markdown("### Educational Content About Common Conditions")

# PCOS Panel
with st.expander("🔹 PCOS (Polycystic Ovary Syndrome)", expanded=True):
    st.markdown("### What is PCOS?")
    st.write("""
    PCOS is a hormonal condition that affects how your ovaries work. 
    It involves ovulation irregularities, androgen imbalance, and/or insulin resistance.
    
    PCOS presents differently in each individual - there's no one-size-fits-all experience.
    """)
    
    st.markdown("### Common Symptoms")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - Irregular periods
        - Excess hair growth
        - Acne
        - Weight gain
        """)
    with col2:
        st.markdown("""
        - Hair thinning
        - Mood changes
        - Sleep issues
        - Difficulty conceiving
        """)
    
    st.markdown("### Why PCOS is Often Misunderstood")
    st.write("""
    PCOS is complex and varies greatly between individuals. Many people go undiagnosed 
    for years because symptoms can be subtle or attributed to other causes.
    """)
    
    st.markdown("### Normal vs Not Normal")
    st.success("**Normal:** Slight cycle variations, occasional breakouts")
    st.warning("**Concerning:** Missing periods for months, severe symptoms")
    
    st.markdown("### When to Seek Help")
    st.write("If you experience persistent irregular periods, severe symptoms, or concerns about fertility.")
    
    st.markdown("### Myths vs Facts")
    col1, col2 = st.columns(2)
    with col1:
        st.error("**Myth:** PCOS means you can't have children")
    with col2:
        st.success("**Fact:** Many people with PCOS conceive with appropriate care")

# PCOD Panel
with st.expander("🔹 PCOD (Polycystic Ovarian Disease)"):
    st.markdown("### What is PCOD?")
    st.write("""
    PCOD is often used interchangeably with PCOS, but may refer to a broader 
    condition influenced by lifestyle and metabolic factors.
    
    Many PCOD cases improve significantly with lifestyle changes.
    """)
    
    # Similar structure as PCOS panel
    # ... (abbreviated for space)

# Endometriosis Panel
with st.expander("🔹 Endometriosis"):
    st.markdown("### What is Endometriosis?")
    st.write("""
    Endometriosis involves tissue similar to the uterine lining growing outside 
    the uterus. It can cause significant pain and other symptoms.
    
    Severe or disabling menstrual pain is not normal and should be evaluated.
    """)
    
    # Similar structure as PCOS panel
    # ... (abbreviated for space)

# Resources Section
st.markdown("---")
st.markdown("### 📖 Additional Resources")
st.markdown("""
- [Reputable Source 1](#)
- [Reputable Source 2](#)
- [Support Groups](#)
""")

# Disclaimer
st.markdown("---")
st.info("⚠️ This content is for educational purposes only. Always consult healthcare professionals for medical advice.")
```

### Key Features

1. **Expandable Panels**: Organized by condition
2. **Structured Content**: What, Symptoms, When to Seek Help, Myths vs Facts
3. **Educational Tone**: Reassuring, non-fear-mongering
4. **Resources Section**: Links to additional information

---

## 📄 Page 5: LIFESTYLE PLAN (`pages/5_🌱_Lifestyle_Plan.py`)

### Layout Structure

```python
import streamlit as st

st.title("🌱 Lifestyle Plan")
st.markdown("### Personalized Lifestyle Guidance")

# Check if user has completed Health Check
if 'health_check_result' not in st.session_state:
    st.warning("⚠️ Please complete the Health Check first to get your personalized plan.")
    if st.button("🔍 Go to Health Check"):
        st.switch_page("pages/2_🔍_Health_Check.py")
    st.stop()

result = st.session_state['health_check_result']

# Check if doctor consultation is urgent
if result.get('doctor_needed', False):
    st.error("""
    ⚠️ **Medical consultation is recommended before focusing on lifestyle changes.**
    
    Please consult with a healthcare professional first. After consultation, 
    you can return here for lifestyle support.
    """)
    if st.button("🩺 Find Help"):
        st.switch_page("pages/8_🩺_Find_Help.py")
    st.stop()

# Display personalized plan based on PCOS type
pcos_type = result['pcos_type']

if "Adrenal" in pcos_type or "Stress" in pcos_type:
    st.success("### 🧘 Focus Area: Stress & Nervous System Regulation")
    st.markdown("""
    **Priority Actions:**
    - Prioritize consistent sleep schedule (7-9 hours)
    - Reduce chronic stress through mindfulness or gentle movement
    - Avoid overtraining - balance activity with recovery
    - Consider cortisol evaluation with healthcare provider
    - Practice stress-reduction techniques (breathing, meditation)
    
    **Nutrition:**
    - Regular meal timing (avoid skipping meals)
    - Balanced macronutrients
    - Limit caffeine, especially in afternoon
    
    **Movement:**
    - Gentle activities: walking, yoga, stretching
    - Avoid excessive high-intensity exercise
    - Prioritize recovery days
    """)
    
elif "Insulin" in pcos_type:
    st.success("### 🍽️ Focus Area: Metabolic Health & Blood Sugar Stability")
    st.markdown("""
    **Priority Actions:**
    - Stabilize blood sugar with regular meals
    - Reduce refined sugar and processed foods
    - Maintain consistent eating schedule
    - Test fasting insulin & HbA1c with healthcare provider
    - Combine protein, fiber, and healthy fats at meals
    
    **Nutrition:**
    - Balanced meals with protein, complex carbs, healthy fats
    - Fiber-rich foods (vegetables, whole grains)
    - Minimize sugary snacks and drinks
    
    **Movement:**
    - Regular moderate activity
    - Post-meal walks can help blood sugar
    - Strength training 2-3x per week
    """)
    
elif "Lean" in pcos_type:
    st.success("### 📊 Focus Area: Hormonal Balance")
    st.markdown("""
    **Priority Actions:**
    - Track ovulation and cycle length
    - Avoid extreme dieting or calorie restriction
    - Monitor LH/FSH ratio with healthcare provider
    - Support hormonal health through balanced nutrition
    
    **Nutrition:**
    - Adequate calories for your activity level
    - Balanced macronutrients
    - Support reproductive health with nutrient-dense foods
    
    **Movement:**
    - Moderate, regular activity
    - Avoid over-exercising
    - Include recovery time
    """)
    
elif "Inflammatory" in pcos_type:
    st.success("### 🔥 Focus Area: Inflammation Management")
    st.markdown("""
    **Priority Actions:**
    - Improve recovery and rest
    - Identify inflammatory triggers (food, stress, environment)
    - Track pain patterns and symptoms
    - Support immune system through lifestyle
    
    **Nutrition:**
    - Anti-inflammatory foods (omega-3s, colorful vegetables)
    - Reduce processed and inflammatory foods
    - Stay hydrated
    
    **Movement:**
    - Gentle activities that don't exacerbate pain
    - Prioritize rest and recovery
    - Listen to your body's signals
    """)
    
else:
    st.info("### 🌿 General Wellness Focus")
    st.markdown("""
    **Maintenance Actions:**
    - Balanced diet
    - Regular movement
    - Adequate sleep
    - Monthly symptom tracking
    - Regular healthcare check-ups
    """)

# Disclaimer
st.markdown("---")
st.info("""
⚠️ **Note:** These recommendations are lifestyle-focused only. 
They do not replace medical advice. Always consult healthcare professionals 
before making significant changes.
""")
```

### Key Features

1. **Access Control**: Requires Health Check completion
2. **Doctor Check**: Redirects if consultation urgent
3. **Personalized Plans**: Based on detected PCOS type
4. **Actionable Guidance**: Clear, specific recommendations
5. **Lifestyle-Only**: No supplements or medications mentioned

---

## 📄 Page 6: TRACKERS (`pages/6_📊_Trackers.py`)

### Layout Structure

```python
import streamlit as st
from datetime import date, timedelta

st.title("📊 Trackers")
st.markdown("### Basic Symptom & Cycle Tracking")

# Initialize session state for tracking data
if 'period_logs' not in st.session_state:
    st.session_state.period_logs = []
if 'cycle_notes' not in st.session_state:
    st.session_state.cycle_notes = {}

# Period Tracker Section
st.markdown("### 📅 Period Tracker")
st.markdown("Track your menstrual cycle (data stored in session only)")

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
note_date = st.date_input("Date for Note", value=date.today())

col1, col2 = st.columns(2)
with col1:
    pain_level = st.slider("Pain Level (1-5)", 1, 5, 1)
with col2:
    mood = st.selectbox("Mood", ["Good", "Okay", "Low", "Anxious", "Irritated"])

symptoms = st.multiselect(
    "Symptoms",
    ["Cramps", "Bloating", "Headache", "Fatigue", "Mood swings", "Other"]
)

notes = st.text_area("Additional Notes (optional)")

if st.button("💾 Save Note"):
    note_entry = {
        "date": note_date,
        "pain_level": pain_level,
        "mood": mood,
        "symptoms": symptoms,
        "notes": notes
    }
    st.session_state.cycle_notes[str(note_date)] = note_entry
    st.success("Note saved!")

# Display recent notes
if st.session_state.cycle_notes:
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
st.caption("⚠️ Tracking data is stored in your browser session only. It is not saved permanently.")
```

### Key Features

1. **Period Tracker**: Date logging, cycle calculation
2. **Cycle Notes**: Pain, mood, symptoms tracking
3. **Session Storage**: Data in session state only
4. **Future Scope**: Clear "coming soon" messaging
5. **Simple UI**: Easy to use, non-overwhelming

---

## 📄 Page 7: COMMUNITY (`pages/7_👥_Community.py`)

### Layout Structure

```python
import streamlit as st

st.title("👥 Community")
st.markdown("### A Safe Space for Support & Sharing")

# Community Guidelines
with st.expander("📜 Community Guidelines", expanded=True):
    st.markdown("""
    **Our Community Rules:**
    - ✅ Be respectful and kind
    - ✅ Share experiences, not medical advice
    - ✅ Respect privacy (anonymous by default)
    - ❌ No personal attacks
    - ❌ No medical diagnosis or prescriptions
    - ❌ No spam or promotional content
    
    **Remember:** This is a supportive space, not a replacement for professional care.
    """)

# Demo Posts (Static Content)
st.markdown("---")
st.markdown("### 💬 Recent Posts")

# Demo Post 1
with st.container():
    st.markdown("""
    <div style='padding: 15px; border-radius: 8px; background-color: #F0F0F0; margin-bottom: 10px;'>
        <strong>Anonymous</strong> • 2 days ago<br>
        "Finally found people who understand what I'm going through. 
        Thank you for this space! 💜"<br>
        <small>💬 5 comments • 👍 12 likes</small>
    </div>
    """, unsafe_allow_html=True)

# Demo Post 2
with st.container():
    st.markdown("""
    <div style='padding: 15px; border-radius: 8px; background-color: #F0F0F0; margin-bottom: 10px;'>
        <strong>Anonymous</strong> • 5 days ago<br>
        "Has anyone found lifestyle changes helpful? Looking for tips 
        on managing symptoms naturally."<br>
        <small>💬 8 comments • 👍 15 likes</small>
    </div>
    """, unsafe_allow_html=True)

# Demo Post 3
with st.container():
    st.markdown("""
    <div style='padding: 15px; border-radius: 8px; background-color: #F0F0F0; margin-bottom: 10px;'>
        <strong>Anonymous</strong> • 1 week ago<br>
        "This platform helped me understand when to see a doctor. 
        Got my diagnosis and feeling more empowered now!"<br>
        <small>💬 12 comments • 👍 23 likes</small>
    </div>
    """, unsafe_allow_html=True)

# Create Post Section
st.markdown("---")
st.markdown("### ✍️ Create a Post")

# Initialize session state for posts
if 'community_posts' not in st.session_state:
    st.session_state.community_posts = []

post_title = st.text_input("Title (optional)")
post_content = st.text_area("Share your thoughts...", height=150)

col1, col2 = st.columns(2)
with col1:
    post_anonymously = st.checkbox("Post anonymously", value=True)
with col2:
    if st.button("📤 Post", type="primary"):
        if post_content:
            new_post = {
                "title": post_title,
                "content": post_content,
                "author": "Anonymous" if post_anonymously else "User",
                "timestamp": "Just now"
            }
            st.session_state.community_posts.append(new_post)
            st.success("Post created! (Stored in session only)")
            st.rerun()
        else:
            st.warning("Please write something to post.")

# Display user's posts
if st.session_state.community_posts:
    st.markdown("### 📝 Your Posts")
    for post in reversed(st.session_state.community_posts):
        with st.expander(f"📄 {post.get('title', 'Untitled')} - {post['author']} • {post['timestamp']}"):
            st.write(post['content'])

# Moderation Disclaimer
st.markdown("---")
st.warning("""
⚠️ **Note:** This is a demo/static community space. In a production version, 
posts would be moderated and stored securely. Always prioritize your privacy and safety.
""")

# Disclaimer
st.markdown("---")
st.info("""
⚠️ **Community Disclaimer:** Posts and comments are for support and sharing only. 
They do not constitute medical advice. Always consult healthcare professionals for medical concerns.
""")
```

### Key Features

1. **Community Guidelines**: Clear rules prominently displayed
2. **Demo Posts**: Static examples for demonstration
3. **Create Post**: Simple form (session state only)
4. **Anonymous by Default**: Privacy-focused
5. **Moderation Note**: Clear disclaimer about demo nature

---

## 📄 Page 8: FIND HELP (`pages/8_🩺_Find_Help.py`)

### Layout Structure

```python
import streamlit as st

st.title("🩺 Find Help")
st.markdown("### Connect with Healthcare Professionals")

# When to See a Doctor Section
st.markdown("### 🚨 When to See a Doctor")

st.markdown("""
**Seek immediate medical attention if you experience:**
- Severe pelvic pain
- Heavy bleeding that soaks through pads/tampons hourly
- Signs of infection (fever, unusual discharge)
- Severe mood changes or thoughts of self-harm

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

st.warning("""
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
- [Platform 1](#) - General healthcare
- [Platform 2](#) - Specialized women's health
- [Platform 3](#) - Endocrinology focus

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
    if st.button("📄 Go to Health Check Report"):
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
```

### Key Features

1. **When to See a Doctor**: Clear indicators
2. **Demo Listings**: 5 example doctors with disclaimers
3. **Teleconsult Options**: Information about virtual visits
4. **Preparation Tips**: Helpful guidance
5. **Self-Advocacy**: Empowering information

---

**End of Pages Specification**
