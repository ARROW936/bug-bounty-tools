# Thu   17 Apr 2025
# 8:30 AM
# v 1
  
"""Extract scope from `csv` file."""

import csv
import glob

def save(scope):
    """Save scope in files"""
    for key, values in scope.items():
        with open(f'Scope/{key}s.txt', 'w') as file:
            for value in values:
                file.write(value + '\n')
        file.close()

def get_types(csv_file):
    """Get types of assets"""
    types = set()

    with open(csv_file, 'r') as cfile:
        reader = csv.DictReader(cfile)
        for row in reader:
            types.add(row['asset_type'])

    return types


def extract_scope(csv_file):
    """Read data from csv file and  return scope."""
    # Get asset types
    asset_types = get_types(csv_file)
    # Create empty dictionary
    scope = {}.fromkeys(asset_types)
    for k in scope.keys():
        scope[k] = []
    
    with open(csv_file, 'r') as cfile:
        reader = csv.DictReader(cfile)
        for row in reader:
            for asset_type in asset_types:
                if asset_type == row['asset_type']:
                    scope[asset_type].append(row['identifier'])

    return scope

# Find scope files in the directory
csv_files = glob.glob('Configurations/scopes*.csv')

# Cheeck for files
if not csv_files:
    print("No files found")
else:
    for csv_file in csv_files:
        scope = extract_scope(csv_file)
        save(scope)