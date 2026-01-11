"""
Community - Safe space for support and sharing with persistent posts
"""

import streamlit as st
from utils.community_storage import load_posts, save_post, get_recent_posts
from utils.auth import is_authenticated, get_current_user
from utils.translations import t, get_language
from utils.language_switcher import render_language_switcher

st.set_page_config(
    page_title="PCOS Health AI - Community",
    page_icon="👥",
    layout="wide"
)

# Initialize language
if 'language' not in st.session_state:
    st.session_state['language'] = 'en'

# Language switcher
render_language_switcher()

st.title("Community")
st.markdown("### A Safe Space for Support & Sharing")

# Community Guidelines
with st.expander("📜 Community Guidelines", expanded=True):
    st.markdown("""
    **Our Community Rules:**
    - ✅ Be respectful and kind
    - ✅ Share experiences, not medical advice
    - ✅ Respect privacy (anonymous by default)
    - ❌ No personal attacks
    - ❌ No medical diagnosis or prescriptions
    - ❌ No spam or promotional content
    
    **Remember:** This is a supportive space, not a replacement for professional care.
    """)

# Load and display posts
posts = get_recent_posts(limit=20)

st.markdown("---")
st.markdown("### Recent Posts")

if posts:
    for post in posts:
        # Format timestamp
        from datetime import datetime
        try:
            post_time = datetime.fromisoformat(post['timestamp'])
            time_ago = (datetime.now() - post_time).days
            if time_ago == 0:
                time_str = "Today"
            elif time_ago == 1:
                time_str = "1 day ago"
            else:
                time_str = f"{time_ago} days ago"
        except:
            time_str = "Recently"
        
        st.markdown(f"""
        <div style='padding: 20px; border-radius: 10px; background: linear-gradient(135deg, #FFF5F8 0%, #F8E8F0 100%); 
                    margin-bottom: 15px; border-left: 4px solid #D9469F; box-shadow: 0 2px 4px rgba(217, 70, 159, 0.1);'>
            <strong style='color: #D9469F;'>{post['author']}</strong> • <span style='color: #8B4A6B;'>{time_str}</span><br>
            <h4 style='color: #2D1B3D; margin-top: 10px;'>{post['title']}</h4>
            <p style='color: #2D1B3D;'>{post['content']}</p>
            <small style='color: #8B4A6B;'>Likes: {post.get('likes', 0)}</small>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No posts yet. Be the first to share!")

# Create Post Section
st.markdown("---")
st.markdown("### Create a Post")

post_title = st.text_input("Title (optional)", key="post_title")
post_content = st.text_area("Share your thoughts...", height=150, key="post_content")

col1, col2 = st.columns(2)
with col1:
    post_anonymously = st.checkbox("Post anonymously", value=True, key="post_anon")
with col2:
    if st.button("Post", type="primary", use_container_width=True):
        if post_content:
            user = get_current_user()
            author_email = user['email'] if (user and not post_anonymously) else None
            author_name = user['name'] if (user and not post_anonymously) else None
            
            save_post(
                title=post_title,
                content=post_content,
                author=author_email or author_name or "Anonymous",
                anonymous=post_anonymously
            )
            st.success("Post created successfully!")
            st.rerun()
        else:
            st.warning("Please write something to post.")

# Disclaimer
st.markdown("---")
st.markdown("""
<div style='padding: 16px; border-radius: 8px; background-color: #FFE5F1; border-left: 4px solid #D9469F;'>
    <p style='color: #8B4A6B; margin: 0;'><strong>Community Disclaimer:</strong> Posts and comments are for support and sharing only. 
    They do not constitute medical advice. Always consult healthcare professionals for medical concerns.</p>
</div>
""", unsafe_allow_html=True)
