def analyze_pcos_signals(
    cycle_length,
    period_pain,
    stress_level,
    sleep_quality,
    mood_changes,
    sugar_cravings,
    weight_change,
    facial_hair,
    age=None,
    missed_periods=None,
    acne=None,
    hair_loss=None,
    anxiety=None,
    activity_level=None,
    diet_pattern=None,
    family_history=None
):
    """
    Core decision engine for PCOS pattern detection.
    This file contains NO UI code. Pure logic only.
    
    Args:
        cycle_length: str - Cycle regularity
        period_pain: str - Period pain frequency
        stress_level: int/float - Stress level (0-10)
        sleep_quality: str - Sleep quality
        mood_changes: str - Mood change frequency
        sugar_cravings: str - Sugar craving frequency
        weight_change: str - Weight change pattern
        facial_hair: str - Facial/body hair growth
        age: int (optional) - Age
        missed_periods: str (optional) - Missed periods frequency
        acne: str (optional) - Acne severity
        hair_loss: str (optional) - Hair loss severity
        anxiety: str (optional) - Anxiety frequency
        activity_level: str (optional) - Activity level
        diet_pattern: str (optional) - Diet pattern
        family_history: str (optional) - Family history of PCOS/PCOD
    
    Returns:
        dict: Analysis results including risk level, PCOS type, signals, and doctor recommendation
    """

    # -----------------------------
    # SIGNAL SCORES
    # -----------------------------
    cycle_signal = 0
    stress_signal = 0
    insulin_signal = 0
    androgen_signal = 0
    inflammation_signal = 0

    # Cycle irregularity
    if cycle_length == "Irregular (varies frequently)":
        cycle_signal += 2
    elif cycle_length == "Absent for months" or cycle_length == "Absent or very irregular":
        cycle_signal += 3
    
    # Missed periods
    if missed_periods:
        if missed_periods == "Frequently" or "three" in missed_periods.lower() or "more" in missed_periods.lower():
            cycle_signal += 2
        elif missed_periods == "Occasionally" or "once" in missed_periods.lower() or "twice" in missed_periods.lower():
            cycle_signal += 1

    # Stress & adrenal
    if isinstance(stress_level, (int, float)):
        if stress_level >= 7:
            stress_signal += 4
        elif stress_level >= 4:
            stress_signal += 2

    if sleep_quality == "Disturbed":
        stress_signal += 1
    elif sleep_quality == "Insomnia / very poor" or sleep_quality == "Poor/Insomnia":
        stress_signal += 2

    if mood_changes == "Frequently":
        stress_signal += 2
    
    if anxiety:
        if anxiety == "Frequently":
            stress_signal += 2
        elif anxiety == "Occasionally":
            stress_signal += 1

    # Insulin resistance
    if sugar_cravings == "Frequently":
        insulin_signal += 3
    elif sugar_cravings == "Occasionally":
        insulin_signal += 1

    if weight_change in ["Weight gain", "Fluctuates"]:
        insulin_signal += 2
    
    if diet_pattern:
        if "High sugar" in diet_pattern or "processed" in diet_pattern.lower():
            insulin_signal += 1
    
    if activity_level:
        if activity_level == "Sedentary":
            insulin_signal += 1

    # Androgen excess
    if facial_hair == "Noticeable" or facial_hair == "Significant":
        androgen_signal += 3
    elif facial_hair == "Mild":
        androgen_signal += 1
    
    if acne:
        if acne == "Severe" or acne == "Moderate":
            androgen_signal += 2
        elif acne == "Mild":
            androgen_signal += 1
    
    if hair_loss:
        if hair_loss == "Noticeable":
            androgen_signal += 2
        elif hair_loss == "Mild":
            androgen_signal += 1

    # Inflammation
    if period_pain == "Often" or period_pain == "Frequently":
        inflammation_signal += 2
    elif period_pain == "Sometimes" or period_pain == "Occasionally":
        inflammation_signal += 1

    if sleep_quality != "Good":
        inflammation_signal += 1

    # -----------------------------
    # PCOS TYPE DETECTION
    # -----------------------------
    pcos_type = "Low / Unclear PCOS Pattern"
    explanation = "Your current responses do not strongly match a specific PCOS subtype."

    if stress_signal >= 7 and insulin_signal < 4:
        pcos_type = "Adrenal PCOS (Stress-driven)"
        explanation = (
            "Your symptoms indicate chronic stress and adrenal overload. "
            "This PCOS type is often overlooked in standard diagnosis."
        )

    elif insulin_signal >= 6:
        pcos_type = "Insulin-Resistant PCOS"
        explanation = (
            "Your responses suggest metabolic stress and insulin resistance, "
            "one of the most common PCOS drivers."
        )

    elif cycle_signal >= 3 and insulin_signal <= 2:
        pcos_type = "Lean PCOS"
        explanation = (
            "Despite limited metabolic symptoms, cycle irregularities suggest "
            "a hormonal imbalance typical of Lean PCOS."
        )

    elif inflammation_signal >= 3:
        pcos_type = "Inflammatory PCOS"
        explanation = (
            "Inflammation, pain, and fatigue dominate your symptom pattern."
        )

    # -----------------------------
    # RISK SCORE
    # -----------------------------
    total_risk_score = (
        cycle_signal +
        stress_signal +
        insulin_signal +
        androgen_signal +
        inflammation_signal
    )
    
    # -----------------------------
    # AI CONFIDENCE ESTIMATION
    # -----------------------------
    max_possible_score = 20
    confidence_score = round((total_risk_score / max_possible_score) * 100, 1)


    if total_risk_score <= 6:
        risk_level = "Low Risk"
    elif total_risk_score <= 12:
        risk_level = "Moderate Risk"
    else:
        risk_level = "High Risk"

    # -----------------------------
    # DOCTOR CONSULTATION LOGIC
    # -----------------------------
    doctor_needed = False
    doctor_reasons = []
    
    # High risk always recommends doctor
    if risk_level == "High Risk":
        doctor_needed = True
        doctor_reasons.append("overall high risk pattern")
    
    # Severe pain with cycle irregularity
    if cycle_signal >= 3 and inflammation_signal >= 3:
        doctor_needed = True
        doctor_reasons.append("severe pain with cycle irregularity")
    
    # Strong metabolic indicators
    if insulin_signal >= 6:
        if not doctor_needed:
            doctor_needed = True
        doctor_reasons.append("strong metabolic indicators")
    
    # Absent periods for extended time
    if cycle_length == "Absent for months" or cycle_length == "Absent or very irregular":
        if not doctor_needed:
            doctor_needed = True
        doctor_reasons.append("prolonged absence of periods")
    
    # Significant androgen symptoms
    if androgen_signal >= 5:
        if not doctor_needed:
            doctor_needed = True
        doctor_reasons.append("significant androgen-related symptoms")

    # -----------------------------
    # ML MODEL HOOK (FUTURE USE)
    # -----------------------------
    """
    def ml_predict(features):
        # Placeholder for future ML model integration
        # model = joblib.load("model/pcos_model.pkl")
        # return model.predict_proba(features)
        pass
    """

    return {
        "pcos_type": pcos_type,
        "explanation": explanation,
        "risk_score": total_risk_score,
        "risk_level": risk_level,
        "confidence": confidence_score,
        "signals": {
            "cycle": cycle_signal,
            "stress": stress_signal,
            "insulin": insulin_signal,
            "androgen": androgen_signal,
            "inflammation": inflammation_signal
        },
        "doctor_needed": doctor_needed,
        "doctor_reasons": doctor_reasons
    }
