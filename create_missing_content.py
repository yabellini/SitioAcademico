#!/usr/bin/env python3
"""
Script to create folders and index.md files for missing GitHub Stars contributions.
Reads from datos/missing_contributions.json and creates the appropriate structure.
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime

def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def create_talk_folder(contrib, talks_dir):
    """
    Create a talk folder and index.md file.
    
    Args:
        contrib: Contribution dictionary
        talks_dir: Path to talks directory
    """
    title = contrib.get('title', 'Untitled')
    date_str = contrib.get('date', '')
    
    # Parse date
    if date_str:
        try:
            date_obj = datetime.fromisoformat(date_str.replace('/', '-'))
            year = date_obj.year
            date_formatted = date_obj.strftime('%Y-%m-%d')
        except:
            year = datetime.now().year
            date_formatted = date_str
    else:
        year = datetime.now().year
        date_formatted = datetime.now().strftime('%Y-%m-%d')
    
    # Create folder name: YEAR_Event_Name
    event = contrib.get('event', slugify(title))
    folder_name = f"{year}_{slugify(event)}"
    folder_path = talks_dir / folder_name
    
    # Check if folder already exists
    if folder_path.exists():
        print(f"  ⚠️  Talk folder already exists: {folder_name}")
        return False
    
    # Create folder
    folder_path.mkdir(parents=True)
    
    # Create index.md
    index_path = folder_path / 'index.md'
    
    # Extract information
    description = contrib.get('description', '')
    location = contrib.get('location', 'online')
    event_url = contrib.get('url', '')
    categories = contrib.get('categories', ['English'])
    tags = contrib.get('tags', [])
    
    # Create frontmatter
    content = f"""---
title: "{title}"
excerpt: "{description}"
date: {date_formatted}
date_end: "{date_formatted}"
author: "Yanina Bellini Saibene"
location: "{location}"
event: "{event}"
event_url: {event_url}
draft: false
layout: single
categories:
"""
    
    for cat in categories:
        content += f"- {cat}\n"
    
    if tags:
        content += "tags:\n"
        for tag in tags:
            content += f"- {tag}\n"
    
    if event_url:
        content += f"""links:
- icon: link
  icon_pack: fas
  name: event
  url: {event_url}
"""
    
    content += """---

"""
    
    if description:
        content += f"{description}\n"
    
    # Write file
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Created talk: {folder_name}")
    return True

def create_blog_folder(contrib, blogs_dir):
    """
    Create a blog folder and index.md file.
    
    Args:
        contrib: Contribution dictionary
        blogs_dir: Path to blogs directory
    """
    title = contrib.get('title', 'Untitled')
    date_str = contrib.get('date', '')
    
    # Parse date
    if date_str:
        try:
            date_obj = datetime.fromisoformat(date_str.replace('/', '-'))
            date_formatted = date_obj.strftime('%Y-%m-%d')
        except:
            date_formatted = date_str
    else:
        date_formatted = datetime.now().strftime('%Y-%m-%d')
    
    # Create folder name: DATE-slug
    slug = slugify(title)
    folder_name = f"{date_formatted}-{slug}"
    folder_path = blogs_dir / folder_name
    
    # Check if folder already exists
    if folder_path.exists():
        print(f"  ⚠️  Blog folder already exists: {folder_name}")
        return False
    
    # Create folder
    folder_path.mkdir(parents=True)
    
    # Create index.md
    index_path = folder_path / 'index.md'
    
    # Extract information
    description = contrib.get('description', '')
    categories = contrib.get('categories', ['English'])
    tags = contrib.get('tags', [])
    
    # Create frontmatter
    content = f"""---
title: {title}
author: Yanina Bellini Saibene
summary: "{description}"
date: '{date_formatted}'
categories:
"""
    
    for cat in categories:
        content += f"  - {cat}\n"
    
    if tags:
        content += "tags:\n"
        for tag in tags:
            content += f"  - {tag}\n"
    
    content += """
---

"""
    
    if description:
        content += f"{description}\n"
    
    # Write file
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Created blog: {folder_name}")
    return True

def main():
    """Main execution function."""
    # Load missing contributions
    missing_file = Path('/home/runner/work/SitioAcademico/SitioAcademico/datos/missing_contributions.json')
    
    if not missing_file.exists():
        print("Error: missing_contributions.json not found")
        print("Please run parse_github_stars.py first")
        return
    
    with open(missing_file, 'r', encoding='utf-8') as f:
        missing = json.load(f)
    
    if not missing:
        print("No missing contributions to create")
        return
    
    print(f"Creating folders for {len(missing)} missing contributions...\n")
    
    # Get directories
    base_dir = Path('/home/runner/work/SitioAcademico/SitioAcademico/content')
    talks_dir = base_dir / 'talk'
    blogs_dir = base_dir / 'blog'
    
    # Track statistics
    talks_created = 0
    blogs_created = 0
    
    # Create content for each missing contribution
    for contrib in missing:
        inferred_type = contrib.get('inferred_type', 'blog')
        
        if inferred_type == 'talk':
            if create_talk_folder(contrib, talks_dir):
                talks_created += 1
        else:
            if create_blog_folder(contrib, blogs_dir):
                blogs_created += 1
    
    print(f"\n✓ Content creation complete!")
    print(f"  Created {talks_created} talks")
    print(f"  Created {blogs_created} blog posts")
    
    if talks_created + blogs_created < len(missing):
        print(f"  Skipped {len(missing) - talks_created - blogs_created} (already existed)")

if __name__ == '__main__':
    main()
