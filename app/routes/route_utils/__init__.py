#!/usr/bin/env python3

"""
route_utils.py - utility functions for routes

# Path: app/routes/route_utils.py
"""

from .choice_selectors import (
    load_project_choices, load_skill_choices, load_blog_choices, load_tutorial_choices, load_category_choices
)

from .decorators import admin_required
from .generate_filters import generate_filters
