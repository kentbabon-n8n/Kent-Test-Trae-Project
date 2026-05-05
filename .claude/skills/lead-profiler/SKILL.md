---
name: lead-profiler
description: "Qualifies leads by researching facility size and profitability. Trigger when user wants to: (1) Evaluate a lead's potential, (2) Calculate cleaning frequency needs, (3) Estimate contract value."
---

# Lead Profiler

This skill performs deep research on qualified leads to determine their profitability and service requirements.

## Core Workflow

1. **Facility Research**: Use public records or satellite imagery to estimate the square footage of the facility.
2. **Usage Analysis**: Determine the type of facility (e.g., medical, office, retail) and its typical cleaning frequency requirements.
3. **Profitability Estimation**: Calculate potential contract value based on size and frequency.
4. **Logging**: Use `lead_profiler.py` to save the final qualification data.

## Rules

- Focus on facilities over 5,000 sq ft for maximum profitability.
- Medical facilities are high-priority due to recurring revenue and higher margins.

## Scripts

- `scripts/lead_profiler.py` — Logs qualification data to the database.

## References

- `file:///c:/Users/ASUS/Documents/trae_projects/Kents%20new%20project%20in%20trae/workflows/lead_qualification_sop.md` — The original SOP for qualification.
