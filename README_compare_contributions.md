# Comparison Script for GitHub Contributions

This script compares the GitHub contributions data with existing events and publications data.

## Purpose

The `compare_contributions.R` script:
1. Reads three CSV files from the `datos` folder:
   - `contributions-github.csv` - All GitHub Star contributions
   - `EventosPorAnioYanina-2025.csv` - Existing events data
   - `PublicacionesPorAnioYanina-2025.csv` - Existing publications data

2. Identifies contributions that are missing from the existing datasets

3. Generates two new CSV files with the missing data:
   - `datos/events.csv` - Events from GitHub contributions not in EventosPorAnioYanina-2025.csv
   - `datos/publications.csv` - Publications from GitHub contributions not in PublicacionesPorAnioYanina-2025.csv

## How to Run

```bash
Rscript compare_contributions.R
```

## Output Format

### events.csv
Contains the following columns matching EventosPorAnioYanina-2025.csv format:
- `Nombre` - Event name (from Title)
- `Institucion.Evento` - Institution/Event (NA if not available)
- `Ciudad` - City (NA if not available)
- `Lugar` - Location/Country (NA if not available)
- `Formato` - Format (Online/In person, detected from description)
- `Fecha` - Date (converted to "Month Year" format)
- `anio` - Year
- `Tipo` - Type (Talk, Event Organization, Hackathon, Other)
- `Cantidad` - Quantity (NA if not available)
- `Rol` - Role (Speaker, Organizer, Participant)
- `Links` - URL

### publications.csv
Contains the following columns matching PublicacionesPorAnioYanina-2025.csv format:
- `Title` - Publication title
- `Year` - Publication year
- `Type_Long` - Long type description (Blog Post, Article, Video/Podcast, Open Source Project)
- `Type` - Short type (Blog, Article, Multimedia, Software)
- `Link` - URL
- `En_mi_web` - Empty field to be filled manually if needed

## Type Mapping

### Events
Contribution types mapped to events:
- `SPEAKING` → Talk (Speaker)
- `EVENT_ORGANIZATION` → Event Organization (Organizer)
- `HACKATHON` → Hackathon (Participant)
- `OTHER` → Other

### Publications
Contribution types mapped to publications:
- `BLOGPOST` → Blog Post (Blog)
- `ARTICLE_PUBLICATION` → Article (Article)
- `VIDEO_PODCAST` → Video/Podcast (Multimedia)
- `OPEN_SOURCE_PROJECT` → Open Source Project (Software)

## Notes

- Fields marked as NA indicate that the information is not available in the contributions-github.csv file
- The comparison is based on matching titles (case-insensitive) and years
- The `Formato` field attempts to detect "Online" events based on keywords in the description
- All other fields should be filled manually as needed
