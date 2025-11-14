#!/usr/bin/env python3
"""
Script to fetch GitHub Stars contributions and parse them into JSON and CSV formats.
Then compare with existing website content and identify missing events.
"""

import json
import csv
import os
import sys
import requests
from datetime import datetime
from pathlib import Path

def fetch_github_stars_contributions(token):
    """
    Fetch contributions from GitHub Stars API.
    
    Args:
        token: GitHub Stars API token
    
    Returns:
        dict: API response data
    """
    # The API endpoint - to be determined based on API documentation
    # Common patterns could be:
    # - /api/profiles/{username}/contributions
    # - /api/v1/contributions
    # - /api/me/contributions
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    
    # Try different potential endpoints
    base_url = 'https://api-stars.github.com'
    potential_endpoints = [
        '/profiles/yabellini/contributions',
        '/api/profiles/yabellini/contributions',
        '/me/contributions',
        '/api/me/contributions',
        '/api/v1/contributions',
        '/contributions'
    ]
    
    for endpoint in potential_endpoints:
        url = base_url + endpoint
        try:
            response = requests.get(url, headers=headers, timeout=30)
            print(f"Trying endpoint: {url} - Status: {response.status_code}")
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                continue
            else:
                print(f"Response: {response.text[:200]}")
        except Exception as e:
            print(f"Error with {url}: {str(e)}")
            continue
    
    print("Could not find valid API endpoint. Please check API documentation.")
    return None

def parse_contributions_to_json(data, output_file):
    """
    Parse contributions data and save as JSON.
    
    Args:
        data: Contributions data from API
        output_file: Path to output JSON file
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved JSON to: {output_file}")

def parse_contributions_to_csv(data, output_file):
    """
    Parse contributions data and save as CSV.
    
    Args:
        data: Contributions data from API
        output_file: Path to output CSV file
    """
    # This will need to be adapted based on actual API response structure
    # For now, create a generic parser
    
    events = []
    
    # Try to extract events from common response structures
    if isinstance(data, dict):
        if 'contributions' in data:
            events = data['contributions']
        elif 'events' in data:
            events = data['events']
        elif 'items' in data:
            events = data['items']
        else:
            # If data itself is the events list
            events = [data]
    elif isinstance(data, list):
        events = data
    
    if not events:
        print("Warning: No events found in data")
        return
    
    # Extract all possible fields from events
    all_fields = set()
    for event in events:
        if isinstance(event, dict):
            all_fields.update(event.keys())
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=sorted(all_fields))
        writer.writeheader()
        for event in events:
            if isinstance(event, dict):
                writer.writerow(event)
    
    print(f"Saved CSV to: {output_file}")

def load_existing_talks():
    """
    Load existing talks from the website.
    
    Returns:
        list: List of existing talk titles/identifiers
    """
    talks_dir = Path('/home/runner/work/SitioAcademico/SitioAcademico/content/talk')
    existing_talks = []
    
    for talk_folder in talks_dir.iterdir():
        if talk_folder.is_dir() and not talk_folder.name.startswith('.'):
            index_file = talk_folder / 'index.md'
            if index_file.exists():
                # Read the index.md file to get title and other metadata
                with open(index_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    existing_talks.append({
                        'folder': talk_folder.name,
                        'path': str(talk_folder),
                        'content': content
                    })
    
    return existing_talks

def load_existing_blogs():
    """
    Load existing blog posts from the website.
    
    Returns:
        list: List of existing blog titles/identifiers
    """
    blogs_dir = Path('/home/runner/work/SitioAcademico/SitioAcademico/content/blog')
    existing_blogs = []
    
    for blog_folder in blogs_dir.iterdir():
        if blog_folder.is_dir() and not blog_folder.name.startswith('.'):
            index_file = blog_folder / 'index.md'
            if index_file.exists():
                # Read the index.md file to get title and other metadata
                with open(index_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    existing_blogs.append({
                        'folder': blog_folder.name,
                        'path': str(blog_folder),
                        'content': content
                    })
    
    return existing_blogs

def compare_and_find_missing(contributions, existing_talks, existing_blogs):
    """
    Compare contributions with existing content and find missing items.
    
    Args:
        contributions: List of contributions from GitHub Stars
        existing_talks: List of existing talks
        existing_blogs: List of existing blogs
    
    Returns:
        list: Missing contributions not in website
    """
    missing = []
    
    # Extract titles and dates from existing content
    existing_talk_titles = set()
    existing_talk_dates = set()
    for talk in existing_talks:
        # Parse frontmatter to get title and date
        import re
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', talk['content'], re.MULTILINE)
        date_match = re.search(r'^date:\s*["\']?(\d{4}-\d{2}-\d{2})', talk['content'], re.MULTILINE)
        
        if title_match:
            existing_talk_titles.add(title_match.group(1).lower().strip())
        if date_match:
            existing_talk_dates.add(date_match.group(1))
    
    existing_blog_titles = set()
    existing_blog_dates = set()
    for blog in existing_blogs:
        # Parse frontmatter to get title and date
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', blog['content'], re.MULTILINE)
        date_match = re.search(r'^date:\s*["\']?(\d{4}-\d{2}-\d{2})', blog['content'], re.MULTILINE)
        
        if title_match:
            existing_blog_titles.add(title_match.group(1).lower().strip())
        if date_match:
            existing_blog_dates.add(date_match.group(1))
    
    print(f"\nExisting content analysis:")
    print(f"  Talk titles: {len(existing_talk_titles)}")
    print(f"  Talk dates: {len(existing_talk_dates)}")
    print(f"  Blog titles: {len(existing_blog_titles)}")
    print(f"  Blog dates: {len(existing_blog_dates)}")
    
    # Process contributions
    if isinstance(contributions, dict):
        if 'contributions' in contributions:
            contrib_list = contributions['contributions']
        elif 'events' in contributions:
            contrib_list = contributions['events']
        elif 'items' in contributions:
            contrib_list = contributions['items']
        else:
            contrib_list = [contributions]
    elif isinstance(contributions, list):
        contrib_list = contributions
    else:
        print("Warning: Unexpected contributions format")
        return missing
    
    print(f"\nAnalyzing {len(contrib_list)} contributions...")
    
    for contrib in contrib_list:
        if not isinstance(contrib, dict):
            continue
        
        title = contrib.get('title', '').lower().strip()
        date = contrib.get('date', '')
        contrib_type = contrib.get('type', '').lower()
        
        if not title:
            continue
        
        # Check if it's a talk or blog
        is_talk = contrib_type in ['talk', 'presentation', 'keynote', 'workshop', 'course', 'panel']
        is_blog = contrib_type in ['blog', 'post', 'article', 'writing']
        
        # If type not specified, try to infer from title or other fields
        if not is_talk and not is_blog:
            event_field = contrib.get('event', '').lower()
            if event_field or 'conference' in title or 'talk' in title:
                is_talk = True
            else:
                is_blog = True
        
        # Check if exists
        found = False
        if is_talk and title in existing_talk_titles:
            found = True
        elif is_blog and title in existing_blog_titles:
            found = True
        
        # Also check by date if available
        if not found and date:
            if is_talk and date in existing_talk_dates:
                found = True
            elif is_blog and date in existing_blog_dates:
                found = True
        
        if not found:
            contrib['inferred_type'] = 'talk' if is_talk else 'blog'
            missing.append(contrib)
    
    print(f"\nFound {len(missing)} missing contributions")
    return missing

def main():
    """Main execution function."""
    # Check if a local data file was provided as an argument
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        print(f"Loading data from local file: {input_file}")
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                if input_file.endswith('.json'):
                    contributions_data = json.load(f)
                elif input_file.endswith('.html'):
                    # If HTML file provided, we'll need to parse it
                    print("HTML parsing not yet implemented. Please provide JSON or CSV.")
                    sys.exit(1)
                else:
                    print("Unsupported file format. Please provide JSON or HTML file.")
                    sys.exit(1)
        except Exception as e:
            print(f"Error loading file: {str(e)}")
            sys.exit(1)
    else:
        # Get token from environment variable
        token = os.environ.get('GITHUB_STARS_TOKEN')
        
        if not token:
            print("Error: GITHUB_STARS_TOKEN environment variable not set")
            print("Please provide either:")
            print("  1. Set GITHUB_STARS_TOKEN environment variable")
            print("  2. Pass a JSON file as argument: python3 parse_github_stars.py data.json")
            sys.exit(1)
        
        print("Fetching GitHub Stars contributions...")
        contributions_data = fetch_github_stars_contributions(token)
        
        if contributions_data is None:
            print("Failed to fetch contributions data")
            print("\nPlease provide the data as a JSON file instead:")
            print("  python3 parse_github_stars.py contributions.json")
            sys.exit(1)
    
    # Create output directory
    output_dir = Path('/home/runner/work/SitioAcademico/SitioAcademico/datos')
    output_dir.mkdir(exist_ok=True)
    
    # Save as JSON
    json_file = output_dir / 'github_stars_contributions.json'
    parse_contributions_to_json(contributions_data, json_file)
    
    # Save as CSV
    csv_file = output_dir / 'github_stars_contributions.csv'
    parse_contributions_to_csv(contributions_data, csv_file)
    
    # Load existing content
    print("\nLoading existing talks and blog posts...")
    existing_talks = load_existing_talks()
    existing_blogs = load_existing_blogs()
    
    # Compare and find missing
    print("\nComparing with existing content...")
    missing = compare_and_find_missing(contributions_data, existing_talks, existing_blogs)
    
    # Save missing items list
    if missing:
        missing_file = output_dir / 'missing_contributions.json'
        with open(missing_file, 'w', encoding='utf-8') as f:
            json.dump(missing, f, indent=2, ensure_ascii=False)
        print(f"\nFound {len(missing)} missing contributions")
        print(f"Saved to: {missing_file}")
    else:
        print("\nNo missing contributions identified (or comparison needs refinement)")
    
    print("\n✓ Data fetching and parsing complete!")
    print(f"  - JSON: {json_file}")
    print(f"  - CSV: {csv_file}")

if __name__ == '__main__':
    main()
