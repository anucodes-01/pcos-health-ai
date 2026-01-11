"""
Health Check Page - Core feature for structured signal collection & explainable assessment
"""

import streamlit as st
from utils.decision_engine import analyze_pcos_signals
from utils.report_generator import generate_summary

st.set_page_config(
    page_title="PCOS Health AI - Health Check",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Health Check")
st.markdown("### Structured Assessment of Your Health Patterns")

# Step 1: Personal & Cycle Information
with st.expander("Step 1: Personal & Cycle Information", expanded=True):
    age = st.slider("Age", 13, 50, 22)
    
    cycle_length = st.selectbox(
        "How regular is your menstrual cycle?",
        ["Regular (25–35 days)", "Irregular (varies frequently)", "Absent for months", "Absent or very irregular"]
    )
    
    period_pain = st.radio(
        "Do you experience severe period pain?",
        ["No", "Sometimes", "Often", "Frequently"]
    )
    
    missed_periods = st.radio(
        "Have you missed periods in the last 6 months?",
        ["No", "Occasionally (once or twice)", "Frequently (three or more times)", "Haven't had a period"]
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
        ["No", "Mild", "Noticeable", "Significant"]
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
        ["Good", "Disturbed", "Insomnia / very poor", "Poor/Insomnia"]
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
    st.markdown("---")
    st.markdown("## 📊 Your Health Assessment Results")
    
    # Risk Assessment
    risk_level = result['risk_level']
    risk_score = result['risk_score']
    
    if risk_level == "Low Risk":
        icon = "✅"
        st.success(f"## {icon} Risk Level: {risk_level}")
    elif risk_level == "Moderate Risk":
        icon = "⚠️"
        st.warning(f"## {icon} Risk Level: {risk_level}")
    else:
        icon = "🔴"
        st.error(f"## {icon} Risk Level: {risk_level}")
    
    st.progress(min(risk_score / 20, 1.0))
    
    # PCOS Type
    st.markdown("---")
    st.markdown(f"## 🔍 Detected Pattern: {result['pcos_type']}")
    st.info(result['explanation'])
    st.markdown(f"**AI Confidence:** {result['confidence']}%")
    st.progress(result['confidence'] / 100)
    st.caption("Confidence derived from transparent clinical signal weighting, not black-box ML.")
    
    # Contributing Factors
    st.markdown("---")
    st.markdown("### 🔎 Key Contributing Factors")
    signals = result['signals']
    factors = []
    
    if signals.get('cycle', 0) >= 3:
        factors.append("Significant menstrual irregularity")
    if signals.get('insulin', 0) >= 4:
        factors.append("Strong metabolic/insulin signals")
    if signals.get('stress', 0) >= 6:
        factors.append("High stress and adrenal load")
    if signals.get('androgen', 0) >= 3:
        factors.append("Noticeable androgen-related symptoms")
    if signals.get('inflammation', 0) >= 3:
        factors.append("Pain and inflammation indicators")
    
    if factors:
        for factor in factors:
            st.markdown(f"- {factor}")
    else:
        st.markdown("- No dominant contributing factors identified")
    
    # Doctor Consultation
    st.markdown("---")
    st.markdown("### 🩺 Medical Consultation Guidance")
    if result.get('doctor_needed', False):
        st.error("**Medical Consultation Recommended**")
        reasons = result.get('doctor_reasons', [])
        if reasons:
            st.write(f"Based on: {', '.join(reasons)}")
    else:
        st.success("**Medical Consultation Not Urgent**")
        st.write("Lifestyle-focused management may be appropriate at this stage.")
    
    # Condition Education
    st.markdown("---")
    st.markdown("### 📘 Understanding Common Conditions")
    
    with st.expander("🔹 PCOS (Polycystic Ovary Syndrome)"):
        st.write("""
        PCOS is a hormonal condition involving ovulation irregularities,
        androgen imbalance, and/or insulin resistance. It presents differently in each individual.
        """)
    
    with st.expander("🔹 PCOD (Polycystic Ovarian Disease)"):
        st.write("""
        PCOD is often influenced by lifestyle and metabolic factors.
        Many cases improve significantly with lifestyle changes.
        """)
    
    with st.expander("🔹 Endometriosis"):
        st.write("""
        Endometriosis involves tissue similar to the uterine lining
        growing outside the uterus. Severe or disabling menstrual pain is not normal and should be evaluated.
        """)
    
    # Lifestyle Plan Link
    if not result.get('doctor_needed', False):
        st.markdown("---")
        st.info("💡 **Next Step:** Check out your personalized Lifestyle Plan!")
        if st.button("🌱 View Lifestyle Plan", use_container_width=True):
            st.switch_page("pages/5_🌱_Lifestyle_Plan.py")
    
    # Report Generation
    st.markdown("---")
    st.markdown("### 📄 Health Summary (For You / Doctor)")
    
    reports = generate_summary(result, user_inputs)
    
    tab1, tab2 = st.tabs(["User Report", "Doctor Summary"])
    
    with tab1:
        st.text_area("Preview", reports['user_report'], height=300, key="user_preview")
        st.download_button(
            "📥 Download User Report",
            reports['user_report'],
            "pcos_health_summary.txt",
            "text/plain",
            key="download_user"
        )
    
    with tab2:
        st.text_area("Preview", reports['doctor_summary'], height=300, key="doc_preview")
        st.download_button(
            "📥 Download Doctor Summary",
            reports['doctor_summary'],
            "pcos_clinical_summary.txt",
            "text/plain",
            key="download_doc"
        )

# Display existing results if available
if 'health_check_result' in st.session_state and 'user_inputs' in st.session_state:
    result = st.session_state['health_check_result']
    user_inputs = st.session_state['user_inputs']
    
    st.markdown("---")
    st.info("💡 You have previously completed a health check. Results are stored in your session.")
    if st.button("📄 View Previous Results", use_container_width=True):
        st.rerun()

# Disclaimer
st.markdown("---")
st.error("⚠️ **Disclaimer:** This tool is for awareness only. It does not provide medical diagnosis.")
