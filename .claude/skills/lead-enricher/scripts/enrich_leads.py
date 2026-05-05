import os
import csv
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Lead Enricher: Add contact info to leads.")
    parser.add_argument("--company", required=True, help="Name of the company.")
    parser.add_argument("--contact", required=True, help="Name of the decision maker.")
    parser.add_argument("--title", help="Title of the contact (e.g., 'Facility Manager').")
    parser.add_argument("--email", help="Email address.")
    parser.add_argument("--phone", help="Phone number.")
    
    args = parser.parse_args()

    data_dir = os.path.join(os.getcwd(), ".tmp")
    output_file = os.path.join(data_dir, "manassas_leads_enriched.csv")
    file_exists = os.path.isfile(output_file)

    try:
        with open(output_file, mode='a', newline='', encoding='utf-8') as f:
            fieldnames = ["company", "contact", "title", "email", "phone"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "company": args.company,
                "contact": args.contact,
                "title": args.title if args.title else "Unknown",
                "email": args.email if args.email else "N/A",
                "phone": args.phone if args.phone else "N/A"
            })
        print(f"SUCCESS: Enriched data for '{args.company}' logged to {output_file}")
        sys.exit(0)
    except Exception as e:
        print(f"ERROR: Failed to enrich lead: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
