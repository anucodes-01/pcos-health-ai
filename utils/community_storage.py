"""
Community posts storage - persistent storage for community posts
"""

import json
import os
from datetime import datetime
from pathlib import Path

POSTS_FILE = "data/community_posts.json"

def init_posts_file():
    """Initialize posts file if it doesn't exist"""
    os.makedirs(os.path.dirname(POSTS_FILE), exist_ok=True)
    if not os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f)

def load_posts():
    """Load all posts from file"""
    init_posts_file()
    try:
        with open(POSTS_FILE, 'r', encoding='utf-8') as f:
            posts = json.load(f)
            # Sort by timestamp (newest first)
            return sorted(posts, key=lambda x: x.get('timestamp', ''), reverse=True)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_post(title, content, author, anonymous=True):
    """
    Save a new post
    
    Args:
        title: Post title
        content: Post content
        author: Author email or 'Anonymous'
        anonymous: Whether post is anonymous
    
    Returns:
        dict: Saved post data
    """
    posts = load_posts()
    
    post = {
        'id': len(posts) + 1,
        'title': title or 'Untitled',
        'content': content,
        'author': 'Anonymous' if anonymous else author,
        'author_email': None if anonymous else author,
        'timestamp': datetime.now().isoformat(),
        'likes': 0,
        'comments': []
    }
    
    posts.append(post)
    
    init_posts_file()
    with open(POSTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    
    return post

def get_recent_posts(limit=10):
    """Get recent posts"""
    posts = load_posts()
    return posts[:limit]
