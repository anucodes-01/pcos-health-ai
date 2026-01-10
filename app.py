import streamlit as st
from utils.decision_engine import analyze_pcos_signals

# -------------------------------------------------
# APP HEADER
# -------------------------------------------------
st.title("PCOS Health AI")
st.caption("Early pattern detection • Not a medical diagnosis")

st.markdown("---")
st.subheader("Step 1: Personal & Cycle Information")

age = st.slider("Age", 13, 50, 22)

cycle_length = st.selectbox(
    "How regular is your menstrual cycle?",
    [
        "Regular (25–35 days)",
        "Irregular (varies frequently)",
        "Absent for months"
    ]
)

period_pain = st.radio(
    "Do you experience severe period pain?",
    ["No", "Sometimes", "Often"]
)

st.markdown("---")
st.subheader("Step 2: Metabolic & Physical Signals")

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

st.markdown("---")
st.subheader("Step 3: Mental & Stress Signals")

stress_level = st.slider(
    "Average stress level (last 3 months)",
    0, 10, 5
)

sleep_quality = st.selectbox(
    "How is your sleep quality?",
    ["Good", "Disturbed", "Insomnia / very poor"]
)

mood_changes = st.radio(
    "Do you notice mood swings or emotional burnout?",
    ["No", "Occasionally", "Frequently"]
)

st.markdown("---")
st.subheader("Step 4: Lifestyle Factors")

activity_level = st.selectbox(
    "Physical activity level",
    ["Sedentary", "Lightly active", "Moderately active", "Very active"]
)

diet_pattern = st.selectbox(
    "Diet pattern",
    ["Balanced", "High sugar / processed", "Low-carb / controlled", "Irregular"]
)

# -------------------------------------------------
# ANALYSIS BUTTON
# -------------------------------------------------
submit = st.button("Analyze My Health Patterns")

if submit:
    st.markdown("## 🧠 Step 2: Understanding Your Health Signals")

    # 🔹 CALL DECISION ENGINE (CORE AI LOGIC)
    result = analyze_pcos_signals(
        cycle_length=cycle_length,
        period_pain=period_pain,
        stress_level=stress_level,
        sleep_quality=sleep_quality,
        mood_changes=mood_changes,
        sugar_cravings=sugar_cravings,
        weight_change=weight_change,
        facial_hair=facial_hair
    )

    # -------------------------------------------------
    # STEP 3: RISK ASSESSMENT
    # -------------------------------------------------
    st.markdown("## ⚠️ Step 3: Overall PCOS Risk Assessment")

    risk_score = result["risk_score"]
    risk_level = result["risk_level"]

    st.progress(min(risk_score / 20, 1.0))

    color = "green" if risk_level == "Low Risk" else "orange" if risk_level == "Moderate Risk" else "red"

    st.markdown(
        f"<h3 style='color:{color}'>Risk Level: {risk_level}</h3>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # STEP 4: PCOS PATTERN
    # -------------------------------------------------
    st.markdown("## 🔍 Step 4: Detected PCOS Pattern")
    st.success(f"**Detected Pattern:** {result['pcos_type']}")
    st.write(result["explanation"])
    st.markdown(f"**AI Confidence:** {result['confidence']}%")
    st.progress(result["confidence"] / 100)
    st.caption(
    "Confidence is derived from transparent clinical signal weighting, "
    "not black-box machine learning."
)
    st.markdown(f"**AI Confidence:** {result['confidence']}%")
    st.caption("Confidence derived from transparent clinical signal weighting, not black-box ML.")


    # -------------------------------------------------
    # CONTRIBUTING FACTORS
    # -------------------------------------------------
    st.markdown("### 🔎 Key Contributing Factors")

    signals = result["signals"]

    if signals["cycle"] >= 3:
        st.write("- Significant menstrual irregularity detected")
    if signals["insulin"] >= 4:
        st.write("- Strong metabolic / insulin-related signals")
    if signals["stress"] >= 6:
        st.write("- High stress and adrenal load")
    if signals["androgen"] >= 3:
        st.write("- Noticeable androgen-related symptoms")
    if signals["inflammation"] >= 3:
        st.write("- Pain and inflammation indicators present")

    st.info(
        "This is an early pattern-detection system for awareness only. "
        "It is not a medical diagnosis."
    )

    # -------------------------------------------------
    # STEP 5: FOLLOW-UP GUIDANCE
    # -------------------------------------------------
    st.markdown("## 🔁 Step 5: Suggested Follow-up & Care Focus")

    pcos_type = result["pcos_type"]

    if "Adrenal" in pcos_type:
        st.success("🧘 Focus Area: Stress & Nervous System Regulation")
        st.write("""
        - Prioritize sleep consistency
        - Reduce chronic stress
        - Avoid overtraining
        - Consider cortisol & thyroid evaluation
        """)

    elif "Insulin" in pcos_type:
        st.success("🍽️ Focus Area: Metabolic Health")
        st.write("""
        - Stabilize blood sugar
        - Reduce refined sugar
        - Maintain regular meals
        - Test fasting insulin & HbA1c
        """)

    elif "Lean" in pcos_type:
        st.success("📊 Focus Area: Hormonal Balance")
        st.write("""
        - Track ovulation & cycle length
        - Avoid extreme dieting
        - Monitor LH/FSH ratio
        """)

    elif "Inflammatory" in pcos_type:
        st.success("🔥 Focus Area: Inflammation Management")
        st.write("""
        - Improve recovery & rest
        - Identify inflammatory triggers
        - Track pain patterns
        """)

    else:
        st.info("""
        No dominant PCOS pattern detected.
        Maintain healthy routines and reassess monthly.
        """)
    # -------------------------------------------------
    # STEP 6: DO I NEED A DOCTOR?
    # -------------------------------------------------
    st.markdown("## 🩺 Medical Consultation Guidance")

    doctor_needed = False
    reasons = []

    scores = result["signals"]

    if risk_level == "High Risk":
        doctor_needed = True
        reasons.append("overall high risk pattern")

    if scores["cycle"] >= 3 and scores["inflammation"] >= 3:
        doctor_needed = True
        reasons.append("severe pain with cycle irregularity")

    if scores["insulin"] >= 6:
        reasons.append("strong metabolic indicators")

    if doctor_needed:
        st.error(
            "### Medical Consultation Recommended\n"
            f"Based on {', '.join(reasons)}, professional medical evaluation is advised."
        )
    else:
        st.success(
            "### Medical Consultation Not Urgent\n"
            "Lifestyle-focused management and monitoring may be appropriate at this stage."
        )

    # -------------------------------------------------
    # STEP 7: CONDITION EDUCATION (SAFE, NON-DIAGNOSTIC)
    # -------------------------------------------------
    st.markdown("## 📘 Understanding Common Conditions")

    with st.expander("🔹 PCOS (Polycystic Ovary Syndrome)"):
        st.write("""
        PCOS is a hormonal condition involving ovulation irregularities,
        androgen imbalance, and/or insulin resistance.

        It presents differently in each individual.
        """)

    with st.expander("🔹 PCOD (Polycystic Ovarian Disease)"):
        st.write("""
        PCOD is often influenced by lifestyle and metabolic factors.
        Many cases improve significantly with lifestyle changes.
        """)

    with st.expander("🔹 Endometriosis"):
        st.write("""
        Endometriosis involves tissue similar to the uterine lining
        growing outside the uterus.

        Severe or disabling menstrual pain is not normal and should be evaluated.
        """)

    # -------------------------------------------------
    # STEP 8: LIFESTYLE PLAN (ONLY IF DOCTOR NOT URGENT)
    # -------------------------------------------------
    st.markdown("## 🌱 Lifestyle Focus")

    if not doctor_needed:
        if "Insulin" in pcos_type:
            st.write("""
            **Focus:** Blood sugar stability  
            - Balanced meals with protein & fiber  
            - Consistent eating schedule  
            - Moderate exercise  
            """)

        elif "Adrenal" in pcos_type:
            st.write("""
            **Focus:** Stress & nervous system  
            - Prioritize sleep  
            - Reduce overexertion  
            - Gentle movement & recovery  
            """)

        elif "Inflammatory" in pcos_type:
            st.write("""
            **Focus:** Recovery & inflammation  
            - Adequate rest  
            - Gentle activity  
            - Symptom journaling  
            """)

        else:
            st.write("""
            **Focus:** Maintenance  
            - Balanced diet  
            - Regular movement  
            - Monthly symptom tracking  
            """)

    # -------------------------------------------------
    # STEP 9: EXPORTABLE HEALTH SUMMARY
    # -------------------------------------------------
    st.markdown("## 📄 Health Summary (For You / Doctor)")

    report_text = f"""
PCOS Health AI – Summary

Risk Level: {risk_level}
Detected Pattern: {pcos_type}

Key Signals:
- Cycle score: {scores['cycle']}
- Stress score: {scores['stress']}
- Insulin score: {scores['insulin']}
- Androgen score: {scores['androgen']}
- Inflammation score: {scores['inflammation']}

Recommendation:
{"Medical consultation recommended." if doctor_needed else "Lifestyle-focused monitoring advised."}

Disclaimer:
This is not a medical diagnosis.
"""

    st.text_area("Preview Report", report_text, height=250)

    st.download_button(
        label="📥 Download Report (Text)",
        data=report_text,
        file_name="pcos_health_summary.txt",
        mime="text/plain"
    )
