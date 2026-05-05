# 🏗️ WAT Framework: Commercial Cleaning Lead Gen

## 🌊 Workflows (SOPs)
1. **[Trigger Scout SOP](workflows/trigger_scout_sop.md)**: Finding companies in a "State of Change" (New leases, relocations).
2. **[Maps Scout SOP](workflows/maps_scout_sop.md)**: Finding high-value local buildings and medical offices.
3. **[Qualification SOP](workflows/lead_qualification_sop.md)**: Deep research into facility type and profitability.

## 🤖 Agents
- **Lead Detective (Trigger)**: Finds companies moving, expanding, or signing new leases.
- **Maps Scout**: Scans Google Maps for medical/professional buildings.
- **Lead Enricher**: Finds specific decision-maker names and contact info for all leads.
- **Lead Profiler**: Conducts deep research to qualify leads for profitability.

## 🛠️ Tools
- `tools/lead_detective.py`: The Trigger-based search script.
- `tools/maps_scout.py`: The Google Maps scanning script.
- `tools/enrich_leads.py`: The unified enrichment script for all sources.
- `tools/lead_profiler.py`: The qualification script.

## 📁 Data
- `.tmp/trigger_leads.csv`: Raw news/lease trigger data.
- `.tmp/maps_leads.csv`: Raw building data from Maps.
- `.tmp/manassas_leads_enriched.csv`: Unified contact data (Gold List).
- `.tmp/manassas_leads_qualified.csv`: Profitability analysis.
