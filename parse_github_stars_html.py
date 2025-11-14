#!/usr/bin/env python3
"""
Script to parse GitHub Stars contributions from HTML content.
This is an alternative to the API-based approach when the API is not accessible.
"""

import json
import csv
import sys
import re
from pathlib import Path
from bs4 import BeautifulSoup

def parse_html_contributions(html_content):
    """
    Parse contributions from GitHub Stars HTML.
    
    Args:
        html_content: HTML string from the contributions page
    
    Returns:
        list: List of contribution dictionaries
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    contributions = []
    
    # Look for common patterns in contribution listings
    # This will need to be adjusted based on actual HTML structure
    
    # Try to find contribution cards/items
    contribution_items = soup.find_all(['article', 'div'], class_=re.compile(r'contribution|event|activity', re.I))
    
    if not contribution_items:
        # Try alternative selectors
        contribution_items = soup.find_all(['li', 'div'], class_=re.compile(r'item|card', re.I))
    
    for item in contribution_items:
        contribution = {}
        
        # Try to extract title
        title_elem = item.find(['h1', 'h2', 'h3', 'h4', 'a'], class_=re.compile(r'title|heading', re.I))
        if title_elem:
            contribution['title'] = title_elem.get_text(strip=True)
        
        # Try to extract date
        date_elem = item.find(['time', 'span'], class_=re.compile(r'date|time', re.I))
        if date_elem:
            contribution['date'] = date_elem.get_text(strip=True)
            # Also check for datetime attribute
            if date_elem.has_attr('datetime'):
                contribution['datetime'] = date_elem['datetime']
        
        # Try to extract description
        desc_elem = item.find(['p', 'div'], class_=re.compile(r'description|excerpt|summary', re.I))
        if desc_elem:
            contribution['description'] = desc_elem.get_text(strip=True)
        
        # Try to extract link
        link_elem = item.find('a', href=True)
        if link_elem:
            contribution['url'] = link_elem['href']
        
        # Try to extract type/category
        type_elem = item.find(['span', 'div'], class_=re.compile(r'type|category|tag', re.I))
        if type_elem:
            contribution['type'] = type_elem.get_text(strip=True)
        
        if contribution:  # Only add if we extracted some data
            contributions.append(contribution)
    
    print(f"Parsed {len(contributions)} contributions from HTML")
    return contributions

def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: python3 parse_github_stars_html.py <html_file>")
        print("\nProvide the HTML file downloaded from GitHub Stars contributions page")
        sys.exit(1)
    
    html_file = sys.argv[1]
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        print(f"Error reading HTML file: {str(e)}")
        sys.exit(1)
    
    print(f"Parsing HTML from: {html_file}")
    contributions = parse_html_contributions(html_content)
    
    if not contributions:
        print("\nWarning: No contributions found in HTML.")
        print("The HTML structure might be different than expected.")
        print("Please share the HTML file for manual inspection.")
        sys.exit(1)
    
    # Save as JSON
    output_dir = Path('/home/runner/work/SitioAcademico/SitioAcademico/datos')
    output_dir.mkdir(exist_ok=True)
    
    json_file = output_dir / 'github_stars_contributions.json'
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(contributions, f, indent=2, ensure_ascii=False)
    print(f"Saved JSON to: {json_file}")
    
    # Save as CSV
    if contributions:
        csv_file = output_dir / 'github_stars_contributions.csv'
        all_fields = set()
        for contrib in contributions:
            all_fields.update(contrib.keys())
        
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=sorted(all_fields))
            writer.writeheader()
            writer.writerows(contributions)
        print(f"Saved CSV to: {csv_file}")
    
    print("\n✓ HTML parsing complete!")
    print(f"  Found {len(contributions)} contributions")
    
    # Show sample of first few contributions
    print("\nSample contributions:")
    for i, contrib in enumerate(contributions[:3], 1):
        print(f"\n{i}. {contrib.get('title', 'No title')}")
        print(f"   Date: {contrib.get('date', 'No date')}")
        print(f"   Type: {contrib.get('type', 'Unknown')}")

if __name__ == '__main__':
    main()
