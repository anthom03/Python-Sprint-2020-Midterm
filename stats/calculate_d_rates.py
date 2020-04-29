"""Calculates two types of death rates for each day and adds them to the csv file."""
# Source for csv class usage: https://docs.python.org/2/library/csv.html
import csv
from datetime import datetime

csv_source_file = 'data/covid19.csv'
dicts = []
with open(csv_source_file) as f:
    reader = csv.DictReader(f)

    for row in reader:
        # Set the values of day_dict
        day_dict = {
            'Date': row['Date'],
            'Infections': row['Infections'],
            'Deaths': row['Deaths'],
            'Recoveries': row['Recoveries'],
        }
        # Parse the numerical values
        infections = int(row['Infections'])
        deaths = int(row['Deaths'])
        recoveries = int(row['Recoveries'])

        # Calculate the death rates, and add them to the dict
        d_rate1 = deaths / infections
        d_rate2 = deaths / recoveries
        print(f"infections: {infections}")
        print(f"deaths: {deaths}")
        print(f"recoveries: {recoveries}")
        print(f"d_rate1: {d_rate1}")
        print(f"d_rate2: {d_rate2}")
        day_dict['d_rate1'] = d_rate1
        day_dict['d_rate2'] = d_rate2

        dicts.append(day_dict)

# Write these dictionaries to a new csv file
csv_write_file = 'data/covid19_d_rates.csv'
with open(csv_write_file, 'w', newline='') as f:
    fieldnames = ['Date', 'Infections', 'Deaths', 'Recoveries', 'd_rate1', 'd_rate2']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dicts)
