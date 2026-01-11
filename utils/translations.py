"""
Multi-language translation support
Supports English and Hindi
"""

TRANSLATIONS = {
    'en': {
        # Navigation
        'home': 'Home',
        'health_check': 'Health Check',
        'ai_assistant': 'AI Assistant',
        'learn_conditions': 'Learn Conditions',
        'lifestyle_plan': 'Lifestyle Plan',
        'trackers': 'Trackers',
        'community': 'Community',
        'find_help': 'Find Help',
        'resources_faq': 'Resources & FAQ',
        
        # Common
        'welcome': 'Welcome',
        'login': 'Login',
        'logout': 'Logout',
        'register': 'Register',
        'email': 'Email',
        'phone': 'Phone Number',
        'password': 'Password',
        'name': 'Full Name',
        'submit': 'Submit',
        'cancel': 'Cancel',
        'save': 'Save',
        'delete': 'Delete',
        'edit': 'Edit',
        'close': 'Close',
        'next': 'Next',
        'back': 'Back',
        'continue': 'Continue',
        'search': 'Search',
        'download': 'Download',
        
        # Auth
        'login_title': 'Login to Your Account',
        'register_title': 'Create New Account',
        'login_success': 'Login successful!',
        'logout_success': 'Logged out successfully',
        'register_success': 'Registration successful!',
        'invalid_credentials': 'Invalid email or password',
        'email_exists': 'Email already registered',
        'phone_exists': 'Phone number already registered',
        
        # Health Check
        'health_check_title': 'Health Check',
        'analyze_patterns': 'Analyze My Health Patterns',
        'risk_level': 'Risk Level',
        'detected_pattern': 'Detected Pattern',
        'key_factors': 'Key Contributing Factors',
        'doctor_consultation': 'Medical Consultation Guidance',
        'consultation_recommended': 'Medical Consultation Recommended',
        'consultation_not_urgent': 'Medical Consultation Not Urgent',
        
        # Community
        'create_post': 'Create a Post',
        'post_title': 'Title (optional)',
        'post_content': 'Share your thoughts...',
        'post_anonymously': 'Post anonymously',
        'recent_posts': 'Recent Posts',
        'your_posts': 'Your Posts',
        
        # Find Help
        'nearby_doctors': 'Nearby Doctors',
        'enter_location': 'Enter your city or ZIP code',
        'find_doctors': 'Find Doctors Near You',
        
        # General
        'disclaimer': 'Disclaimer',
        'disclaimer_text': 'This tool is for awareness and support only. It does not provide medical diagnosis.',
    },
    'hi': {
        # Navigation
        'home': 'होम',
        'health_check': 'स्वास्थ्य जांच',
        'ai_assistant': 'AI सहायक',
        'learn_conditions': 'स्थितियां सीखें',
        'lifestyle_plan': 'जीवनशैली योजना',
        'trackers': 'ट्रैकर्स',
        'community': 'समुदाय',
        'find_help': 'मदद खोजें',
        'resources_faq': 'संसाधन और FAQ',
        
        # Common
        'welcome': 'स्वागत है',
        'login': 'लॉगिन',
        'logout': 'लॉगआउट',
        'register': 'पंजीकरण',
        'email': 'ईमेल',
        'phone': 'फोन नंबर',
        'password': 'पासवर्ड',
        'name': 'पूरा नाम',
        'submit': 'जमा करें',
        'cancel': 'रद्द करें',
        'save': 'सहेजें',
        'delete': 'हटाएं',
        'edit': 'संपादित करें',
        'close': 'बंद करें',
        'next': 'अगला',
        'back': 'वापस',
        'continue': 'जारी रखें',
        'search': 'खोजें',
        'download': 'डाउनलोड',
        
        # Auth
        'login_title': 'अपने खाते में लॉगिन करें',
        'register_title': 'नया खाता बनाएं',
        'login_success': 'लॉगिन सफल!',
        'logout_success': 'सफलतापूर्वक लॉगआउट किया गया',
        'register_success': 'पंजीकरण सफल!',
        'invalid_credentials': 'अमान्य ईमेल या पासवर्ड',
        'email_exists': 'ईमेल पहले से पंजीकृत है',
        'phone_exists': 'फोन नंबर पहले से पंजीकृत है',
        
        # Health Check
        'health_check_title': 'स्वास्थ्य जांच',
        'analyze_patterns': 'मेरे स्वास्थ्य पैटर्न का विश्लेषण करें',
        'risk_level': 'जोखिम स्तर',
        'detected_pattern': 'पता चला पैटर्न',
        'key_factors': 'मुख्य योगदान कारक',
        'doctor_consultation': 'चिकित्सा परामर्श मार्गदर्शन',
        'consultation_recommended': 'चिकित्सा परामर्श की सिफारिश की गई',
        'consultation_not_urgent': 'चिकित्सा परामर्श तत्काल नहीं',
        
        # Community
        'create_post': 'एक पोस्ट बनाएं',
        'post_title': 'शीर्षक (वैकल्पिक)',
        'post_content': 'अपने विचार साझा करें...',
        'post_anonymously': 'अज्ञात रूप से पोस्ट करें',
        'recent_posts': 'हाल की पोस्ट',
        'your_posts': 'आपकी पोस्ट',
        
        # Find Help
        'nearby_doctors': 'पास के डॉक्टर',
        'enter_location': 'अपना शहर या ज़िप कोड दर्ज करें',
        'find_doctors': 'अपने पास डॉक्टर खोजें',
        
        # General
        'disclaimer': 'अस्वीकरण',
        'disclaimer_text': 'यह उपकरण केवल जागरूकता और सहायता के लिए है। यह चिकित्सा निदान प्रदान नहीं करता है।',
    }
}

def get_translation(key, lang='en'):
    """Get translation for a key"""
    return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, key)

def get_language():
    """Get current language from session state"""
    return st.session_state.get('language', 'en')

def set_language(lang):
    """Set language in session state"""
    st.session_state['language'] = lang

def t(key):
    """Shortcut function to get translation"""
    lang = get_language()
    return get_translation(key, lang)
