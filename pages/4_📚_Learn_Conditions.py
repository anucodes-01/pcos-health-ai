"""
Learn Conditions - Educational content about PCOS, PCOD, and Endometriosis
"""

import streamlit as st

st.set_page_config(
    page_title="PCOS Health AI - Learn Conditions",
    page_icon="📚",
    layout="wide"
)

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
    
    st.markdown("### Common Symptoms")
    st.write("Similar to PCOS, including irregular periods, hormonal imbalances, and metabolic concerns.")
    
    st.markdown("### Lifestyle Factors")
    st.write("""
    PCOD is often more responsive to lifestyle modifications including:
    - Balanced nutrition
    - Regular physical activity
    - Stress management
    - Adequate sleep
    """)
    
    st.markdown("### When to Seek Help")
    st.write("If symptoms persist despite lifestyle changes or significantly affect your daily life.")

# Endometriosis Panel
with st.expander("🔹 Endometriosis"):
    st.markdown("### What is Endometriosis?")
    st.write("""
    Endometriosis involves tissue similar to the uterine lining growing outside 
    the uterus. It can cause significant pain and other symptoms.
    
    Severe or disabling menstrual pain is not normal and should be evaluated.
    """)
    
    st.markdown("### Common Symptoms")
    st.markdown("""
    - Severe menstrual pain
    - Pain during intercourse
    - Painful bowel movements
    - Heavy or irregular bleeding
    - Fatigue
    - Infertility concerns
    """)
    
    st.markdown("### Why Diagnosis is Often Delayed")
    st.write("""
    Endometriosis symptoms can be mistaken for normal period pain. 
    It often takes years to receive a diagnosis, which can delay appropriate care.
    """)
    
    st.markdown("### Normal Pain vs Concerning Pain")
    st.success("**Normal:** Mild to moderate period pain that's manageable")
    st.error("**Concerning:** Severe pain that affects daily life, pain outside of periods")
    
    st.markdown("### When to Seek Help")
    st.write("""
    If you experience severe or disabling period pain, pain at other times in your cycle, 
    or pain that affects your daily activities, consider consulting a healthcare provider.
    """)

# Resources Section
st.markdown("---")
st.markdown("### 📖 Additional Resources")
st.info("""
🚀 **Coming Soon:** Links to reputable sources, support groups, and additional educational materials.
""")

# Link to Health Check
st.markdown("---")
st.markdown("### 💡 Next Steps")
if st.button("🔍 Take Health Check", type="primary", use_container_width=True):
    st.switch_page("pages/2_🔍_Health_Check.py")

# Disclaimer
st.markdown("---")
st.error("⚠️ **Disclaimer:** This content is for educational purposes only. Always consult healthcare professionals for medical advice.")
