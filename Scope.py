# Tue   15 Apr 2025
# 8:30 AM
  
"""Extract scopes from `csv` file."""

import csv
import glob

def extract_scope(csv_file):
    """Read data from csv file and  write it in scope file."""
    with open(csv_file, 'r') as cfile, open('scope.txt', 'w') as sfile:
        reader = csv.DictReader(cfile)
        for row in reader:
            if row['asset_type'] == 'URL':
                print(row['identifier'])
                sfile.write(row['identifier'] + '\n')

# Find scope files in the directory
csv_files = glob.glob('Configurations/scopes*.csv')

# Cheeck for files
if not csv_files:
    print("No files found")
else:
    for csv_file in csv_files:
        extract_scope(csv_file)

