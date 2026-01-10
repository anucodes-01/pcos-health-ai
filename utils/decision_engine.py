def analyze_pcos_signals(
    cycle_length,
    period_pain,
    stress_level,
    sleep_quality,
    mood_changes,
    sugar_cravings,
    weight_change,
    facial_hair
):
    """
    Core decision engine for PCOS pattern detection.
    This file contains NO UI code. Pure logic only.
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
    elif cycle_length == "Absent for months":
        cycle_signal += 3

    # Stress & adrenal
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

    # Insulin resistance
    if sugar_cravings == "Frequently":
        insulin_signal += 3
    elif sugar_cravings == "Occasionally":
        insulin_signal += 1

    if weight_change in ["Weight gain", "Fluctuates"]:
        insulin_signal += 2

    # Androgen excess
    if facial_hair == "Noticeable":
        androgen_signal += 3
    elif facial_hair == "Mild":
        androgen_signal += 1

    # Inflammation
    if period_pain == "Often":
        inflammation_signal += 2

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

    if total_risk_score <= 6:
        risk_level = "Low Risk"
    elif total_risk_score <= 12:
        risk_level = "Moderate Risk"
    else:
        risk_level = "High Risk"

    return {
        "pcos_type": pcos_type,
        "explanation": explanation,
        "risk_score": total_risk_score,
        "risk_level": risk_level,
        "signals": {
            "cycle": cycle_signal,
            "stress": stress_signal,
            "insulin": insulin_signal,
            "androgen": androgen_signal,
            "inflammation": inflammation_signal
        }
    }
