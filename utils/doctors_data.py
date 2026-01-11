"""
Doctor data with location-based information
"""

DOCTORS_DATA = {
    'mumbai': [
        {
            "name": "Dr. Priya Sharma",
            "specialization": "Reproductive Health, PCOS",
            "location": "Andheri West, Mumbai",
            "distance": "2.3 km",
            "phone": "+91 22 1234 5678",
            "rating": "4.8"
        },
        {
            "name": "Dr. Anjali Patel",
            "specialization": "Women's Health, Endocrinology",
            "location": "Bandra, Mumbai",
            "distance": "5.1 km",
            "phone": "+91 22 2345 6789",
            "rating": "4.6"
        },
        {
            "name": "Dr. Meera Desai",
            "specialization": "Gynecology, Hormonal Disorders",
            "location": "Powai, Mumbai",
            "distance": "7.8 km",
            "phone": "+91 22 3456 7890",
            "rating": "4.9"
        }
    ],
    'delhi': [
        {
            "name": "Dr. Kavita Singh",
            "specialization": "Reproductive Endocrinology",
            "location": "Connaught Place, Delhi",
            "distance": "1.5 km",
            "phone": "+91 11 1234 5678",
            "rating": "4.7"
        },
        {
            "name": "Dr. Neha Gupta",
            "specialization": "Gynecology, PCOS Management",
            "location": "Gurgaon, Delhi NCR",
            "distance": "12.3 km",
            "phone": "+91 11 2345 6789",
            "rating": "4.8"
        },
        {
            "name": "Dr. Pooja Verma",
            "specialization": "Women's Health, PCOS",
            "location": "Saket, Delhi",
            "distance": "8.2 km",
            "phone": "+91 11 3456 7890",
            "rating": "4.5"
        }
    ],
    'bangalore': [
        {
            "name": "Dr. Shilpa Reddy",
            "specialization": "Reproductive Health, PCOS",
            "location": "Koramangala, Bangalore",
            "distance": "3.2 km",
            "phone": "+91 80 1234 5678",
            "rating": "4.9"
        },
        {
            "name": "Dr. Anitha Rao",
            "specialization": "Women's Health, Endocrinology",
            "location": "Indiranagar, Bangalore",
            "distance": "5.7 km",
            "phone": "+91 80 2345 6789",
            "rating": "4.6"
        },
        {
            "name": "Dr. Lakshmi Nair",
            "specialization": "Gynecology, Hormonal Disorders",
            "location": "Whitefield, Bangalore",
            "distance": "15.4 km",
            "phone": "+91 80 3456 7890",
            "rating": "4.7"
        }
    ],
    'default': [
        {
            "name": "Dr. Sarah Johnson",
            "specialization": "Reproductive Health, PCOS",
            "location": "Downtown Medical Center",
            "distance": "2.5 miles",
            "phone": "+1 123-456-7890",
            "rating": "4.8"
        },
        {
            "name": "Dr. Maria Rodriguez",
            "specialization": "Women's Health, Endocrinology",
            "location": "City Health Clinic",
            "distance": "3.8 miles",
            "phone": "+1 234-567-8901",
            "rating": "4.6"
        },
        {
            "name": "Dr. Priya Patel",
            "specialization": "Gynecology, Hormonal Disorders",
            "location": "Community Hospital",
            "distance": "5.2 miles",
            "phone": "+1 345-678-9012",
            "rating": "4.7"
        }
    ]
}

def get_doctors_by_location(location):
    """
    Get doctors based on location
    
    Args:
        location: City name or location string
    
    Returns:
        list: List of doctor dictionaries
    """
    location_lower = location.lower() if location else ''
    
    # Check for major cities
    if 'mumbai' in location_lower or 'bombay' in location_lower:
        return DOCTORS_DATA.get('mumbai', DOCTORS_DATA['default'])
    elif 'delhi' in location_lower or 'ncr' in location_lower or 'gurgaon' in location_lower:
        return DOCTORS_DATA.get('delhi', DOCTORS_DATA['default'])
    elif 'bangalore' in location_lower or 'bengaluru' in location_lower:
        return DOCTORS_DATA.get('bangalore', DOCTORS_DATA['default'])
    else:
        return DOCTORS_DATA['default']
