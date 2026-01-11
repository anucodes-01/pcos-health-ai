"""
Guided chatbot engine for clarification and emotional support.
Rule-based, explainable responses - no black-box ML.
"""

from utils.prompt_library import get_questions_for_category


def generate_response(age_group, concern_category, answers):
    """
    Generate a clarification and guidance response based on user answers.
    
    Args:
        age_group: str - "teenager", "young_adult", or "adult"
        concern_category: str - "menstrual", "pain", "hormonal", "mood", "weight", "other"
        answers: dict - Dictionary of question_id: answer pairs
    
    Returns:
        dict: {
            "clarification": str - Explanation in plain language,
            "is_normal": bool or None - Whether response suggests normal variation,
            "next_steps": list[str] - Suggested actions,
            "suggest_health_check": bool - Whether to recommend full health check
        }
    """
    
    clarification = ""
    is_normal = None
    next_steps = []
    suggest_health_check = False
    
    # Determine response based on category and answers
    if concern_category == "menstrual":
        clarification, is_normal, next_steps, suggest_health_check = _handle_menstrual_concerns(
            age_group, answers
        )
    elif concern_category == "pain":
        clarification, is_normal, next_steps, suggest_health_check = _handle_pain_concerns(
            age_group, answers
        )
    elif concern_category == "hormonal":
        clarification, is_normal, next_steps, suggest_health_check = _handle_hormonal_concerns(
            age_group, answers
        )
    elif concern_category == "mood":
        clarification, is_normal, next_steps, suggest_health_check = _handle_mood_concerns(
            age_group, answers
        )
    elif concern_category == "weight":
        clarification, is_normal, next_steps, suggest_health_check = _handle_weight_concerns(
            age_group, answers
        )
    else:
        clarification = (
            "Thank you for sharing your concerns. Your experiences are valid, "
            "and it's understandable to seek clarification."
        )
        next_steps = [
            "Consider taking our full Health Check for a comprehensive assessment",
            "Learn more about common conditions in our Education section",
            "If concerns persist, consider consulting with a healthcare professional"
        ]
        suggest_health_check = True
    
    return {
        "clarification": clarification,
        "is_normal": is_normal,
        "next_steps": next_steps,
        "suggest_health_check": suggest_health_check
    }


def _handle_menstrual_concerns(age_group, answers):
    """Handle menstrual-related concerns."""
    clarification = "Menstrual patterns can vary widely, and what's normal for one person may differ for another."
    is_normal = None
    next_steps = []
    suggest_health_check = False
    
    # Check for irregularity indicators
    irregularity_indicators = [
        "Irregular", "Very irregular", "Absent", "missing", "varies more"
    ]
    
    has_irregularity = any(
        any(indicator.lower() in str(answer).lower() for indicator in irregularity_indicators)
        for answer in answers.values()
    )
    
    if has_irregularity:
        clarification += (
            " Irregular periods can have many causes, including hormonal changes, "
            "stress, lifestyle factors, or underlying conditions. "
            "If irregularity persists or is concerning, it's worth discussing with a healthcare provider."
        )
        is_normal = False
        next_steps = [
            "Track your cycle patterns for 2-3 months",
            "Consider taking our full Health Check for comprehensive assessment",
            "If irregularity persists for 3+ months, consider consulting a healthcare provider"
        ]
        suggest_health_check = True
    else:
        clarification += (
            " Regular cycles (every 25-35 days) are generally considered normal, "
            "though some variation is common, especially during teenage years or times of stress."
        )
        is_normal = True
        next_steps = [
            "Continue tracking your cycle patterns",
            "Maintain a healthy lifestyle with balanced nutrition and regular activity",
            "If patterns change significantly, consider our Health Check"
        ]
    
    return clarification, is_normal, next_steps, suggest_health_check


def _handle_pain_concerns(age_group, answers):
    """Handle pain-related concerns."""
    clarification = "Period pain varies greatly between individuals, but severe or disabling pain is not normal."
    is_normal = None
    next_steps = []
    suggest_health_check = False
    
    # Check for severe pain indicators
    severe_pain_indicators = ["Severe", "disabling", "difficult to function", "Significantly"]
    
    has_severe_pain = any(
        any(indicator.lower() in str(answer).lower() for indicator in severe_pain_indicators)
        for answer in answers.values()
    )
    
    if has_severe_pain:
        clarification += (
            " Severe or disabling pain that affects your daily life warrants attention. "
            "This could indicate various conditions and should be evaluated by a healthcare provider."
        )
        is_normal = False
        next_steps = [
            "Consider consulting with a healthcare provider, especially if pain is severe or worsening",
            "Take our full Health Check to document all symptoms",
            "Keep a pain diary noting when, where, and how severe the pain is"
        ]
        suggest_health_check = True
    else:
        clarification += (
            " Mild to moderate period pain is common and can often be managed with "
            "rest, heat, gentle movement, or over-the-counter pain relief (as appropriate)."
        )
        is_normal = True
        next_steps = [
            "Continue to monitor pain patterns",
            "Try gentle movement and heat for pain management",
            "If pain worsens or changes, consider our Health Check"
        ]
    
    return clarification, is_normal, next_steps, suggest_health_check


def _handle_hormonal_concerns(age_group, answers):
    """Handle hormonal-related concerns."""
    clarification = "Hormonal changes can affect many aspects of health, including skin, hair, and body composition."
    is_normal = None
    next_steps = []
    suggest_health_check = False
    
    # Check for significant hormonal indicators
    significant_indicators = ["Noticeable", "Significant", "Severe", "persistent"]
    
    has_significant_symptoms = any(
        any(indicator.lower() in str(answer).lower() for indicator in significant_indicators)
        for answer in answers.values()
    )
    
    if has_significant_symptoms:
        clarification += (
            " Noticeable changes in hair growth, hair loss, or persistent acne "
            "may indicate hormonal imbalances worth discussing with a healthcare provider."
        )
        is_normal = False
        next_steps = [
            "Consider our full Health Check for comprehensive assessment",
            "Document changes with photos or notes over time",
            "If symptoms are concerning, consider consulting a healthcare provider"
        ]
        suggest_health_check = True
    else:
        clarification += (
            " Some degree of hormonal variation is normal, especially during "
            "teenage years, times of stress, or life transitions."
        )
        is_normal = True
        next_steps = [
            "Continue monitoring changes",
            "Maintain a balanced lifestyle with good nutrition and sleep",
            "If changes become more noticeable, consider our Health Check"
        ]
    
    return clarification, is_normal, next_steps, suggest_health_check


def _handle_mood_concerns(age_group, answers):
    """Handle mood and mental health concerns."""
    clarification = "Mood changes can be influenced by many factors, including hormonal cycles, stress, and lifestyle."
    is_normal = None
    next_steps = []
    suggest_health_check = False
    
    # Check for significant mood indicators
    frequent_indicators = ["Frequently", "Often", "Poor", "Insomnia"]
    high_stress = any(
        isinstance(answer, (int, float)) and answer >= 7
        for answer in answers.values()
    )
    
    has_frequent_mood_issues = any(
        any(indicator.lower() in str(answer).lower() for indicator in frequent_indicators)
        for answer in answers.values()
    ) or high_stress
    
    if has_frequent_mood_issues:
        clarification += (
            " Frequent mood changes, high stress, or poor sleep can significantly impact "
            "overall health and may be connected to hormonal patterns. "
            "If these affect your daily life, support from healthcare providers or mental health professionals can be helpful."
        )
        is_normal = False
        next_steps = [
            "Prioritize sleep and stress management",
            "Consider our full Health Check to see how mood connects with other symptoms",
            "If mood changes are severe or concerning, consider consulting with healthcare or mental health professionals"
        ]
        suggest_health_check = True
    else:
        clarification += (
            " Occasional mood changes, especially around menstrual cycles, are common. "
            "Good sleep, stress management, and self-care can help."
        )
        is_normal = True
        next_steps = [
            "Continue practicing self-care and stress management",
            "Maintain regular sleep patterns",
            "If mood changes worsen, consider our Health Check or professional support"
        ]
    
    return clarification, is_normal, next_steps, suggest_health_check


def _handle_weight_concerns(age_group, answers):
    """Handle weight and metabolic concerns."""
    clarification = "Weight changes can have many causes, including hormonal patterns, lifestyle, stress, and metabolism."
    is_normal = None
    next_steps = []
    suggest_health_check = False
    
    # Check for significant weight/metabolic indicators
    significant_indicators = ["Noticeable", "Significant", "Frequently", "Very difficult"]
    weight_gain_or_cravings = any(
        "weight gain" in str(answer).lower() or "Frequently" in str(answer)
        for answer in answers.values()
    )
    
    if weight_gain_or_cravings or any(
        any(indicator.lower() in str(answer).lower() for indicator in significant_indicators)
        for answer in answers.values()
    ):
        clarification += (
            " Unexplained weight changes or frequent cravings can sometimes be connected "
            "to metabolic or hormonal patterns. A comprehensive assessment may help understand contributing factors."
        )
        is_normal = False
        next_steps = [
            "Consider our full Health Check for comprehensive assessment",
            "Focus on balanced nutrition and regular meals",
            "If weight changes are unexplained or concerning, consider consulting with a healthcare provider"
        ]
        suggest_health_check = True
    else:
        clarification += (
            " Some weight fluctuation is normal, and cravings can be influenced by "
            "many factors including stress, sleep, and hormonal cycles."
        )
        is_normal = True
        next_steps = [
            "Maintain balanced nutrition with regular meals",
            "Stay active and prioritize sleep",
            "If changes become more significant, consider our Health Check"
        ]
    
    return clarification, is_normal, next_steps, suggest_health_check
