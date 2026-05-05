import os
import csv
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Lead Detective: Log found leads from triggers.")
    parser.add_argument("--company", required=True, help="Name of the company found.")
    parser.add_argument("--location", required=True, help="Address or location of the company.")
    parser.add_argument("--trigger", required=True, help="The event that triggered the lead (e.g., 'New Lease').")
    parser.add_argument("--source", help="Source of the information (e.g., 'Manassas Journal').")
    
    args = parser.parse_args()

    data_dir = os.path.join(os.getcwd(), ".tmp")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    output_file = os.path.join(data_dir, "trigger_leads.csv")
    file_exists = os.path.isfile(output_file)

    try:
        with open(output_file, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["company", "location", "trigger", "source"])
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "company": args.company,
                "location": args.location,
                "trigger": args.trigger,
                "source": args.source if args.source else "Manual"
            })
        print(f"SUCCESS: Lead for '{args.company}' logged to {output_file}")
        sys.exit(0)
    except Exception as e:
        print(f"ERROR: Failed to log lead: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
