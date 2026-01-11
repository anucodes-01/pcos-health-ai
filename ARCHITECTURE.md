# PCOS Health AI – Complete Architecture Blueprint

**Project:** PCOS Health AI – A Safe, Explainable Women's Health Companion  
**Architecture Version:** 1.0  
**Purpose:** Production-grade, hackathon-winning female health platform

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture Principles](#architecture-principles)
3. [File Structure & Organization](#file-structure--organization)
4. [Page-by-Page Feature Specification](#page-by-page-feature-specification)
5. [User Journey Flows](#user-journey-flows)
6. [Technical Implementation Guide](#technical-implementation-guide)
7. [UI/UX Guidelines](#uiux-guidelines)
8. [Safety & Ethics Framework](#safety--ethics-framework)
9. [Deployment Strategy](#deployment-strategy)

---

## 🎯 Project Overview

### Mission Statement
PCOS Health AI is a non-diagnostic, ethical, explainable platform designed to help users:
- Understand their body signals
- Reduce confusion and anxiety
- Decide whether doctor consultation is needed
- Receive structured education
- Get lifestyle guidance
- Generate doctor-ready summaries
- Feel emotionally supported

### Core Principles
- **Non-diagnostic**: Never claims to diagnose diseases
- **Ethical**: Transparent, respectful, inclusive
- **Explainable**: All decisions have clear reasoning
- **Supportive**: Emotional support, not clinical replacement
- **Taboo-free**: Normalizes conversations about reproductive health
- **Clinically respectful**: Supports, not replaces, healthcare professionals

---

## 🏗️ Architecture Principles

### 1. Strict Separation of Concerns

```
UI Layer (pages/)           → Pure presentation, user interaction
Logic Layer (utils/)        → Business rules, decision making
Data Layer (none)           → No persistence (stateless design)
```

### 2. Modular Design

Each utility module has a single, well-defined responsibility:
- `decision_engine.py` → Health signal analysis & scoring
- `chat_engine.py` → Guided chatbot conversation flow
- `prompt_library.py` → Standardized question sets
- `report_generator.py` → Report formatting & export

### 3. Explainable AI

- **No black-box ML models**
- Rule-based, transparent logic
- Every decision is traceable
- Confidence scores derived from signal strength
- Clear explanation for every output

### 4. Stateless Design

- No user data persistence
- Session-based state only
- No database required
- Privacy-first approach

---

## 📁 File Structure & Organization

```
pcos-health-ai/
│
├── app.py                      # Main entry point (navigation only)
├── README.md                   # Project documentation
├── ARCHITECTURE.md            # This file
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
    ├── report_generator.py    # Report formatting
    └── ui_components.py       # Reusable UI components (optional)
```

---

## 📄 Page-by-Page Feature Specification

### 1️⃣ HOME PAGE (`pages/1_🏠_Home.py`)

**Purpose:** Trust-building, clear value proposition, calm entry point

**Layout:**
```
┌─────────────────────────────────────────┐
│  Hero Section                            │
│  - Title: PCOS Health AI                │
│  - Subtitle: A Safe, Explainable        │
│    Women's Health Companion              │
│  - Tagline: Understand • Decide • Feel  │
│    Supported                             │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  What We Do / Don't Do Section          │
│  - ✅ What this tool DOES               │
│  - ❌ What this tool DOES NOT           │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  Feature Cards (3-4 cards in grid)      │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │ 🔍   │ │ 💬   │ │ 📚   │ │ 👥   │  │
│  │Health│ │ AI   │ │Learn │ │Commu │  │
│  │Check │ │Assist│ │Cond. │ │nity  │  │
│  └──────┘ └──────┘ └──────┘ └──────┘  │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  Embedded Video Section                 │
│  - YouTube iframe (explainer video)     │
│  - "How PCOS Health AI Works"           │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  CTA Buttons                            │
│  - [Start Health Check] (primary)       │
│  - [Talk to AI Assistant] (secondary)   │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  Disclaimer Banner (persistent)         │
│  - Non-diagnostic warning               │
│  - Ethical use statement                │
└─────────────────────────────────────────┘
```

**Key Features:**
- Trust-building messaging
- Clear disclaimers
- Feature discovery
- Video integration
- Navigation to other pages

**Tone:** Calm, inclusive, non-clinical, supportive

---

### 2️⃣ HEALTH CHECK (`pages/2_🔍_Health_Check.py`)

**Purpose:** Core feature - structured signal collection & explainable assessment

**Flow:**
```
Step 1: Personal & Cycle Information
├── Age (slider: 13-50)
├── Cycle regularity (selectbox)
├── Period pain (radio)
└── Menstrual history (optional)

Step 2: Metabolic & Physical Signals
├── Weight changes (selectbox)
├── Sugar cravings (radio)
├── Facial/body hair (radio)
├── Acne severity (radio)
└── Hair loss (radio)

Step 3: Mental & Stress Signals
├── Stress level (slider: 0-10)
├── Sleep quality (selectbox)
├── Mood changes (radio)
└── Anxiety/depression indicators (radio)

Step 4: Lifestyle Factors
├── Activity level (selectbox)
├── Diet pattern (selectbox)
├── Sleep schedule (selectbox)
└── Work stress (selectbox)

Step 5: Optional Family History
└── PCOS/PCOD in family (radio)

[Analyze Button]

Results Section:
├── Risk Assessment (visual indicator)
├── PCOS Pattern Detection
├── AI Confidence Score
├── Contributing Factors
├── Doctor Consultation Guidance
├── Lifestyle Recommendations
└── Report Export
```

**Logic Flow:**
1. Collect all inputs → Store in session state
2. Call `decision_engine.analyze_pcos_signals()` → Get results
3. Display results with visual indicators
4. Generate report using `report_generator.generate_summary()`
5. Offer download option

**Outputs:**
- Risk Level: Low / Moderate / High (with color coding)
- PCOS Type: Insulin-Resistant / Adrenal / Lean / Inflammatory / Unclear
- Confidence Score: 0-100% (explainable)
- Contributing Factors: List of key signals
- Doctor Consultation: Recommended / Not Urgent
- Lifestyle Focus: Pattern-specific guidance

**Key Requirements:**
- All logic in `utils/decision_engine.py`
- UI only in page file
- Transparent scoring
- No medical diagnosis language

---

### 3️⃣ AI HEALTH ASSISTANT (`pages/3_💬_AI_Assistant.py`)

**Purpose:** Guided chatbot for clarification & emotional support

**Design Philosophy:**
- NOT free-text chat
- Guided, clickable flow
- Question cards
- 5-step journey

**Flow:**
```
Step 1: Age Group Selection
├── [Teenager (13-18)]
├── [Young Adult (19-30)]
└── [Adult (31-45)]

Step 2: Concern Category
├── [Menstrual Issues]
├── [Pain & Discomfort]
├── [Hormonal Changes]
├── [Mood & Mental Health]
├── [Weight & Metabolism]
└── [Other Concerns]

Step 3: Guided Questions
├── Display 3-5 relevant questions from prompt_library
├── Clickable question cards
├── Answer collection (radio/selectbox)
└── [Continue] button

Step 4: Clarification & Reassurance
├── AI response (from chat_engine)
├── Explanation in plain language
├── "This is normal when..." or "This may indicate..."
└── No diagnosis language

Step 5: Next Steps
├── Suggested actions
├── Link to Health Check (if relevant)
├── Link to Learn Conditions
└── "When to see a doctor" guidance
```

**Implementation:**
- Questions from `utils/prompt_library.py`
- Logic in `utils/chat_engine.py`
- UI only in page file
- Session state for conversation flow

---

### 4️⃣ LEARN CONDITIONS (`pages/4_📚_Learn_Conditions.py`)

**Purpose:** Educational content without fear-mongering

**Sections:**

**PCOS Panel:**
- What is PCOS?
- Common symptoms
- Why it's misunderstood
- Normal vs not normal
- When to seek help
- Myths vs facts

**PCOD Panel:**
- What is PCOD?
- Difference from PCOS
- Common symptoms
- Lifestyle factors
- When to seek help
- Myths vs facts

**Endometriosis Panel:**
- What is Endometriosis?
- Common symptoms
- Why diagnosis is delayed
- Normal pain vs concerning pain
- When to seek help
- Myths vs facts

**Additional Resources:**
- Links to reputable sources
- Community resources
- Support groups

**Tone:** Educational, reassuring, non-diagnostic

---

### 5️⃣ LIFESTYLE PLAN (`pages/5_🌱_Lifestyle_Plan.py`)

**Purpose:** Actionable guidance (only shown if doctor consultation not urgent)

**Access Logic:**
- Only accessible if user has completed Health Check
- Check if `doctor_needed == False` in session state
- If urgent, redirect with message

**Plan Categories:**

**1. Stress Regulation (for Adrenal PCOS)**
- Sleep consistency
- Stress management techniques
- Recovery practices
- Activity recommendations

**2. Blood Sugar Stability (for Insulin-Resistant PCOS)**
- Meal timing
- Food choices
- Snacking strategies
- Exercise timing

**3. Hormonal Balance (for Lean PCOS)**
- Cycle tracking
- Nutrition balance
- Recovery focus
- Moderate activity

**4. Recovery & Inflammation (for Inflammatory PCOS)**
- Rest practices
- Anti-inflammatory foods
- Gentle movement
- Pain management (non-medical)

**Rules:**
- No supplements mentioned
- No medications mentioned
- No medical claims
- Lifestyle-focused only

---

### 6️⃣ TRACKERS (`pages/6_📊_Trackers.py`)

**Purpose:** Basic habit awareness & symptom tracking

**Features:**

**Period Tracker:**
- Last period date (date picker)
- Cycle length (auto-calculated if multiple entries)
- Notes (optional)
- [Log Period] button

**Cycle Logging:**
- Visual calendar (simple)
- Pain level (1-5 scale)
- Mood notes
- Symptoms checklist

**Pain Notes:**
- Date
- Severity (1-10)
- Location
- Notes

**Future Scope Note:**
- "Advanced tracking features coming soon"
- Link to request features

**Implementation:**
- Session state only (no persistence)
- Simple UI components
- Clear "coming soon" messaging

---

### 7️⃣ COMMUNITY (`pages/7_👥_Community.py`)

**Purpose:** Taboo-free emotional support space

**Design:**
- Anonymous by default
- Optional identity reveal (username)
- Demo/static posts
- Safety rules prominently displayed

**Layout:**
```
┌─────────────────────────────────────────┐
│  Community Guidelines                   │
│  - Be respectful                        │
│  - No medical advice                    │
│  - Anonymous by default                 │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  Demo Posts (static examples)           │
│  ┌───────────────────────────────────┐ │
│  │ Anonymous • 2 days ago            │ │
│  │ "Finally found people who get it" │ │
│  │ 💬 5 • 👍 12                      │ │
│  └───────────────────────────────────┘ │
│  ... (3-5 demo posts)                   │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  [Create Post] Button                   │
│  (Opens form, saves to session state)   │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  Moderation Disclaimer                  │
│  - Posts are reviewed                  │
│  - This is a demo/static space         │
└─────────────────────────────────────────┘
```

**Safety Features:**
- Clear rules
- Moderation disclaimer
- No personal data collection
- Demo/static content only

---

### 8️⃣ FIND HELP (`pages/8_🩺_Find_Help.py`)

**Purpose:** Reduce friction to real care

**Sections:**

**Nearby Gynecologists (Demo):**
- 5 static/demo entries
- Name, location, specializations
- "Demo data - Not endorsements" disclaimer
- Location placeholder (future: geolocation)

**Teleconsult Options:**
- Mention teleconsult platforms
- "Future scope" note
- General guidance

**When to See a Doctor:**
- Clear indicators
- Emergency situations
- Routine check-ups

**Preparation Tips:**
- What to bring
- Questions to ask
- How to advocate for yourself

**Disclaimer:**
- Not endorsements
- Demo data
- User should research independently

---

## 🔄 User Journey Flows

### Journey 1: First-Time User (Confused Teenager)

```
Home Page
  → Reads "What We Do"
  → Clicks "Start Health Check"
  
Health Check
  → Fills form (Step 1-4)
  → Clicks "Analyze"
  → Sees "Moderate Risk" result
  → Reads explanation
  → Sees "Doctor Consultation Not Urgent"
  → Clicks "View Lifestyle Plan"
  
Lifestyle Plan
  → Reads stress regulation tips
  → Takes notes
  
Optional:
  → Clicks "Learn Conditions"
  → Reads PCOS education
  → Downloads report
```

### Journey 2: Worried Young Adult

```
Home Page
  → Clicks "Talk to AI Assistant"
  
AI Assistant
  → Selects "Young Adult (19-30)"
  → Selects "Menstrual Issues"
  → Answers guided questions
  → Receives clarification
  → Clicks "Take Full Health Check"
  
Health Check
  → Completes assessment
  → Sees "High Risk" result
  → Sees "Doctor Consultation Recommended"
  → Downloads report
  → Clicks "Find Help"
  
Find Help
  → Views demo doctor list
  → Reads preparation tips
```

### Journey 3: Diagnosed User (Seeking Guidance)

```
Home Page
  → Skips to "Learn Conditions"
  
Learn Conditions
  → Reads PCOS panel
  → Reads PCOD panel
  → Clicks "Lifestyle Plan"
  
Lifestyle Plan
  → Completes Health Check first (if not done)
  → Views personalized plan
  → Takes notes
```

---

## 🛠️ Technical Implementation Guide

### Module: `utils/decision_engine.py`

**Function:** `analyze_pcos_signals(params)`

**Responsibilities:**
- Signal scoring (transparent rules)
- PCOS type detection
- Risk level calculation
- Confidence score computation

**Returns:**
```python
{
    "pcos_type": str,
    "explanation": str,
    "risk_score": int,
    "risk_level": str,  # "Low Risk" | "Moderate Risk" | "High Risk"
    "confidence": float,  # 0-100
    "signals": {
        "cycle": int,
        "stress": int,
        "insulin": int,
        "androgen": int,
        "inflammation": int
    },
    "doctor_needed": bool,
    "doctor_reasons": list[str]
}
```

---

### Module: `utils/chat_engine.py`

**Function:** `generate_response(age_group, concern_category, answers)`

**Responsibilities:**
- Question selection from prompt_library
- Response generation (rule-based)
- Next step suggestions

**Returns:**
```python
{
    "clarification": str,
    "is_normal": bool,  # or None
    "next_steps": list[str],
    "suggest_health_check": bool
}
```

---

### Module: `utils/prompt_library.py`

**Structure:**
```python
PROMPTS = {
    "teenager": {
        "menstrual": [list of questions],
        "pain": [list of questions],
        ...
    },
    "young_adult": {...},
    "adult": {...}
}
```

**Question Format:**
```python
{
    "id": str,
    "text": str,
    "type": "radio" | "selectbox" | "slider",
    "options": list,
    "category": str
}
```

---

### Module: `utils/report_generator.py`

**Function:** `generate_summary(result_dict, user_inputs)`

**Responsibilities:**
- Format user report (text)
- Format doctor summary (text)
- Ensure non-diagnostic language

**Returns:**
```python
{
    "user_report": str,
    "doctor_summary": str
}
```

---

## 🎨 UI/UX Guidelines

### Color Palette

**Primary Colors:**
- Soft lavender: `#E8D5FF`
- Pastel pink: `#FFD5E5`
- Mint green: `#D5FFE8`
- Light peach: `#FFE8D5`

**Accent Colors:**
- Purple: `#9B7EDE` (primary actions)
- Teal: `#5FB3B3` (secondary actions)
- Coral: `#FF6B9D` (emphasis)

**Alert Colors:**
- Red: Only for urgent alerts
- Orange: Moderate warnings
- Green: Positive/safe indicators

### Typography

- **Headings:** Clear, bold, sans-serif
- **Body:** Readable, comfortable line height
- **Size:** Accessible (minimum 14px)

### Components

**Cards:**
- Rounded corners (8-12px)
- Soft shadows
- Padding: 16-24px

**Buttons:**
- Rounded (6-8px)
- Clear labels
- Adequate padding

**Forms:**
- Clear labels
- Helpful placeholders
- Error states (if needed)

### Mobile Responsiveness

- Single column on mobile
- Touch-friendly buttons
- Readable font sizes
- Adequate spacing

---

## 🛡️ Safety & Ethics Framework

### Disclaimers (Required on Every Page)

1. **Non-Diagnostic Statement:**
   "This tool is for awareness and support only. It does not provide medical diagnosis."

2. **Ethical Use Statement:**
   "PCOS Health AI is designed to support, not replace, healthcare professionals."

3. **Privacy Statement:**
   "We do not store your personal data. All information is session-based only."

### Language Rules

**DO:**
- "Your symptoms may indicate..."
- "This pattern suggests..."
- "You might benefit from..."
- "Consider consulting a doctor if..."

**DON'T:**
- "You have PCOS"
- "You are diagnosed with..."
- "This is definitely..."
- "You should take..."

### Content Moderation

- All educational content reviewed
- No medical claims
- Evidence-based information only
- Respectful, inclusive language

---

## 🚀 Deployment Strategy

### Streamlit Cloud Deployment

1. **Repository Setup:**
   - GitHub repository
   - Clear README
   - requirements.txt

2. **Streamlit Cloud:**
   - Connect GitHub repo
   - Set main file: `app.py`
   - Deploy

3. **Configuration:**
   - `.streamlit/config.toml` for theme
   - Environment variables (if needed)

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

---

## 📊 Feature-to-File Mapping

| Feature | File Location | Logic Location |
|---------|--------------|----------------|
| Home Page | `pages/1_🏠_Home.py` | None (static) |
| Health Check UI | `pages/2_🔍_Health_Check.py` | `utils/decision_engine.py` |
| AI Assistant UI | `pages/3_💬_AI_Assistant.py` | `utils/chat_engine.py` |
| Condition Education | `pages/4_📚_Learn_Conditions.py` | None (static) |
| Lifestyle Plan | `pages/5_🌱_Lifestyle_Plan.py` | `utils/decision_engine.py` |
| Trackers | `pages/6_📊_Trackers.py` | Session state only |
| Community | `pages/7_👥_Community.py` | Session state only |
| Find Help | `pages/8_🩺_Find_Help.py` | None (static) |
| Report Export | All pages (via button) | `utils/report_generator.py` |

---

## ✅ Implementation Checklist

### Phase 1: Foundation
- [x] Create architecture document
- [ ] Set up file structure
- [ ] Create `.streamlit/config.toml`
- [ ] Create `requirements.txt`

### Phase 2: Core Modules
- [ ] Enhance `utils/decision_engine.py`
- [ ] Create `utils/chat_engine.py`
- [ ] Create `utils/prompt_library.py`
- [ ] Create `utils/report_generator.py`

### Phase 3: Pages
- [ ] Create `pages/1_🏠_Home.py`
- [ ] Create `pages/2_🔍_Health_Check.py`
- [ ] Create `pages/3_💬_AI_Assistant.py`
- [ ] Create `pages/4_📚_Learn_Conditions.py`
- [ ] Create `pages/5_🌱_Lifestyle_Plan.py`
- [ ] Create `pages/6_📊_Trackers.py`
- [ ] Create `pages/7_👥_Community.py`
- [ ] Create `pages/8_🩺_Find_Help.py`

### Phase 4: Main App
- [ ] Create new `app.py` (navigation)
- [ ] Test all pages
- [ ] Verify logic separation

### Phase 5: Polish
- [ ] Update README.md
- [ ] Add disclaimers
- [ ] Test user journeys
- [ ] Deploy to Streamlit Cloud

---

## 🎯 Success Metrics (For Judging)

### Technical Excellence
- ✅ Clean code architecture
- ✅ Modular design
- ✅ Explainable AI
- ✅ No black-box models

### User Experience
- ✅ Clear navigation
- ✅ Intuitive flows
- ✅ Supportive tone
- ✅ Accessible design

### Ethical Design
- ✅ Non-diagnostic
- ✅ Clear disclaimers
- ✅ Privacy-first
- ✅ Clinically respectful

### Impact Potential
- ✅ Addresses real problem
- ✅ Scalable architecture
- ✅ Production-ready structure
- ✅ Clear value proposition

---

**End of Architecture Blueprint**
