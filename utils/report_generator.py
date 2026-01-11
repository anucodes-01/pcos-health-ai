"""
Report generator for user and doctor summaries.
Formats results in clear, non-diagnostic language.
"""

from datetime import datetime


def generate_summary(result_dict, user_inputs):
    """
    Generate user and doctor summaries from health check results.
    
    Args:
        result_dict: dict - Results from decision_engine.analyze_pcos_signals()
        user_inputs: dict - Original user inputs
    
    Returns:
        dict: {
            "user_report": str - User-friendly summary,
            "doctor_summary": str - Doctor-ready summary
        }
    """
    
    user_report = _generate_user_report(result_dict, user_inputs)
    doctor_summary = _generate_doctor_summary(result_dict, user_inputs)
    
    return {
        "user_report": user_report,
        "doctor_summary": doctor_summary
    }


def _generate_user_report(result_dict, user_inputs):
    """Generate user-friendly report."""
    risk_level = result_dict.get("risk_level", "Unknown")
    pcos_type = result_dict.get("pcos_type", "Unclear")
    confidence = result_dict.get("confidence", 0)
    signals = result_dict.get("signals", {})
    doctor_needed = result_dict.get("doctor_needed", False)
    doctor_reasons = result_dict.get("doctor_reasons", [])
    
    report = f"""
═══════════════════════════════════════════════════════════════
PCOS Health AI – Personal Health Summary
Generated: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}
═══════════════════════════════════════════════════════════════

OVERALL ASSESSMENT
───────────────────────────────────────────────────────────────
Risk Level: {risk_level}
Detected Pattern: {pcos_type}
AI Confidence: {confidence}%

YOUR HEALTH SIGNALS
───────────────────────────────────────────────────────────────
Cycle Irregularity Score: {signals.get('cycle', 0)}/10
Stress & Adrenal Score: {signals.get('stress', 0)}/10
Metabolic/Insulin Score: {signals.get('insulin', 0)}/10
Androgen-Related Score: {signals.get('androgen', 0)}/10
Inflammation Score: {signals.get('inflammation', 0)}/10

EXPLANATION
───────────────────────────────────────────────────────────────
{result_dict.get('explanation', 'No specific pattern detected.')}

CONTRIBUTING FACTORS
───────────────────────────────────────────────────────────────
"""
    
    contributing_factors = []
    if signals.get('cycle', 0) >= 3:
        contributing_factors.append("Significant menstrual irregularity")
    if signals.get('insulin', 0) >= 4:
        contributing_factors.append("Strong metabolic/insulin-related signals")
    if signals.get('stress', 0) >= 6:
        contributing_factors.append("High stress and adrenal load")
    if signals.get('androgen', 0) >= 3:
        contributing_factors.append("Noticeable androgen-related symptoms")
    if signals.get('inflammation', 0) >= 3:
        contributing_factors.append("Pain and inflammation indicators")
    
    if contributing_factors:
        for factor in contributing_factors:
            report += f"• {factor}\n"
    else:
        report += "• No dominant contributing factors identified\n"
    
    report += f"""
RECOMMENDATION
───────────────────────────────────────────────────────────────
"""
    
    if doctor_needed:
        reasons_text = ", ".join(doctor_reasons) if doctor_reasons else "pattern assessment"
        report += f"""
Medical consultation is recommended based on: {reasons_text}

Professional medical evaluation is advised for:
• Confirmation and comprehensive assessment
• Appropriate testing
• Personalized treatment plan
• Ongoing monitoring and support
"""
    else:
        report += """
Lifestyle-focused management and monitoring may be appropriate at this stage.

Consider:
• Continuing to track symptoms and patterns
• Focusing on lifestyle factors (sleep, stress, nutrition, activity)
• Reassessing in 2-3 months or if symptoms change
• Consulting a healthcare provider if symptoms worsen
"""
    
    report += f"""
YOUR RESPONSES (SUMMARY)
───────────────────────────────────────────────────────────────
Age: {user_inputs.get('age', 'Not provided')}
Cycle Regularity: {user_inputs.get('cycle_length', 'Not provided')}
Period Pain: {user_inputs.get('period_pain', 'Not provided')}
Stress Level: {user_inputs.get('stress_level', 'Not provided')}/10
Sleep Quality: {user_inputs.get('sleep_quality', 'Not provided')}
Activity Level: {user_inputs.get('activity_level', 'Not provided')}

═══════════════════════════════════════════════════════════════
IMPORTANT DISCLAIMER
═══════════════════════════════════════════════════════════════
This summary is generated for awareness and support only.
It is NOT a medical diagnosis.

This tool is designed to:
• Help you understand your body signals
• Reduce confusion and anxiety
• Guide you on when to see a doctor
• Provide structured education

This tool does NOT:
• Diagnose medical conditions
• Prescribe treatments
• Replace healthcare professionals
• Store your personal data

Always consult qualified healthcare professionals for:
• Medical diagnosis
• Treatment recommendations
• Urgent health concerns
• Ongoing medical care

For urgent health concerns, contact emergency services immediately.

═══════════════════════════════════════════════════════════════
Generated by PCOS Health AI
A Safe, Explainable Women's Health Companion
═══════════════════════════════════════════════════════════════
"""
    
    return report.strip()


def _generate_doctor_summary(result_dict, user_inputs):
    """Generate doctor-ready clinical summary."""
    risk_level = result_dict.get("risk_level", "Unknown")
    pcos_type = result_dict.get("pcos_type", "Unclear")
    confidence = result_dict.get("confidence", 0)
    signals = result_dict.get("signals", {})
    doctor_needed = result_dict.get("doctor_needed", False)
    doctor_reasons = result_dict.get("doctor_reasons", [])
    
    summary = f"""
═══════════════════════════════════════════════════════════════
PCOS Health AI – Clinical Summary for Healthcare Provider
Generated: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}
═══════════════════════════════════════════════════════════════

PATIENT PRESENTATION
───────────────────────────────────────────────────────────────
Patient presents with a {risk_level.lower()} PCOS risk profile.

DETECTED PATTERN
───────────────────────────────────────────────────────────────
AI-detected pattern: {pcos_type}
Confidence score: {confidence}% (based on transparent signal weighting)

CLINICAL SIGNALS
───────────────────────────────────────────────────────────────
Cycle Irregularity: {signals.get('cycle', 0)}/10
  {'↑ Elevated' if signals.get('cycle', 0) >= 3 else '→ Within normal range'}
  
Stress & Adrenal Load: {signals.get('stress', 0)}/10
  {'↑ Elevated' if signals.get('stress', 0) >= 6 else '→ Within manageable range'}
  
Metabolic/Insulin Indicators: {signals.get('insulin', 0)}/10
  {'↑ Elevated' if signals.get('insulin', 0) >= 4 else '→ No strong indicators'}
  
Androgen-Related Symptoms: {signals.get('androgen', 0)}/10
  {'↑ Present' if signals.get('androgen', 0) >= 3 else '→ Minimal'}
  
Inflammation Indicators: {signals.get('inflammation', 0)}/10
  {'↑ Present' if signals.get('inflammation', 0) >= 3 else '→ Minimal'}

REPORTED SYMPTOMS
───────────────────────────────────────────────────────────────
Age: {user_inputs.get('age', 'Not reported')}
Menstrual Pattern: {user_inputs.get('cycle_length', 'Not reported')}
Period Pain: {user_inputs.get('period_pain', 'Not reported')}
Stress Level: {user_inputs.get('stress_level', 'Not reported')}/10
Sleep Quality: {user_inputs.get('sleep_quality', 'Not reported')}
Mood Changes: {user_inputs.get('mood_changes', 'Not reported')}
Sugar Cravings: {user_inputs.get('sugar_cravings', 'Not reported')}
Weight Changes: {user_inputs.get('weight_change', 'Not reported')}
Hair Growth: {user_inputs.get('facial_hair', 'Not reported')}
Activity Level: {user_inputs.get('activity_level', 'Not reported')}
Diet Pattern: {user_inputs.get('diet_pattern', 'Not reported')}

CLINICAL RECOMMENDATION
───────────────────────────────────────────────────────────────
"""
    
    if doctor_needed:
        reasons_text = "; ".join(doctor_reasons) if doctor_reasons else "pattern assessment"
        summary += f"""
Medical evaluation is advised based on: {reasons_text}

Suggested evaluation may include:
• Comprehensive history and physical examination
• Hormonal assessment (LH, FSH, testosterone, DHEA-S, etc.)
• Metabolic evaluation (fasting insulin, HbA1c, glucose tolerance if indicated)
• Additional testing as clinically indicated
• Consideration of PCOS diagnostic criteria (Rotterdam criteria)
"""
    else:
        summary += """
Lifestyle-focused monitoring may be appropriate with reassessment if symptoms evolve.

Consider:
• Symptom tracking and monitoring
• Lifestyle modifications (sleep, stress management, nutrition, activity)
• Reassessment in 2-3 months or if symptoms change
• Patient education about PCOS/PCOD if applicable
"""
    
    summary += f"""
NOTES ON TOOL METHODOLOGY
───────────────────────────────────────────────────────────────
This summary was generated using a rule-based, explainable AI system.
All scoring is transparent and based on clinical signal weighting.

• No black-box machine learning models were used
• All decisions are traceable to specific input signals
• Confidence scores reflect signal strength, not diagnostic certainty
• This tool is for awareness and discussion support only

═══════════════════════════════════════════════════════════════
DISCLAIMER FOR HEALTHCARE PROVIDERS
═══════════════════════════════════════════════════════════════
This summary is generated for informational purposes and discussion support.
It is NOT a medical diagnosis and should be used as one data point among many
in your clinical evaluation.

This tool is designed to:
• Help patients understand their symptoms
• Facilitate patient-provider conversations
• Provide structured symptom documentation

Clinical decision-making should always be based on:
• Comprehensive medical history
• Physical examination
• Appropriate diagnostic testing
• Professional clinical judgment

═══════════════════════════════════════════════════════════════
Generated by PCOS Health AI
A Safe, Explainable Women's Health Companion
═══════════════════════════════════════════════════════════════
"""
    
    return summary.strip()
