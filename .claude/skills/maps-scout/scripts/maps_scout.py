import os
import csv
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Maps Scout: Log facilities found via map scouting.")
    parser.add_argument("--name", required=True, help="Name of the building or facility.")
    parser.add_argument("--address", required=True, help="Physical address.")
    parser.add_argument("--type", required=True, help="Facility type (e.g., 'Medical Office').")
    
    args = parser.parse_args()

    data_dir = os.path.join(os.getcwd(), ".tmp")
    output_file = os.path.join(data_dir, "maps_leads.csv")
    file_exists = os.path.isfile(output_file)

    try:
        with open(output_file, mode='a', newline='', encoding='utf-8') as f:
            fieldnames = ["name", "address", "type"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "name": args.name,
                "address": args.address,
                "type": args.type
            })
        print(f"SUCCESS: Facility '{args.name}' logged to {output_file}")
        sys.exit(0)
    except Exception as e:
        print(f"ERROR: Failed to log facility: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
