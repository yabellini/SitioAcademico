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
    
    # This will need to be customized based on actual API response structure
    # For now, return placeholder
    
    print(f"Total contributions from API: {len(contributions) if isinstance(contributions, list) else 'N/A'}")
    print(f"Total existing talks: {len(existing_talks)}")
    print(f"Total existing blogs: {len(existing_blogs)}")
    
    return missing

def main():
    """Main execution function."""
    # Get token from environment variable or command line
    token = os.environ.get('GITHUB_STARS_TOKEN')
    
    if not token:
        print("Error: GITHUB_STARS_TOKEN environment variable not set")
        print("Please set it with: export GITHUB_STARS_TOKEN='your-token-here'")
        sys.exit(1)
    
    print("Fetching GitHub Stars contributions...")
    contributions_data = fetch_github_stars_contributions(token)
    
    if contributions_data is None:
        print("Failed to fetch contributions data")
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
