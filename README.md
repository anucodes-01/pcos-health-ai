# PCOS Health AI

**A Safe, Explainable Women's Health Companion**

PCOS Health AI is a production-grade, hackathon-winning female health web platform designed to help users understand their body signals, reduce confusion and anxiety, decide whether doctor consultation is needed, receive structured education, get lifestyle guidance, generate doctor-ready summaries, and feel emotionally supported.

> ⚠️ **This tool is for awareness and support only. It does not provide medical diagnosis.**

---

## 🎯 Project Overview

This project is a Streamlit-based web application focused on female reproductive and hormonal health. The platform is:

- **Non-diagnostic** - Never claims to diagnose diseases
- **Ethical** - Transparent, respectful, inclusive
- **Explainable** - All decisions have clear reasoning
- **Supportive** - Emotional support, not clinical replacement
- **Taboo-free** - Normalizes conversations about reproductive health
- **Clinically respectful** - Supports, not replaces, healthcare professionals

---

## 🎯 Who This Is For

- **Teenagers (13–18)** confused about periods and pain
- **Young adults (19–30)** noticing irregular cycles, acne, weight change
- **Women (31–45)** with diagnosed or suspected PCOS/PCOD
- Users with reports who want lifestyle clarity
- Users unsure whether symptoms are "normal"

---

## 🧠 How the System Works

### 1. Structured Health Input
- Menstrual patterns
- Hormonal & metabolic signals
- Stress, sleep, and mood indicators
- Pain and lifestyle factors

### 2. Explainable AI Decision Engine
- Rule-based, transparent logic (no black-box ML)
- Detects PCOS subtypes:
  - Insulin-resistant PCOS
  - Adrenal PCOS (stress-driven)
  - Lean PCOS
  - Inflammatory PCOS
- Computes overall risk level (Low / Moderate / High)
- AI confidence score (based on signal strength)

### 3. Decision Guidance
- Clearly indicates whether medical consultation is recommended
- Explains *why* the decision was made (signal-level explainability)

### 4. Condition Education
- Educational panels on PCOS, PCOD, and Endometriosis
- Non-diagnostic, awareness-focused content

### 5. Personalized Lifestyle Focus
- Stress, metabolic, hormonal, or recovery-oriented guidance
- Only lifestyle-level recommendations (no medications or supplements)

### 6. Doctor-Ready Report Export
- Text-based health summary
- Downloadable and easy to share with healthcare professionals

---

## 🧩 Technical Architecture

```
pcos-health-ai/
│
├── app.py                      # Main entry point (navigation)
├── README.md                   # This file
├── ARCHITECTURE.md            # Detailed architecture blueprint
├── PAGES_SPECIFICATION.md     # Page-by-page specifications
├── requirements.txt            # Python dependencies
│
├── .streamlit/
│   └── config.toml            # Streamlit theme & configuration
│
├── pages/                      # Multi-page Streamlit app
│   ├── 1_🏠_Home.py
│   ├── 2_🔍_Health_Check.py
│   ├── 3_💬_AI_Assistant.py
│   ├── 4_📚_Learn_Conditions.py
│   ├── 5_🌱_Lifestyle_Plan.py
│   ├── 6_📊_Trackers.py
│   ├── 7_👥_Community.py
│   └── 8_🩺_Find_Help.py
│
└── utils/                      # Core logic modules
    ├── decision_engine.py     # PCOS pattern detection logic
    ├── chat_engine.py         # Guided chatbot flow
    ├── prompt_library.py      # Question sets & prompts
    └── report_generator.py    # Report formatting
```

### Architecture Principles

- **Strict Separation of Concerns**: UI (pages/) vs Logic (utils/)
- **Modular Design**: Each utility module has a single, well-defined responsibility
- **Explainable AI**: Rule-based, transparent logic (no black-box ML)
- **Stateless Design**: No user data persistence (session-based only)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd pcos-health-ai
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Access the application:**
   - The app will open in your default web browser
   - Default URL: `http://localhost:8501`

### Deployment

#### Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Set the main file to `app.py`
5. Deploy!

---

## 📄 Features

### 1️⃣ Home Page
- Trust-building messaging
- Clear value proposition
- Feature discovery
- Navigation to other pages

### 2️⃣ Health Check (Core Feature)
- Structured signal collection
- Explainable assessment
- PCOS subtype detection
- Risk level calculation
- Doctor consultation guidance
- Report export

### 3️⃣ AI Health Assistant
- Guided chatbot flow
- Question-based conversation
- Age-group specific prompts
- Clarification and reassurance
- Next-step suggestions

### 4️⃣ Learn Conditions
- Educational content about PCOS, PCOD, Endometriosis
- Myths vs facts
- When to seek help
- Normal vs not normal

### 5️⃣ Lifestyle Plan
- Personalized guidance based on health check
- Pattern-specific recommendations
- Lifestyle-focused only (no medications/supplements)

### 6️⃣ Trackers
- Period tracking
- Cycle logging
- Pain notes
- Session-based storage

### 7️⃣ Community
- Safe space for support
- Demo/static posts
- Anonymous by default
- Community guidelines

### 8️⃣ Find Help
- Demo doctor listings
- Teleconsult information
- Preparation tips
- Self-advocacy guidance

---

## 🛡️ Safety & Ethics

### Disclaimers
- **Non-Diagnostic Statement**: This tool is for awareness and support only. It does not provide medical diagnosis.
- **Ethical Use Statement**: PCOS Health AI is designed to support, not replace, healthcare professionals.
- **Privacy Statement**: We do not store your personal data. All information is session-based only.

### Language Rules
- Uses "may indicate" rather than "diagnoses"
- Provides "guidance" not "prescriptions"
- Encourages consultation with healthcare professionals
- Never makes medical claims

---

## 📊 Technical Details

### Decision Engine
- Rule-based logic (no black-box ML)
- Transparent signal scoring
- PCOS subtype detection
- Risk level calculation
- Doctor consultation logic

### Chat Engine
- Guided conversation flow
- Age-group specific prompts
- Rule-based responses
- Next-step suggestions

### Report Generator
- User-friendly summaries
- Doctor-ready clinical summaries
- Non-diagnostic language
- Downloadable text format

---

## 🎨 UI/UX Guidelines

- **Soft pastel theme** - Calm, inclusive colors
- **High contrast but calm** - Readable but soothing
- **Rounded cards** - Modern, friendly design
- **Icons for clarity** - Visual communication
- **Minimal red** - Only for urgent alerts
- **Inclusive language** - Respectful, supportive
- **Mobile-friendly** - Responsive design

---

## 📚 Documentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Complete architecture blueprint
- **[PAGES_SPECIFICATION.md](PAGES_SPECIFICATION.md)** - Detailed page specifications
- **[README.md](README.md)** - This file

---

## 🔮 Future Scope (Not Implemented)

- ML-based prediction models
- PDF report export
- Wearable integration
- Teleconsult booking
- Events & workshops
- Video consultations
- More conditions (thyroid, anemia, menopause)

---

## 🤝 Contributing

This is a hackathon project. Contributions, feedback, and suggestions are welcome!

---

## 📄 License

See [LICENSE](LICENSE) file for details.

---

## ⚠️ Important Disclaimer

**This tool is for awareness and support only. It does not provide medical diagnosis, prescription, or treatment. Always consult qualified healthcare professionals for medical advice, diagnosis, and treatment. In case of emergency, contact emergency services immediately.**

---

**PCOS Health AI - A Safe, Explainable Women's Health Companion**
