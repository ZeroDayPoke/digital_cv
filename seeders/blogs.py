# ./seeders/blogs.py

from app.models import Blog
from app import db


def seed_blogs():
    """Seed the blogs table"""

    blogs = [
        {"name": "cnn", "description": "cnn",
            "content_file": "cnn", "image_filename": ""},
        {"name": "optimization", "description": "optimization",
            "content_file": "optimization", "image_filename": ""},
        {"name": "regularization", "description": "regularization",
            "content_file": "regularization", "image_filename": ""}
    ]
    existing_blogs = [b.name for b in Blog.query.all()]
    for blog_data in blogs:
        if blog_data["name"] not in existing_blogs:
            blog = Blog(**blog_data)
            db.session.add(blog)
    db.session.commit()
