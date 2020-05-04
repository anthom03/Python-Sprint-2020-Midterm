"""Downloads COVID-19 data from an API in JSON format and saves it to a csv file."""
import requests
from datetime import datetime
import csv

earliest_date = datetime.strptime('2020-03-01', '%Y-%m-%d')
latest_date = datetime.strptime('2020-04-20', '%Y-%m-%d')

url = "https://covid19.mathdro.id/api/daily"
r = requests.get(url)
response = r.json()

# Extract the data we want from the response
daily_dicts = []
for row in response:
    # Get the date, and check if it is in range
    date = datetime.strptime(row['reportDate'], '%Y-%m-%d')
    if date < earliest_date or date > latest_date:
        continue
    daily_dict = {
        'Date': row['reportDate'],
        'Infections': row['totalConfirmed'],
        'Deaths': row['deaths']['total'],
        'Recoveries': row['totalRecovered']
    }
    daily_dicts.append(daily_dict)

out_path = 'data/covid19_from_json.csv'
with open(out_path, 'w', newline='') as f:
    field_names = ['Date', 'Infections', 'Deaths', 'Recoveries']
    writer = csv.DictWriter(f, fieldnames=field_names)
    # Write to the file
    writer.writeheader()
    writer.writerows(daily_dicts)
