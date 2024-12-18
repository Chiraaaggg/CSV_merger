import os
import pandas as pd
from datetime import datetime

def merge_csv_files(input_dir, output_csv, convert_to_excel=False):
    try:
        # List all CSV files in the input directory
        csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
        
        if not csv_files:
            print("No CSV files found in the directory.")
            return

        print(f"Found {len(csv_files)} CSV files. Merging them...")

        # Read and merge all CSV files
        merged_df = pd.concat([pd.read_csv(os.path.join(input_dir, file)) for file in csv_files], ignore_index=True)
        merged_df.to_csv(output_csv, index=False)
        print(f"Merged CSV saved as: {output_csv}")

        # Convert to Excel if requested
        if convert_to_excel:
            output_excel = output_csv.replace('.csv', '.xlsx')
            merged_df.to_excel(output_excel, index=False, engine='openpyxl')
            print(f"Merged Excel saved as: {output_excel}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("CSV Merger Tool")
    input_dir = input("Enter the directory containing the CSV files: ").strip()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_csv = f"merged_{timestamp}.csv"
    
    # Ask if user wants Excel conversion
    convert_choice = input("Do you want to convert the merged file to Excel format? (yes/no): ").strip().lower()
    convert_to_excel = convert_choice in ["yes", "y"]
    
    merge_csv_files(input_dir, output_csv, convert_to_excel)
