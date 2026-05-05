---
name: maps-scout
description: "Scans Google Maps for high-value commercial buildings (medical offices, industrial parks, professional buildings). Trigger when user wants to: (1) Find local businesses on a map, (2) List medical facilities in an area, (3) Scout industrial zones for cleaning leads."
---

# Maps Scout

This skill leverages Google Maps (or map-based search) to identify physical buildings and facilities that are high-value targets for commercial cleaning.

## Core Workflow

1. **Target Area**: Define the geographic bounds (e.g., zip code, city).
2. **Search Categories**: Focus on high-frequency cleaning needs:
   - Medical Offices / Clinics
   - Dental Offices
   - Law Firms / Professional Suites
   - Industrial Parks
3. **Data Extraction**: Collect building name, address, and facility type.
4. **Logging**: Use `maps_scout.py` to save findings.

## Rules

- Prioritize medical and dental facilities as they have higher cleaning standards and frequency.
- Group leads by office park or building to enable efficient site visits.

## Scripts

- `scripts/maps_scout.py` — Logs map-based leads to the project database.

## References

- `file:///c:/Users/ASUS/Documents/trae_projects/Kents%20new%20project%20in%20trae/workflows/maps_scout_sop.md` — The original SOP for map scouting.
