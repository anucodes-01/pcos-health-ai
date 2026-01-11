"""
Standardized question sets for guided chatbot flow.
All questions are safe, non-judgmental, and clinically inspired.
"""

PROMPTS = {
    "teenager": {
        "menstrual": [
            {
                "id": "t_men_1",
                "text": "How regular are your periods?",
                "type": "radio",
                "options": ["Very regular (every 28-32 days)", "Somewhat regular (varies 3-7 days)", "Irregular (varies more than a week)", "Very irregular or missing"],
                "category": "menstrual"
            },
            {
                "id": "t_men_2",
                "text": "How long do your periods usually last?",
                "type": "radio",
                "options": ["3-5 days", "6-7 days", "More than 7 days", "Varies a lot"],
                "category": "menstrual"
            },
            {
                "id": "t_men_3",
                "text": "Do you experience heavy bleeding?",
                "type": "radio",
                "options": ["No", "Sometimes", "Often"],
                "category": "menstrual"
            },
            {
                "id": "t_men_4",
                "text": "When did you get your first period?",
                "type": "radio",
                "options": ["Before age 12", "Age 12-14", "Age 15-17", "Haven't gotten it yet"],
                "category": "menstrual"
            }
        ],
        "pain": [
            {
                "id": "t_pain_1",
                "text": "Do you experience period pain?",
                "type": "radio",
                "options": ["No pain", "Mild pain (can manage with rest)", "Moderate pain (affects daily activities)", "Severe pain (difficult to function)"],
                "category": "pain"
            },
            {
                "id": "t_pain_2",
                "text": "When does the pain occur?",
                "type": "radio",
                "options": ["During periods only", "Before periods start", "During and before periods", "Other times too"],
                "category": "pain"
            },
            {
                "id": "t_pain_3",
                "text": "Does the pain affect your school or activities?",
                "type": "radio",
                "options": ["No", "Sometimes", "Often"],
                "category": "pain"
            }
        ],
        "hormonal": [
            {
                "id": "t_horm_1",
                "text": "Do you experience acne?",
                "type": "radio",
                "options": ["No", "Mild (occasional breakouts)", "Moderate (regular breakouts)", "Severe (persistent acne)"],
                "category": "hormonal"
            },
            {
                "id": "t_horm_2",
                "text": "Have you noticed changes in body hair?",
                "type": "radio",
                "options": ["No changes", "Slightly more noticeable", "Noticeable increase", "Significant increase"],
                "category": "hormonal"
            },
            {
                "id": "t_horm_3",
                "text": "Have you noticed changes in your weight?",
                "type": "radio",
                "options": ["No changes", "Slight weight gain", "Noticeable weight gain", "Weight loss"],
                "category": "hormonal"
            }
        ],
        "mood": [
            {
                "id": "t_mood_1",
                "text": "Do you experience mood swings around your period?",
                "type": "radio",
                "options": ["No", "Occasionally", "Frequently"],
                "category": "mood"
            },
            {
                "id": "t_mood_2",
                "text": "Do you feel more anxious or stressed lately?",
                "type": "radio",
                "options": ["No", "Sometimes", "Often"],
                "category": "mood"
            },
            {
                "id": "t_mood_3",
                "text": "How is your sleep?",
                "type": "radio",
                "options": ["Good (7-9 hours)", "Okay (5-7 hours)", "Poor (less than 5 hours or trouble falling asleep)"],
                "category": "mood"
            }
        ],
        "weight": [
            {
                "id": "t_weight_1",
                "text": "Have you noticed unexplained weight changes?",
                "type": "radio",
                "options": ["No", "Slight weight gain", "Noticeable weight gain", "Weight loss"],
                "category": "weight"
            },
            {
                "id": "t_weight_2",
                "text": "Do you experience strong sugar cravings?",
                "type": "radio",
                "options": ["No", "Occasionally", "Frequently"],
                "category": "weight"
            },
            {
                "id": "t_weight_3",
                "text": "How is your energy level?",
                "type": "radio",
                "options": ["Good", "Sometimes low", "Often low"],
                "category": "weight"
            }
        ],
        "other": [
            {
                "id": "t_other_1",
                "text": "What's your main concern?",
                "type": "text",
                "options": [],
                "category": "other"
            }
        ]
    },
    "young_adult": {
        "menstrual": [
            {
                "id": "ya_men_1",
                "text": "How regular are your menstrual cycles?",
                "type": "radio",
                "options": ["Regular (25-35 days)", "Somewhat regular (varies 5-10 days)", "Irregular (varies more than 10 days)", "Very irregular or absent"],
                "category": "menstrual"
            },
            {
                "id": "ya_men_2",
                "text": "Have you missed periods in the last 6 months?",
                "type": "radio",
                "options": ["No", "Once or twice", "Three or more times", "Haven't had a period"],
                "category": "menstrual"
            },
            {
                "id": "ya_men_3",
                "text": "Do you experience heavy or prolonged bleeding?",
                "type": "radio",
                "options": ["No", "Occasionally", "Often"],
                "category": "menstrual"
            },
            {
                "id": "ya_men_4",
                "text": "Have your periods changed recently?",
                "type": "radio",
                "options": ["No changes", "More irregular", "Heavier", "Lighter or missing"],
                "category": "menstrual"
            }
        ],
        "pain": [
            {
                "id": "ya_pain_1",
                "text": "How severe is your period pain?",
                "type": "radio",
                "options": ["No pain", "Mild (manageable)", "Moderate (affects activities)", "Severe (disabling)"],
                "category": "pain"
            },
            {
                "id": "ya_pain_2",
                "text": "Does pain occur at other times (not just during periods)?",
                "type": "radio",
                "options": ["No", "Occasionally", "Frequently"],
                "category": "pain"
            },
            {
                "id": "ya_pain_3",
                "text": "Has the pain gotten worse over time?",
                "type": "radio",
                "options": ["No", "Slightly worse", "Significantly worse"],
                "category": "pain"
            }
        ],
        "hormonal": [
            {
                "id": "ya_horm_1",
                "text": "Do you experience excess facial or body hair?",
                "type": "radio",
                "options": ["No", "Mild", "Noticeable", "Significant"],
                "category": "hormonal"
            },
            {
                "id": "ya_horm_2",
                "text": "Have you noticed hair thinning or loss?",
                "type": "radio",
                "options": ["No", "Mild", "Noticeable"],
                "category": "hormonal"
            },
            {
                "id": "ya_horm_3",
                "text": "Do you experience persistent acne?",
                "type": "radio",
                "options": ["No", "Mild", "Moderate", "Severe"],
                "category": "hormonal"
            }
        ],
        "mood": [
            {
                "id": "ya_mood_1",
                "text": "Do you experience mood swings or emotional changes?",
                "type": "radio",
                "options": ["No", "Occasionally", "Frequently"],
                "category": "mood"
            },
            {
                "id": "ya_mood_2",
                "text": "How is your stress level?",
                "type": "slider",
                "options": [0, 10],
                "category": "mood"
            },
            {
                "id": "ya_mood_3",
                "text": "How is your sleep quality?",
                "type": "radio",
                "options": ["Good", "Disturbed", "Poor/Insomnia"],
                "category": "mood"
            }
        ],
        "weight": [
            {
                "id": "ya_weight_1",
                "text": "Have you experienced unexplained weight changes?",
                "type": "radio",
                "options": ["No", "Weight gain", "Weight loss", "Fluctuates"],
                "category": "weight"
            },
            {
                "id": "ya_weight_2",
                "text": "Do you experience strong sugar or carbohydrate cravings?",
                "type": "radio",
                "options": ["No", "Occasionally", "Frequently"],
                "category": "weight"
            },
            {
                "id": "ya_weight_3",
                "text": "How is your energy level throughout the day?",
                "type": "radio",
                "options": ["Consistent", "Sometimes low", "Often low or crashes"],
                "category": "weight"
            }
        ],
        "other": [
            {
                "id": "ya_other_1",
                "text": "What's your main concern?",
                "type": "text",
                "options": [],
                "category": "other"
            }
        ]
    },
    "adult": {
        "menstrual": [
            {
                "id": "a_men_1",
                "text": "How regular are your menstrual cycles?",
                "type": "radio",
                "options": ["Regular (25-35 days)", "Somewhat regular", "Irregular", "Absent or very irregular"],
                "category": "menstrual"
            },
            {
                "id": "a_men_2",
                "text": "Have you missed periods in the last year?",
                "type": "radio",
                "options": ["No", "Occasionally", "Frequently", "Haven't had a period"],
                "category": "menstrual"
            },
            {
                "id": "a_men_3",
                "text": "Have your periods changed compared to when you were younger?",
                "type": "radio",
                "options": ["No changes", "More irregular", "Heavier or different", "Lighter or missing"],
                "category": "menstrual"
            },
            {
                "id": "a_men_4",
                "text": "Are you trying to conceive or concerned about fertility?",
                "type": "radio",
                "options": ["No", "Considering in future", "Currently trying", "Concerned about fertility"],
                "category": "menstrual"
            }
        ],
        "pain": [
            {
                "id": "a_pain_1",
                "text": "How severe is your period or pelvic pain?",
                "type": "radio",
                "options": ["No pain", "Mild", "Moderate", "Severe"],
                "category": "pain"
            },
            {
                "id": "a_pain_2",
                "text": "Does pain occur outside of periods?",
                "type": "radio",
                "options": ["No", "Occasionally", "Frequently"],
                "category": "pain"
            },
            {
                "id": "a_pain_3",
                "text": "Has pain affected your daily life or relationships?",
                "type": "radio",
                "options": ["No", "Somewhat", "Significantly"],
                "category": "pain"
            }
        ],
        "hormonal": [
            {
                "id": "a_horm_1",
                "text": "Do you experience excess facial or body hair?",
                "type": "radio",
                "options": ["No", "Mild", "Noticeable", "Significant"],
                "category": "hormonal"
            },
            {
                "id": "a_horm_2",
                "text": "Have you noticed hair thinning or loss?",
                "type": "radio",
                "options": ["No", "Mild", "Noticeable"],
                "category": "hormonal"
            },
            {
                "id": "a_horm_3",
                "text": "Do you experience persistent acne or skin changes?",
                "type": "radio",
                "options": ["No", "Mild", "Moderate", "Severe"],
                "category": "hormonal"
            }
        ],
        "mood": [
            {
                "id": "a_mood_1",
                "text": "Do you experience mood swings or emotional changes?",
                "type": "radio",
                "options": ["No", "Occasionally", "Frequently"],
                "category": "mood"
            },
            {
                "id": "a_mood_2",
                "text": "How would you rate your stress level?",
                "type": "slider",
                "options": [0, 10],
                "category": "mood"
            },
            {
                "id": "a_mood_3",
                "text": "How is your sleep quality?",
                "type": "radio",
                "options": ["Good", "Disturbed", "Poor/Insomnia"],
                "category": "mood"
            }
        ],
        "weight": [
            {
                "id": "a_weight_1",
                "text": "Have you experienced unexplained weight changes?",
                "type": "radio",
                "options": ["No", "Weight gain", "Weight loss", "Fluctuates"],
                "category": "weight"
            },
            {
                "id": "a_weight_2",
                "text": "Do you experience strong sugar or carbohydrate cravings?",
                "type": "radio",
                "options": ["No", "Occasionally", "Frequently"],
                "category": "weight"
            },
            {
                "id": "a_weight_3",
                "text": "How is your energy level and ability to manage weight?",
                "type": "radio",
                "options": ["Good", "Challenging", "Very difficult"],
                "category": "weight"
            }
        ],
        "other": [
            {
                "id": "a_other_1",
                "text": "What's your main concern?",
                "type": "text",
                "options": [],
                "category": "other"
            }
        ]
    }
}


def get_questions_for_category(age_group, concern_category, limit=5):
    """
    Get questions for a specific age group and concern category.
    
    Args:
        age_group: str - "teenager", "young_adult", or "adult"
        concern_category: str - "menstrual", "pain", "hormonal", "mood", "weight", "other"
        limit: int - Maximum number of questions to return (default: 5)
    
    Returns:
        list: List of question dictionaries
    """
    age_key = age_group if age_group in PROMPTS else "teenager"
    category_key = concern_category if concern_category in PROMPTS[age_key] else "other"
    
    questions = PROMPTS.get(age_key, {}).get(category_key, [])
    return questions[:limit]


def get_all_questions_for_category(age_group, concern_category):
    """Get all questions for a category (no limit)."""
    return get_questions_for_category(age_group, concern_category, limit=100)
