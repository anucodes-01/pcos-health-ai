"""
Resources & FAQ - Comprehensive resource library and frequently asked questions
"""

import streamlit as st

st.set_page_config(
    page_title="PCOS Health AI - Resources & FAQ",
    page_icon="📖",
    layout="wide"
)

st.title("Resources & FAQ")
st.markdown("### Comprehensive Information and Support")

# FAQ Section
st.markdown("---")
st.markdown("### Frequently Asked Questions")

faq_items = [
    {
        "question": "How accurate is the health check assessment?",
        "answer": "Our health check uses explainable, rule-based logic to analyze your symptoms. It provides pattern recognition and risk assessment, but it is not a medical diagnosis. The results are designed to help you understand your health patterns and guide you on when to consult healthcare professionals."
    },
    {
        "question": "Is my data stored or shared?",
        "answer": "No. We do not store any personal data. All information is processed in your browser session only and is not saved or transmitted to any server. Your privacy is our priority."
    },
    {
        "question": "Can this tool diagnose PCOS?",
        "answer": "No. This tool does not provide medical diagnosis. It helps identify patterns and signals that may indicate the need for professional medical evaluation. Only qualified healthcare providers can diagnose medical conditions."
    },
    {
        "question": "What should I do if the assessment suggests I see a doctor?",
        "answer": "If the assessment recommends medical consultation, we suggest: 1) Download your health summary report, 2) Schedule an appointment with a healthcare provider, 3) Bring the report to your appointment, 4) Be prepared to discuss your symptoms and concerns."
    },
    {
        "question": "How often should I use the health check?",
        "answer": "You can use the health check whenever you notice changes in your symptoms or patterns. We recommend reassessing every 2-3 months or if you experience significant changes in your health."
    },
    {
        "question": "Is this tool suitable for teenagers?",
        "answer": "Yes. Our platform is designed to be inclusive and supportive for users aged 13 and above. However, teenagers should always involve a parent or guardian when making healthcare decisions."
    },
    {
        "question": "What lifestyle changes are recommended?",
        "answer": "Lifestyle recommendations are personalized based on your health check results. They may include stress management, balanced nutrition, regular physical activity, and adequate sleep. All recommendations are lifestyle-focused and do not include medications or supplements."
    },
    {
        "question": "Can I use this tool if I'm already diagnosed with PCOS?",
        "answer": "Yes. The platform can help you track patterns, understand your symptoms better, and generate reports to share with your healthcare provider. It's designed to support, not replace, ongoing medical care."
    }
]

for i, faq in enumerate(faq_items):
    with st.expander(f"Q{i+1}: {faq['question']}"):
        st.write(faq['answer'])

# Resources Section
st.markdown("---")
st.markdown("### Educational Resources")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background: linear-gradient(135deg, #F8E8F0 0%, #FFE5F1 100%); border-left: 4px solid #D9469F;'>
        <h3 style='color: #D9469F; margin-top: 0;'>Understanding PCOS</h3>
        <ul style='color: #2D1B3D;'>
            <li>PCOS Foundation Resources</li>
            <li>Hormonal Health Guides</li>
            <li>Symptom Tracking Methods</li>
            <li>Lifestyle Management Tips</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='padding: 20px; border-radius: 10px; background: linear-gradient(135deg, #FFE5F1 0%, #F0E5F5 100%); border-left: 4px solid #D9469F;'>
        <h3 style='color: #D9469F; margin-top: 0;'>Support & Community</h3>
        <ul style='color: #2D1B3D;'>
            <li>Support Group Directories</li>
            <li>Online Communities</li>
            <li>Mental Health Resources</li>
            <li>Advocacy Organizations</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Quick Tips Section
st.markdown("---")
st.markdown("### Quick Health Tips")

tips = [
    "Track your cycle patterns for at least 3 months to identify trends",
    "Maintain regular meal times to support blood sugar stability",
    "Prioritize 7-9 hours of quality sleep each night",
    "Practice stress-reduction techniques like deep breathing or meditation",
    "Stay hydrated - aim for 8-10 glasses of water daily",
    "Engage in moderate physical activity most days of the week",
    "Keep a symptom journal to identify patterns and triggers",
    "Don't skip meals - regular nutrition supports hormonal balance"
]

st.markdown("""
<div style='padding: 20px; border-radius: 10px; background: linear-gradient(135deg, #FFF5F8 0%, #F8E8F0 100%);'>
    <ul style='color: #2D1B3D;'>
""", unsafe_allow_html=True)

for tip in tips:
    st.markdown(f"<li style='margin-bottom: 8px;'>{tip}</li>", unsafe_allow_html=True)

st.markdown("</ul></div>", unsafe_allow_html=True)

# Glossary Section
st.markdown("---")
st.markdown("### Health Terms Glossary")

glossary_terms = {
    "PCOS": "Polycystic Ovary Syndrome - a hormonal condition affecting the ovaries",
    "PCOD": "Polycystic Ovarian Disease - often used interchangeably with PCOS",
    "Insulin Resistance": "When cells don't respond well to insulin, affecting blood sugar",
    "Androgens": "Male hormones present in both men and women",
    "Endometriosis": "Condition where tissue similar to uterine lining grows outside the uterus",
    "LH/FSH Ratio": "Luteinizing hormone to Follicle-stimulating hormone ratio - used in PCOS diagnosis",
    "HbA1c": "Blood test measuring average blood sugar levels over 2-3 months"
}

for term, definition in glossary_terms.items():
    with st.expander(term):
        st.write(definition)

# Disclaimer
st.markdown("---")
st.markdown("""
<div style='padding: 16px; border-radius: 8px; background-color: #FFE5F1; border-left: 4px solid #D9469F;'>
    <p style='color: #8B4A6B; margin: 0;'><strong>Note:</strong> Resources and information provided are for educational purposes only. 
    Always consult healthcare professionals for medical advice and diagnosis.</p>
</div>
""", unsafe_allow_html=True)
