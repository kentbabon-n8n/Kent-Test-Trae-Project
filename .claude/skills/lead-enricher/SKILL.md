---
name: lead-enricher
description: "Finds decision-maker names and contact information for leads. Trigger when user wants to: (1) Find who is in charge of a facility, (2) Get email/phone for a lead, (3) Research company personnel."
---

# Lead Enricher

This skill specializes in finding the right person to contact at a target company and gathering their contact details.

## Core Workflow

1. **Target Identification**: Take a company name and address.
2. **Personnel Search**: Search for:
   - Facility Manager
   - Property Manager
   - Operations Manager
   - Office Manager (for smaller offices)
3. **Contact Info**: Use LinkedIn, company websites, or public records to find email addresses and phone numbers.
4. **Logging**: Use `enrich_leads.py` to update the lead record.

## Rules

- **Efficiency First**: If no specific name is found, mark as "Check LinkedIn later" or "Skip" to maintain momentum.
- Prioritize leads with clear business-person associations.
- Verify contact info whenever possible.

## Scripts

- `scripts/enrich_leads.py` — Updates lead records with contact information.

## References

- `file:///c:/Users/ASUS/Documents/trae_projects/Kents%20new%20project%20in%20trae/.trae/project_rules.md` — Contains core filtering rules.
