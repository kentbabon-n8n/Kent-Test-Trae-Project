import os
import csv
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Lead Profiler: Qualify leads based on size and profitability.")
    parser.add_argument("--company", required=True, help="Name of the company.")
    parser.add_argument("--sqft", type=int, required=True, help="Estimated square footage.")
    parser.add_argument("--frequency", required=True, help="Estimated cleaning frequency (e.g., '3x/week').")
    parser.add_argument("--value", type=float, help="Estimated monthly contract value.")
    
    args = parser.parse_args()

    data_dir = os.path.join(os.getcwd(), ".tmp")
    output_file = os.path.join(data_dir, "manassas_leads_qualified.csv")
    file_exists = os.path.isfile(output_file)

    # Simple qualification logic
    status = "Qualified" if args.sqft >= 5000 else "Small Account"

    try:
        with open(output_file, mode='a', newline='', encoding='utf-8') as f:
            fieldnames = ["company", "sqft", "frequency", "value", "status"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "company": args.company,
                "sqft": args.sqft,
                "frequency": args.frequency,
                "value": args.value if args.value else 0.0,
                "status": status
            })
        print(f"SUCCESS: Qualification for '{args.company}' logged to {output_file} (Status: {status})")
        sys.exit(0)
    except Exception as e:
        print(f"ERROR: Failed to qualify lead: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
