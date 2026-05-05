# 🏗️ WAT Framework: Commercial Cleaning Lead Gen

## 🌊 Workflows (SOPs)
1. **[Trigger Scout SOP](workflows/trigger_scout_sop.md)**: Finding companies in a "State of Change" (New leases, relocations).
2. **[Maps Scout SOP](workflows/maps_scout_sop.md)**: Finding high-value local buildings and medical offices.
3. **[Qualification SOP](workflows/lead_qualification_sop.md)**: Deep research into facility type and profitability.

## 🤖 Agents (Skills)
- **[Lead Detective](.claude/skills/lead-detective/SKILL.md)**: Finds companies moving, expanding, or signing new leases.
- **[Maps Scout](.claude/skills/maps-scout/SKILL.md)**: Scans Google Maps for medical/professional buildings.
- **[Lead Enricher](.claude/skills/lead-enricher/SKILL.md)**: Finds specific decision-maker names and contact info for all leads.
- **[Lead Profiler](.claude/skills/lead-profiler/SKILL.md)**: Conducts deep research to qualify leads for profitability.

## 🛠️ Tools (Scripts)
- `.claude/skills/lead-detective/scripts/lead_detective.py`: The Trigger-based search script.
- `.claude/skills/maps-scout/scripts/maps_scout.py`: The Google Maps scanning script.
- `.claude/skills/lead-enricher/scripts/enrich_leads.py`: The unified enrichment script for all sources.
- `.claude/skills/lead-profiler/scripts/lead_profiler.py`: The qualification script.

## 📁 Data
- `.tmp/trigger_leads.csv`: Raw news/lease trigger data.
- `.tmp/maps_leads.csv`: Raw building data from Maps.
- `.tmp/manassas_leads_enriched.csv`: Unified contact data (Gold List).
- `.tmp/manassas_leads_qualified.csv`: Profitability analysis.
