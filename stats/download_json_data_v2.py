"""Uses another API to get COVID-19 data, and saves it to a csv file."""
import csv
from datetime import datetime
from operator import itemgetter

import requests

earliest_date = datetime.strptime('2020-03-01', '%Y-%m-%d')
latest_date = datetime.strptime('2020-04-20', '%Y-%m-%d')

url = 'https://thevirustracker.com/timeline/map-data.json'
r = requests.get(url)
response = r.json()
data = response['data']

# Extract the information
days_dict = {}  # Key is date, value is another dictionary of data
for row in data:
    # This API sends each day of each country in a separate row
    date = datetime.strptime(row['date'], "%m/%d/%y")
    if date < earliest_date or date > latest_date:
        continue

    # If this day's dictionary already exists, add these numbers to its
    if date in days_dict.keys():
        day_dict = days_dict[date]
        day_dict['Infections'] += int(row['cases'])
        day_dict['Deaths'] += int(row['deaths'])
        day_dict['Recoveries'] += int(row['recovered'])
    else:
        # Create this day's dictionary
        day_dict = {
            'Infections': int(row['cases']),
            'Deaths': int(row['deaths']),
            'Recoveries': int(row['recovered']),
        }
        # Add to the dict list
        days_dict[date] = day_dict

# Convert to a format that can be made into a csv
days = []
# Use of dict.items() from https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp
for date, day_data in days_dict.items():
    day_dict = {
        'Date': date.strftime('%Y-%m-%d'),
        'Infections': day_data['Infections'],
        'Deaths': day_data['Deaths'],
        'Recoveries': day_data['Recoveries'],
    }
    days.append(day_dict)

# Make sure days are in order
days.sort(key=itemgetter('Date'))

# Write csv file
out_path = 'data/covid19_from_json_v2.csv'
with open(out_path, 'w', newline='') as f:
    field_names = ['Date', 'Infections', 'Deaths', 'Recoveries']
    writer = csv.DictWriter(f, fieldnames=field_names)
    # Write to the file
    writer.writeheader()
    writer.writerows(days)


"""
print(f"Infections: {day_dict['Infections']}")
print(f"Deaths: {day_dict['Deaths']}")
print(f"Recoveries: {day_dict['Recoveries']}")
"""