#!/usr/bin/env python3

from bs4 import BeautifulSoup

def extract_sections_from_content(content_file):
    with open(content_file, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    sections = []

    for h2 in soup.find_all('h2'):
        title = h2.get_text()
        anchor = h2.attrs.get('id', '')
        sections.append({
            'title': title,
            'anchor': anchor
        })

    return sections
