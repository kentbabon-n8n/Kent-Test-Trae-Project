---
name: lead-detective
description: "Finds companies in a 'State of Change' (new leases, relocations, expansions) for commercial cleaning lead generation. Trigger when user wants to: (1) Find companies moving, (2) Scout for new lease announcements, (3) Search for local business expansions."
---

# Lead Detective

This skill identifies high-potential commercial cleaning leads by searching for companies undergoing significant changes that often trigger the need for new cleaning services.

## Core Workflow

1. **Identify Triggers**: Search for keywords like "new lease", "relocation", "opening soon", "expansion", "new headquarters" in local news or business journals.
2. **Extract Data**: Capture company name, new address, and the nature of the change.
3. **Log Lead**: Use the `lead_detective.py` script to save the findings to the project's lead database.

## Rules

- Prioritize business-to-business (B2B) relocations.
- Focus on the target geographic area (default: Manassas/Northern Virginia).
- If a lead is vague (no specific company or address), mark for further research or skip.

## Scripts

- `scripts/lead_detective.py` — Logs a found lead to the central CSV file.

## References

- `references/trigger-keywords.md` — List of high-intent search queries and keywords.
- `file:///c:/Users/ASUS/Documents/trae_projects/Kents%20new%20project%20in%20trae/workflows/trigger_scout_sop.md` — The original SOP for this workflow.
