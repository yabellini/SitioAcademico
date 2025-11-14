# GitHub Stars Contributions Parsing

This document describes the process for parsing GitHub Stars contributions and adding them to the website.

## Overview

The task is to:
1. Fetch contributions from GitHub Stars API
2. Parse them into JSON and CSV formats
3. Compare with existing talks and blog posts on the website
4. Identify missing contributions
5. Create folders and index.md files for missing contributions

## Prerequisites

- GitHub Stars API token (provided by @yabellini)
- Python 3 with `requests` library

## Process

**Note:** The GitHub Stars domain is blocked in the automation environment. Please use one of these methods to provide the data:

### Quick Start: Run the Helper Script

```bash
cd /home/runner/work/SitioAcademico/SitioAcademico
./fetch_stars_profile.sh
```

This will display instructions for all available methods.

### Option 1: Copy/Paste Text from Page

1. Open: https://stars.github.com/profiles/yabellini/
2. Find and copy the "Community Contribution" section text
3. Save it to a file: `contributions.txt`
4. Run:

```bash
cd /home/runner/work/SitioAcademico/SitioAcademico
python3 parse_text_contributions.py contributions.txt
python3 parse_github_stars.py datos/github_stars_contributions.json
python3 create_missing_content.py
```

### Option 2: Save Page as HTML

1. Open: https://stars.github.com/profiles/yabellini/
2. Right-click → Save Page As → `contributions.html`
3. Upload to repository
4. Run:

```bash
cd /home/runner/work/SitioAcademico/SitioAcademico
python3 parse_github_stars_html.py contributions.html
python3 create_missing_content.py
```

### Option 3: Manual JSON Entry

1. Edit `contributions_template.json` with your contributions
2. Run:

```bash
cd /home/runner/work/SitioAcademico/SitioAcademico
python3 parse_github_stars.py contributions_template.json
python3 create_missing_content.py
```

### Option 4: Using API Token (if accessible)

```bash
export GITHUB_STARS_TOKEN='your-token-here'
cd /home/runner/work/SitioAcademico/SitioAcademico
python3 parse_github_stars.py
python3 create_missing_content.py
```

All approaches will:
- Save raw data to `datos/github_stars_contributions.json`
- Parse and save to `datos/github_stars_contributions.csv`
- Compare with existing content
- Generate list of missing contributions in `datos/missing_contributions.json`
- Create folders and index.md files for missing content

### Step 3: Create missing content

After identifying missing contributions, we'll create:
- For talks: `content/talk/{YEAR}_{Event_Name}/index.md`
- For blog posts: `content/blog/{DATE}-{slug}/index.md`

## Website Structure

### Talks
- Location: `content/talk/`
- Format: Each talk is in a folder named `{YEAR}_{Event_Name}/`
- Required file: `index.md` with frontmatter

Example frontmatter:
```yaml
---
title: "Talk Title"
excerpt: "Brief description"
date: 2024-03-12
date_end: "2024-03-12"
author: "Yanina Bellini Saibene"
location: "online"
event: "Event Name"
event_url: https://example.com
draft: false
layout: single
categories:
- Category1
- Category2
tags:
- Tag1
- Tag2
links:
- icon: youtube
  icon_pack: fab
  name: video
  url: https://example.com/video
---

Content here...
```

### Blog Posts
- Location: `content/blog/`
- Format: Each post is in a folder named `{DATE}-{slug}/`
- Required file: `index.md` with frontmatter

Example frontmatter:
```yaml
---
title: Blog Post Title
author: Yanina Bellini Saibene
summary: "Brief summary"
date: '2025-02-09'
categories:
  - English
  - Category
tags:
  - Tag1
  - Tag2
---

Content here...
```

## Next Steps

Once the token is provided and data is fetched:
1. Review the API response structure
2. Refine the comparison logic to properly match events
3. Generate missing content folders and index files
4. Validate the generated content

## Files

- `parse_github_stars.py` - Main parsing script
- `datos/github_stars_contributions.json` - Raw API data
- `datos/github_stars_contributions.csv` - Parsed CSV
- `datos/missing_contributions.json` - List of missing items
