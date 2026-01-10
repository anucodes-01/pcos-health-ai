import streamlit as st

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

submit = st.button("Analyze My Health Patterns")
if submit:
    st.markdown("## 🧠 Step 2: Understanding Your Health Signals")

    # -----------------------------
    # SIGNAL EXTRACTION
    # -----------------------------
    cycle_signal = 0
    stress_signal = 0
    insulin_signal = 0
    androgen_signal = 0
    inflammation_signal = 0

    # Cycle irregularity
    if cycle_length == "Irregular (varies frequently)":
        cycle_signal += 2
    elif cycle_length == "Absent for months":
        cycle_signal += 3

    # Stress & adrenal signals (threshold-based)
    if stress_level >= 7:
        stress_signal += 4
    elif stress_level >= 4:
        stress_signal += 2

    if sleep_quality == "Disturbed":
        stress_signal += 1
    elif sleep_quality == "Insomnia / very poor":
        stress_signal += 2

    if mood_changes == "Frequently":
        stress_signal += 2

    # Insulin resistance signals
    if sugar_cravings == "Frequently":
        insulin_signal += 3
    elif sugar_cravings == "Occasionally":
        insulin_signal += 1

    if weight_change in ["Weight gain", "Fluctuates"]:
        insulin_signal += 2

    # Androgen signals
    if facial_hair == "Noticeable":
        androgen_signal += 3
    elif facial_hair == "Mild":
        androgen_signal += 1

    # Inflammatory signals
    if period_pain == "Often":
        inflammation_signal += 2

    if sleep_quality != "Good":
        inflammation_signal += 1

    # -----------------------------
    # PCOS TYPE DETECTION
    # -----------------------------
    pcos_type = "Low / Unclear PCOS Pattern"
    explanation = ""

    if stress_signal >= 7 and insulin_signal < 4:
        pcos_type = "Adrenal PCOS (Stress-driven)"
        explanation = (
            "Your responses show strong stress and adrenal-related signals. "
            "This PCOS type is commonly underdiagnosed and linked to chronic stress."
        )

    elif insulin_signal >= 6:
        pcos_type = "Insulin-Resistant PCOS"
        explanation = (
            "Metabolic indicators such as sugar cravings and weight changes "
            "suggest insulin resistance, a common PCOS driver."
        )

    elif cycle_signal >= 3 and insulin_signal <= 2:
        pcos_type = "Lean PCOS"
        explanation = (
            "Despite limited metabolic symptoms, your menstrual irregularities "
            "suggest a hormonal imbalance consistent with Lean PCOS."
        )

    elif inflammation_signal >= 3:
        pcos_type = "Inflammatory PCOS"
        explanation = (
            "Pain, fatigue, and inflammatory indicators dominate your symptom pattern."
        )

    # -----------------------------
    # OVERALL PCOS RISK SCORING
    # -----------------------------
    total_risk_score = (
        cycle_signal +
        stress_signal +
        insulin_signal +
        androgen_signal +
        inflammation_signal
    )

    if total_risk_score <= 6:
        risk_level = "Low Risk"
        risk_color = "green"
    elif total_risk_score <= 12:
        risk_level = "Moderate Risk"
        risk_color = "orange"
    else:
        risk_level = "High Risk"
        risk_color = "red"

    # -----------------------------
    # DISPLAY RESULTS
    # -----------------------------
    st.markdown("## ⚠️ Step 3: Overall PCOS Risk Assessment")

    st.progress(min(total_risk_score / 20, 1.0))

    st.markdown(
        f"<h3 style='color:{risk_color}'>Risk Level: {risk_level}</h3>",
        unsafe_allow_html=True
    )

    st.markdown("## 🔍 Step 4: Detected PCOS Pattern")
    st.success(f"**Detected Pattern:** {pcos_type}")
    st.write(explanation)

    st.markdown("### 🔎 Key Contributing Factors")

    if cycle_signal >= 3:
        st.write("- Significant menstrual irregularity detected")
    if insulin_signal >= 4:
        st.write("- Strong metabolic / insulin-related signals")
    if stress_signal >= 6:
        st.write("- High stress and adrenal load")
    if androgen_signal >= 3:
        st.write("- Noticeable androgen-related symptoms")
    if inflammation_signal >= 3:
        st.write("- Pain and inflammation indicators present")

    st.info(
        "This is an early pattern-detection system for awareness only. "
        "It is not a medical diagnosis."
    )
    # -----------------------------
    # STEP 5: FOLLOW-UP & NEXT STEPS
    # -----------------------------
    st.markdown("## 🔁 Step 5: Suggested Follow-up")

    if risk_level == "High Risk":
        st.error(
            "### Immediate Attention Recommended\n"
            "- Consider consulting a gynecologist or endocrinologist\n"
            "- Track menstrual cycle, mood, sleep, and diet daily for 4–6 weeks\n"
            "- Avoid delaying evaluation if symptoms worsen"
        )

    elif risk_level == "Moderate Risk":
        st.warning(
            "### Active Monitoring Suggested\n"
            "- Track symptoms weekly (cycle regularity, stress, cravings)\n"
            "- Introduce lifestyle adjustments (sleep, diet, stress reduction)\n"
            "- Reassess patterns in 3–4 weeks"
        )

    else:
        st.success(
            "### Preventive Care Advised\n"
            "- Maintain current healthy routines\n"
            "- Monitor cycle and stress levels monthly\n"
            "- Seek medical advice if new symptoms appear"
        )

    # PCOS-type specific note
    st.markdown("### 🧭 PCOS-Type Focus")

    if "Adrenal" in pcos_type:
        st.write(
            "- Emphasize stress management, sleep hygiene, and burnout prevention\n"
            "- Cortisol regulation plays a key role in this pattern"
        )

    elif "Insulin" in pcos_type:
        st.write(
            "- Focus on blood sugar stability and dietary consistency\n"
            "- Metabolic regulation is central to this pattern"
        )

    elif "Lean" in pcos_type:
        st.write(
            "- Hormonal regulation may occur without weight-related indicators\n"
            "- Cycle tracking is especially important"
        )

    elif "Inflammatory" in pcos_type:
        st.write(
            "- Address pain, fatigue, and inflammatory triggers\n"
            "- Recovery and rest cycles are important"
        )
