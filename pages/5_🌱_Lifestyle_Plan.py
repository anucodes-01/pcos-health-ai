"""
Lifestyle Plan - Personalized lifestyle guidance based on health check results
"""

import streamlit as st

st.set_page_config(
    page_title="PCOS Health AI - Lifestyle Plan",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Lifestyle Plan")
st.markdown("### Personalized Lifestyle Guidance")

# Check if user has completed Health Check
if 'health_check_result' not in st.session_state:
    st.warning("⚠️ Please complete the Health Check first to get your personalized plan.")
    if st.button("🔍 Go to Health Check", type="primary", use_container_width=True):
        st.switch_page("pages/2_🔍_Health_Check.py")
    st.stop()

result = st.session_state.get('health_check_result', {})

# Check if doctor consultation is urgent
if result.get('doctor_needed', False):
    st.error("""
    ⚠️ **Medical consultation is recommended before focusing on lifestyle changes.**
    
    Please consult with a healthcare professional first. After consultation, 
    you can return here for lifestyle support.
    """)
    if st.button("🩺 Find Help", type="primary", use_container_width=True):
        st.switch_page("pages/8_🩺_Find_Help.py")
    st.stop()

# Display personalized plan based on PCOS type
pcos_type = result.get('pcos_type', 'Low / Unclear PCOS Pattern')

if "Adrenal" in pcos_type or "Stress" in pcos_type:
    st.success("### 🧘 Focus Area: Stress & Nervous System Regulation")
    st.markdown("""
    **Priority Actions:**
    - Prioritize consistent sleep schedule (7-9 hours)
    - Reduce chronic stress through mindfulness or gentle movement
    - Avoid overtraining - balance activity with recovery
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
st.warning("""
⚠️ **Note:** These recommendations are lifestyle-focused only. 
They do not replace medical advice. Always consult healthcare professionals 
before making significant changes.
""")

# Link back to Health Check
st.markdown("---")
if st.button("🔍 Review Health Check Results", use_container_width=True):
    st.switch_page("pages/2_🔍_Health_Check.py")
