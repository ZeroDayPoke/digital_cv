# ./seeders/blogs.py

from app.models import Blog
from app import db

def seed_blogs():
    """Seed the blogs table"""

    blogs = [
        {"name": "My Journey to Programming", "description": "A blog post about how I got into programming.", "content_file": "journey", "image_filename": "notfound1.png"},
    ]
    existing_blogs = [b.name for b in Blog.query.all()]
    for blog_data in blogs:
        if blog_data["name"] not in existing_blogs:
            blog = Blog(**blog_data)
            db.session.add(blog)
    db.session.commit()
