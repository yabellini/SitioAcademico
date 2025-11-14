#!/usr/bin/env python3
"""
Script to convert plain text contributions list to structured JSON.
Useful when user can only provide text copy-paste from the page.

Usage:
    python3 parse_text_contributions.py contributions.txt
    
The text file should contain contributions in a simple format like:
    Title of Event 1
    Date: 2024-03-15
    Type: Talk
    Location: Online
    Description: Brief description
    ---
    Title of Event 2
    Date: 2024-02-10
    ...
"""

import json
import sys
import re
from pathlib import Path
from datetime import datetime

def parse_text_contributions(text):
    """
    Parse contributions from plain text format.
    
    Args:
        text: Plain text with contributions
    
    Returns:
        list: List of contribution dictionaries
    """
    contributions = []
    
    # Split by separator (---, blank lines, or numbered items)
    # Try different splitting patterns
    sections = re.split(r'\n(?:---+|\d+\.|•)\s*\n', text)
    
    if len(sections) <= 1:
        # Try splitting by double newlines
        sections = text.split('\n\n')
    
    for section in sections:
        if not section.strip():
            continue
        
        contrib = {}
        lines = section.strip().split('\n')
        
        # Try to parse structured format (Key: Value)
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check for key: value pattern
            match = re.match(r'^([^:]+):\s*(.+)$', line)
            if match:
                key = match.group(1).strip().lower()
                value = match.group(2).strip()
                
                # Map common field names
                if key in ['title', 'name', 'event']:
                    contrib['title'] = value
                elif key in ['date', 'when', 'time']:
                    contrib['date'] = value
                elif key in ['type', 'kind', 'category']:
                    contrib['type'] = value
                elif key in ['location', 'where', 'place']:
                    contrib['location'] = value
                elif key in ['description', 'desc', 'about', 'summary']:
                    contrib['description'] = value
                elif key in ['url', 'link', 'website']:
                    contrib['url'] = value
                elif key in ['event', 'conference', 'venue']:
                    contrib['event'] = value
            else:
                # First line without colon is likely the title
                if 'title' not in contrib and line and not line.startswith(('http://', 'https://')):
                    contrib['title'] = line
        
        if contrib and 'title' in contrib:
            contributions.append(contrib)
    
    # If no structured parsing worked, try simple bullet point or numbered list
    if not contributions:
        lines = text.split('\n')
        current_contrib = None
        
        for line in lines:
            line = line.strip()
            if not line:
                if current_contrib:
                    contributions.append(current_contrib)
                    current_contrib = None
                continue
            
            # Check if it's a new item (numbered or bulleted)
            if re.match(r'^\d+\.|^[-•*]\s+', line):
                if current_contrib:
                    contributions.append(current_contrib)
                current_contrib = {'title': re.sub(r'^\d+\.|^[-•*]\s+', '', line)}
            elif current_contrib:
                # Add as description
                if 'description' not in current_contrib:
                    current_contrib['description'] = line
                else:
                    current_contrib['description'] += ' ' + line
        
        if current_contrib:
            contributions.append(current_contrib)
    
    return contributions

def interactive_enrichment(contributions):
    """
    Interactively enrich contributions with missing data.
    
    Args:
        contributions: List of contribution dictionaries
    
    Returns:
        list: Enriched contributions
    """
    print("\nEnriching contributions data...")
    print("Press Enter to skip a field.\n")
    
    for i, contrib in enumerate(contributions, 1):
        print(f"\n--- Contribution {i}/{len(contributions)} ---")
        print(f"Title: {contrib.get('title', 'N/A')}")
        
        # Ask for missing fields
        if 'date' not in contrib:
            date = input("Date (YYYY-MM-DD): ").strip()
            if date:
                contrib['date'] = date
        
        if 'type' not in contrib:
            type_val = input("Type (talk/blog/article/workshop/etc): ").strip()
            if type_val:
                contrib['type'] = type_val
        
        if 'location' not in contrib:
            location = input("Location (or 'online'): ").strip()
            if location:
                contrib['location'] = location
        
        if 'description' not in contrib:
            description = input("Description: ").strip()
            if description:
                contrib['description'] = description
        
        if 'url' not in contrib:
            url = input("URL: ").strip()
            if url:
                contrib['url'] = url
    
    return contributions

def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: python3 parse_text_contributions.py <text_file>")
        print("\nProvide a text file with contributions information.")
        print("The script will try to parse it and create structured JSON.")
        sys.exit(1)
    
    text_file = sys.argv[1]
    
    try:
        with open(text_file, 'r', encoding='utf-8') as f:
            text_content = f.read()
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)
    
    print(f"Parsing text from: {text_file}")
    contributions = parse_text_contributions(text_content)
    
    if not contributions:
        print("\nWarning: Could not parse any contributions from the text.")
        print("Please check the format or try the interactive mode.")
        sys.exit(1)
    
    print(f"\nParsed {len(contributions)} contributions")
    
    # Ask if user wants to enrich the data
    enrich = input("\nDo you want to interactively add missing information? (y/n): ").strip().lower()
    if enrich == 'y':
        contributions = interactive_enrichment(contributions)
    
    # Save as JSON
    output_dir = Path('/home/runner/work/SitioAcademico/SitioAcademico/datos')
    output_dir.mkdir(exist_ok=True)
    
    json_file = output_dir / 'github_stars_contributions.json'
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(contributions, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Saved to: {json_file}")
    print(f"  Total contributions: {len(contributions)}")
    
    # Show sample
    print("\nSample contributions:")
    for i, contrib in enumerate(contributions[:3], 1):
        print(f"\n{i}. {contrib.get('title', 'No title')}")
        print(f"   Date: {contrib.get('date', 'No date')}")
        print(f"   Type: {contrib.get('type', 'Unknown')}")
    
    print("\n\nNext step: Run the comparison script to find missing content:")
    print("  python3 parse_github_stars.py datos/github_stars_contributions.json")

if __name__ == '__main__':
    main()
