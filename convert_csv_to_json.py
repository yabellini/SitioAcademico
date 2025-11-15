#!/usr/bin/env python3
"""
Script to convert GitHub Stars contributions CSV to JSON format.
"""

import csv
import json
from pathlib import Path
from datetime import datetime

def convert_csv_to_json(csv_file):
    """
    Convert GitHub Stars CSV to JSON format.
    
    Args:
        csv_file: Path to CSV file
    
    Returns:
        list: List of contribution dictionaries
    """
    contributions = []
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Parse the date
            date_str = row.get('Date', '')
            if date_str:
                try:
                    # Parse ISO format date
                    date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                    date_formatted = date_obj.strftime('%Y-%m-%d')
                except:
                    date_formatted = date_str
            else:
                date_formatted = ''
            
            # Determine type
            contrib_type = row.get('Type', '').lower()
            if contrib_type == 'blogpost':
                inferred_type = 'blog'
            elif contrib_type in ['speaking', 'event_organization', 'hackathon', 'video_podcast']:
                # These are typically talks/presentations
                inferred_type = 'talk'
            elif contrib_type in ['article_publication']:
                # Could be either, default to blog
                inferred_type = 'blog'
            elif contrib_type in ['open_source_project']:
                # Projects should probably be talks or blogs, lean towards blog
                inferred_type = 'blog'
            else:
                # For 'other' and unknown, check title/description
                title_lower = row.get('Title', '').lower()
                desc_lower = row.get('Description', '').lower()
                
                # Look for talk indicators
                if any(word in title_lower or word in desc_lower for word in 
                       ['talk', 'presentation', 'keynote', 'workshop', 'conference', 
                        'panel', 'seminar', 'speaker', 'speaking', 'charla', 'curso']):
                    inferred_type = 'talk'
                else:
                    inferred_type = 'blog'
            
            contribution = {
                'id': row.get('ID', ''),
                'title': row.get('Title', ''),
                'description': row.get('Description', ''),
                'date': date_formatted,
                'type': contrib_type,
                'inferred_type': inferred_type,
                'url': row.get('URL', ''),
                'categories': ['English'],  # Default, can be refined
                'tags': []
            }
            
            contributions.append(contribution)
    
    return contributions

def main():
    """Main execution function."""
    csv_file = Path('/home/runner/work/SitioAcademico/SitioAcademico/contributions.csv')
    
    if not csv_file.exists():
        print("Error: contributions.csv not found")
        return
    
    print(f"Converting {csv_file}...")
    contributions = convert_csv_to_json(csv_file)
    
    print(f"Parsed {len(contributions)} contributions")
    
    # Save as JSON
    output_dir = Path('/home/runner/work/SitioAcademico/SitioAcademico/datos')
    output_dir.mkdir(exist_ok=True)
    
    json_file = output_dir / 'github_stars_contributions.json'
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(contributions, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Saved to: {json_file}")
    
    # Also save as CSV in datos folder
    csv_output = output_dir / 'github_stars_contributions.csv'
    with open(csv_output, 'w', encoding='utf-8', newline='') as f:
        if contributions:
            fieldnames = contributions[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contributions)
    
    print(f"✓ Saved CSV to: {csv_output}")
    
    # Show statistics
    types_count = {}
    for contrib in contributions:
        t = contrib.get('type', 'unknown')
        types_count[t] = types_count.get(t, 0) + 1
    
    print("\nContribution types:")
    for t, count in sorted(types_count.items(), key=lambda x: x[1], reverse=True):
        print(f"  {t}: {count}")

if __name__ == '__main__':
    main()
