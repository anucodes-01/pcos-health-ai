"""
Community - Safe space for support and sharing (demo/static content)
"""

import streamlit as st

st.set_page_config(
    page_title="PCOS Health AI - Community",
    page_icon="👥",
    layout="wide"
)

st.title("👥 Community")
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

# Demo Posts (Static Content)
st.markdown("---")
st.markdown("### 💬 Recent Posts")

# Demo Post 1
st.markdown("""
<div style='padding: 15px; border-radius: 8px; background-color: #F0F0F0; margin-bottom: 10px;'>
    <strong>Anonymous</strong> • 2 days ago<br>
    "Finally found people who understand what I'm going through. Thank you for this space! 💜"<br>
    <small>💬 5 comments • 👍 12 likes</small>
</div>
""", unsafe_allow_html=True)

# Demo Post 2
st.markdown("""
<div style='padding: 15px; border-radius: 8px; background-color: #F0F0F0; margin-bottom: 10px;'>
    <strong>Anonymous</strong> • 5 days ago<br>
    "Has anyone found lifestyle changes helpful? Looking for tips on managing symptoms naturally."<br>
    <small>💬 8 comments • 👍 15 likes</small>
</div>
""", unsafe_allow_html=True)

# Demo Post 3
st.markdown("""
<div style='padding: 15px; border-radius: 8px; background-color: #F0F0F0; margin-bottom: 10px;'>
    <strong>Anonymous</strong> • 1 week ago<br>
    "This platform helped me understand when to see a doctor. Got my diagnosis and feeling more empowered now!"<br>
    <small>💬 12 comments • 👍 23 likes</small>
</div>
""", unsafe_allow_html=True)

# Create Post Section
st.markdown("---")
st.markdown("### ✍️ Create a Post")

# Initialize session state for posts
if 'community_posts' not in st.session_state:
    st.session_state.community_posts = []

post_title = st.text_input("Title (optional)", key="post_title")
post_content = st.text_area("Share your thoughts...", height=150, key="post_content")

col1, col2 = st.columns(2)
with col1:
    post_anonymously = st.checkbox("Post anonymously", value=True, key="post_anon")
with col2:
    if st.button("📤 Post", type="primary"):
        if post_content:
            new_post = {
                "title": post_title,
                "content": post_content,
                "author": "Anonymous" if post_anonymously else "User",
                "timestamp": "Just now"
            }
            st.session_state.community_posts.append(new_post)
            st.success("Post created! (Stored in session only)")
            st.rerun()
        else:
            st.warning("Please write something to post.")

# Display user's posts
if st.session_state.community_posts:
    st.markdown("---")
    st.markdown("### 📝 Your Posts")
    for post in reversed(st.session_state.community_posts):
        with st.expander(f"📄 {post.get('title', 'Untitled')} - {post['author']} • {post['timestamp']}"):
            st.write(post['content'])

# Moderation Disclaimer
st.markdown("---")
st.warning("""
⚠️ **Note:** This is a demo/static community space. In a production version, 
posts would be moderated and stored securely. Always prioritize your privacy and safety.
""")

# Disclaimer
st.markdown("---")
st.error("""
⚠️ **Community Disclaimer:** Posts and comments are for support and sharing only. 
They do not constitute medical advice. Always consult healthcare professionals for medical concerns.
""")
