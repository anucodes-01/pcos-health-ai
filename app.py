import streamlit as st

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Female Health AI",
    page_icon="🌸",
    layout="centered"
)

# -----------------------------------
# Sidebar Navigation
# -----------------------------------
st.sidebar.title("🌸 Female Health AI")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Health Check", "Follow-up", "About"]
)

# -----------------------------------
# HOME PAGE
# -----------------------------------
if page == "Home":
    st.title("Female Healthcare Support System")
    st.subheader("PCOS / PCOD Early Awareness Tool")

    st.write("""
    This application helps women gain **early awareness**
    about PCOS/PCOD and related health concerns.

    **Workflow followed:**
    Ask → Detect → Respond → Follow-up
    """)

    st.info("⚠️ This tool is for awareness only. It is NOT a medical diagnosis.")

# -----------------------------------
# HEALTH CHECK PAGE
# -----------------------------------
elif page == "Health Check":
    st.title("🩺 Health Check")

    st.subheader("Basic Information")
    age = st.slider("Age", 13, 50, 22)
    height = st.number_input("Height (cm)", 130, 200, 160)
    weight = st.number_input("Weight (kg)", 35, 120, 55)

    st.subheader("Symptoms")
    irregular_periods = st.checkbox("Irregular periods")
    acne = st.checkbox("Acne issues")
    hair_issues = st.checkbox("Hair fall / excessive hair growth")
    fatigue = st.checkbox("Frequent fatigue")
    mood_swings = st.checkbox("Mood swings / anxiety")
    sleep_issues = st.checkbox("Sleep problems")

    st.subheader("Lifestyle")
    stress_level = st.slider("Stress level (1 = low, 10 = high)", 1, 10, 5)
    exercise = st.selectbox(
        "Exercise frequency",
        ["Rarely", "1–2 times/week", "3–5 times/week", "Daily"]
    )

    if st.button("Check Health Risk"):
        # Mock logic (temporary)
        if irregular_periods and (fatigue or acne):
            risk = "High"
            pattern = "Hormonal / Lifestyle related"
        elif fatigue or mood_swings or stress_level > 6:
            risk = "Medium"
            pattern = "Stress & lifestyle related"
        else:
            risk = "Low"
            pattern = "Low visible risk"

        st.subheader("📊 Result")

        if risk == "High":
            st.error("🔴 High Risk")
        elif risk == "Medium":
            st.warning("🟡 Medium Risk")
        else:
            st.success("🟢 Low Risk")

        st.write(f"**Dominant pattern:** {pattern}")
        st.info("Please consult a healthcare professional for medical advice.")

# -----------------------------------
# FOLLOW-UP PAGE
# -----------------------------------
elif page == "Follow-up":
    st.title("📌 Follow-up & Guidance")

    st.write("""
    Taking care of hormonal health is a long-term process.
    Small, consistent steps can make a big difference.
    """)

    st.markdown("""
    **Lifestyle Tips**
    - Maintain a balanced diet
    - Exercise regularly
    - Reduce stress through mindfulness or yoga
    - Get adequate sleep

    **When to Consult a Doctor**
    - Persistent irregular periods
    - Severe fatigue or pain
    - Sudden weight changes
    """)

    st.success("💚 You are not alone. Awareness is the first step.")

# -----------------------------------
# ABOUT PAGE
# -----------------------------------
elif page == "About":
    st.title("ℹ️ About This Project")

    st.write("""
    This project is a **hackathon prototype** built to demonstrate
    how technology can support **female healthcare awareness**.

    **Technology Used**
    - Python
    - Streamlit

    **Disclaimer**
    This application is for educational purposes only.
    """)
