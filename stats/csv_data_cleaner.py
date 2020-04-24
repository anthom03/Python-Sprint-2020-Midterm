"""Clean the csv source file to include only the rows we want."""
# Source for csv class usage: https://docs.python.org/2/library/csv.html
import csv
from datetime import datetime

earliest_date = datetime.strptime('2020-03-01', '%Y-%m-%d')
latest_date = datetime.strptime('2020-04-20', '%Y-%m-%d')
country = 'US'

in_path = 'data/countries-aggregated.csv'
daily_dicts = []
with open(in_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Get the date, and check if it is in range
        date = datetime.strptime(row['Date'], '%Y-%m-%d')
        if date < earliest_date or date > latest_date:
            continue
        # Check country
        if row['Country'] != country:
            continue
        # Make a dictionary for this day, and add it to the list
        day_dict = {
            'Date': row['Date'],
            'Infections': row['Confirmed'],
            'Deaths': row['Deaths'],
            'Recoveries': row['Recovered'],
        }
        daily_dicts.append(day_dict)


out_path = 'data/covid19.csv'
# Fix for preventing extra rows in output file:
# https://stackoverflow.com/questions/16271236/python-3-3-csv-writer-writes-extra-blank-rows
with open(out_path, 'w', newline='') as f:
    field_names = ['Date', 'Infections', 'Deaths', 'Recoveries']
    writer = csv.DictWriter(f, fieldnames=field_names)
    # Write to the file
    writer.writeheader()
    writer.writerows(daily_dicts)
