# pcos-health-ai
# PCOS Health AI

PCOS Health AI is an **explainable, decision-support system** designed to help
women understand menstrual, hormonal, metabolic, and pain-related health patterns.

It is built to reduce confusion around conditions such as **PCOS, PCOD, and Endometriosis**
and to guide users on **when lifestyle management is sufficient and when medical consultation is recommended**.

> ⚠️ This tool is for awareness and support only. It does not provide medical diagnosis.

---

## 🎯 Who This Is For

- Women who are unsure whether their symptoms require a doctor
- Users already diagnosed with PCOS/PCOD seeking lifestyle guidance
- Individuals wanting a clear, doctor-friendly health summary
- Early exploration before clinical consultation

---

## 🧠 How the System Works

1. **Structured Health Input**
   - Menstrual patterns
   - Hormonal & metabolic signals
   - Stress, sleep, and mood indicators
   - Pain and lifestyle factors

2. **Explainable AI Decision Engine**
   - Rule-based, transparent logic (no black-box ML)
   - Detects PCOS subtypes:
     - Adrenal PCOS (stress-driven)
     - Insulin-Resistant PCOS
     - Lean PCOS
     - Inflammatory PCOS
   - Computes overall risk level (Low / Moderate / High)

3. **Decision Guidance**
   - Clearly indicates whether medical consultation is recommended
   - Explains *why* the decision was made (signal-level explainability)

4. **Condition Education**
   - Educational panels on:
     - PCOS
     - PCOD
     - Endometriosis
   - Non-diagnostic, awareness-focused content

5. **Personalized Lifestyle Focus**
   - Stress, metabolic, hormonal, or recovery-oriented guidance
   - Only lifestyle-level recommendations (no medications or supplements)

6. **Doctor-Ready Report Export**
   - Text-based health summary
   - Downloadable and easy to share with healthcare professionals

---

## 🧩 Technical Architecture

# PCOS Health AI

PCOS Health AI is an **explainable, decision-support system** designed to help
women understand menstrual, hormonal, metabolic, and pain-related health patterns.

It is built to reduce confusion around conditions such as **PCOS, PCOD, and Endometriosis**
and to guide users on **when lifestyle management is sufficient and when medical consultation is recommended**.

> ⚠️ This tool is for awareness and support only. It does not provide medical diagnosis.

---

## 🎯 Who This Is For

- Women who are unsure whether their symptoms require a doctor
- Users already diagnosed with PCOS/PCOD seeking lifestyle guidance
- Individuals wanting a clear, doctor-friendly health summary
- Early exploration before clinical consultation

---

## 🧠 How the System Works

1. **Structured Health Input**
   - Menstrual patterns
   - Hormonal & metabolic signals
   - Stress, sleep, and mood indicators
   - Pain and lifestyle factors

2. **Explainable AI Decision Engine**
   - Rule-based, transparent logic (no black-box ML)
   - Detects PCOS subtypes:
     - Adrenal PCOS (stress-driven)
     - Insulin-Resistant PCOS
     - Lean PCOS
     - Inflammatory PCOS
   - Computes overall risk level (Low / Moderate / High)

3. **Decision Guidance**
   - Clearly indicates whether medical consultation is recommended
   - Explains *why* the decision was made (signal-level explainability)

4. **Condition Education**
   - Educational panels on:
     - PCOS
     - PCOD
     - Endometriosis
   - Non-diagnostic, awareness-focused content

5. **Personalized Lifestyle Focus**
   - Stress, metabolic, hormonal, or recovery-oriented guidance
   - Only lifestyle-level recommendations (no medications or supplements)

6. **Doctor-Ready Report Export**
   - Text-based health summary
   - Downloadable and easy to share with healthcare professionals

---

## 🧩 Technical Architecture

app.py → Streamlit UI
utils/decision_engine.py → Core AI & decision logic
.streamlit/config.toml → UI theme


- Clean separation of UI and logic
- Fully explainable decision-making
- ML-ready architecture (future extension)

---

## 🛡️ Safety & Ethics

- No medical diagnosis claims
- No prescription or supplement advice
- Transparent logic for every decision
- Designed to support, not replace, healthcare professionals

---

## 🚀 Future Scope

- Longitudinal symptom tracking
- ML-based progression modeling (with real datasets)
- PDF report export
- Clinician-facing dashboards