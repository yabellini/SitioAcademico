#!/usr/bin/env Rscript

# Script to compare contributions-github.csv with EventosPorAnioYanina-2025.csv 
# and PublicacionesPorAnioYanina-2025.csv
# Author: Generated for Yanina Bellini Saibene
# Date: 2025-12-21

# Read the CSV files
cat("Reading CSV files...\n")
contributions <- read.csv("datos/contributions-github.csv", stringsAsFactors = FALSE)
eventos_existing <- read.csv("datos/EventosPorAnioYanina-2025.csv", stringsAsFactors = FALSE)
publicaciones_existing <- read.csv("datos/PublicacionesPorAnioYanina-2025.csv", stringsAsFactors = FALSE)

cat(sprintf("Loaded %d contributions from GitHub\n", nrow(contributions)))
cat(sprintf("Loaded %d existing events\n", nrow(eventos_existing)))
cat(sprintf("Loaded %d existing publications\n", nrow(publicaciones_existing)))

# Define which contribution types correspond to events vs publications
event_types <- c("SPEAKING", "EVENT_ORGANIZATION", "HACKATHON", "OTHER")
publication_types <- c("BLOGPOST", "ARTICLE_PUBLICATION", "VIDEO_PODCAST", "OPEN_SOURCE_PROJECT")

# Filter contributions by type
contrib_events <- contributions[contributions$Type %in% event_types, ]
contrib_publications <- contributions[contributions$Type %in% publication_types, ]

cat(sprintf("\nFound %d event-type contributions\n", nrow(contrib_events)))
cat(sprintf("Found %d publication-type contributions\n", nrow(contrib_publications)))

# --- PROCESS EVENTS ---
cat("\n=== Processing Events ===\n")

# Create a comparison key for events
# We'll use Title and year from the Date field for matching
contrib_events$year <- as.integer(format(as.Date(contrib_events$Date), "%Y"))
contrib_events$title_clean <- tolower(trimws(contrib_events$Title))

eventos_existing$title_clean <- tolower(trimws(eventos_existing$Nombre))

# Find events in contributions that are NOT in existing events
# Match by title and year
# Create a matching key
contrib_events$match_key <- paste(contrib_events$title_clean, contrib_events$year, sep = "_")
eventos_existing$match_key <- paste(eventos_existing$title_clean, eventos_existing$anio, sep = "_")

# Find missing events
missing_events <- contrib_events[!contrib_events$match_key %in% eventos_existing$match_key, ]

cat(sprintf("Found %d events in contributions-github.csv not in EventosPorAnioYanina-2025.csv\n", 
            nrow(missing_events)))

# Transform missing events to match the EventosPorAnioYanina format
events_dataset <- data.frame(
  Nombre = missing_events$Title,
  Institucion.Evento = NA,  # Not available in contributions
  Ciudad = NA,              # Not available in contributions
  Lugar = NA,               # Not available in contributions
  Formato = ifelse(grepl("online|virtual", missing_events$Description, ignore.case = TRUE), "Online", NA),
  Fecha = format(as.Date(missing_events$Date), "%B %Y"),  # Convert to Month Year format
  anio = missing_events$year,
  Tipo = sapply(missing_events$Type, function(x) {
    switch(x,
      "SPEAKING" = "Talk",
      "EVENT_ORGANIZATION" = "Event Organization",
      "HACKATHON" = "Hackathon",
      "OTHER" = "Other",
      NA_character_
    )
  }),
  Cantidad = NA,  # Not available in contributions
  Rol = sapply(missing_events$Type, function(x) {
    switch(x,
      "SPEAKING" = "Speaker",
      "EVENT_ORGANIZATION" = "Organizer",
      "HACKATHON" = "Participant",
      "OTHER" = "Other",
      NA_character_
    )
  }),
  Links = missing_events$URL,
  stringsAsFactors = FALSE
)

# --- PROCESS PUBLICATIONS ---
cat("\n=== Processing Publications ===\n")

# Create a comparison key for publications
contrib_publications$year <- as.integer(format(as.Date(contrib_publications$Date), "%Y"))
contrib_publications$title_clean <- tolower(trimws(contrib_publications$Title))

publicaciones_existing$title_clean <- tolower(trimws(publicaciones_existing$Title))

# Find publications in contributions that are NOT in existing publications
# Create a matching key
contrib_publications$match_key <- paste(contrib_publications$title_clean, contrib_publications$year, sep = "_")
publicaciones_existing$match_key <- paste(publicaciones_existing$title_clean, publicaciones_existing$Year, sep = "_")

# Find missing publications
missing_publications <- contrib_publications[!contrib_publications$match_key %in% publicaciones_existing$match_key, ]

cat(sprintf("Found %d publications in contributions-github.csv not in PublicacionesPorAnioYanina-2025.csv\n", 
            nrow(missing_publications)))

# Transform missing publications to match the PublicacionesPorAnioYanina format
publications_dataset <- data.frame(
  Title = missing_publications$Title,
  Year = missing_publications$year,
  Type_Long = sapply(missing_publications$Type, function(x) {
    switch(x,
      "BLOGPOST" = "Blog Post",
      "ARTICLE_PUBLICATION" = "Article",
      "VIDEO_PODCAST" = "Video/Podcast",
      "OPEN_SOURCE_PROJECT" = "Open Source Project",
      NA_character_
    )
  }),
  Type = sapply(missing_publications$Type, function(x) {
    switch(x,
      "BLOGPOST" = "Blog",
      "ARTICLE_PUBLICATION" = "Article",
      "VIDEO_PODCAST" = "Multimedia",
      "OPEN_SOURCE_PROJECT" = "Software",
      NA_character_
    )
  }),
  Link = missing_publications$URL,
  En_mi_web = "",  # Empty by default, to be filled manually if needed
  stringsAsFactors = FALSE
)

# --- SAVE RESULTS ---
cat("\n=== Saving Results ===\n")

# Save the events dataset
write.csv(events_dataset, "datos/events.csv", row.names = FALSE, na = "")
cat(sprintf("Saved %d missing events to datos/events.csv\n", nrow(events_dataset)))

# Save the publications dataset
write.csv(publications_dataset, "datos/publications.csv", row.names = FALSE, na = "")
cat(sprintf("Saved %d missing publications to datos/publications.csv\n", nrow(publications_dataset)))

# --- SUMMARY ---
cat("\n=== Summary ===\n")
cat(sprintf("Events in contributions-github.csv: %d\n", nrow(contrib_events)))
cat(sprintf("Events already in EventosPorAnioYanina-2025.csv: %d\n", 
            nrow(contrib_events) - nrow(missing_events)))
cat(sprintf("Missing events (saved to events.csv): %d\n", nrow(events_dataset)))
cat("\n")
cat(sprintf("Publications in contributions-github.csv: %d\n", nrow(contrib_publications)))
cat(sprintf("Publications already in PublicacionesPorAnioYanina-2025.csv: %d\n", 
            nrow(contrib_publications) - nrow(missing_publications)))
cat(sprintf("Missing publications (saved to publications.csv): %d\n", nrow(publications_dataset)))

cat("\nDone!\n")
