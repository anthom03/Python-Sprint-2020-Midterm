"""Create a plot showing the US infections, deaths, and recoveries over time."""
# Used https://plotly.com/python/line-charts/ for how to set up and style the plotly graph
import plotly.graph_objects as go
import csv
from datetime import datetime
from plotly import offline
import os

# Where to save the html file
# Source: https://stackoverflow.com/questions/918154/relative-paths-in-python
project_path = os.path.realpath('..')
filename = os.path.join(project_path, "web_app", "templates", "web_app", "graph.html")

# Load the data from the csv file
data_file_path = 'data/covid19.csv'
dates, infections, deaths, recoveries = [], [], [], []
with open(data_file_path) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Find the column indexes based on the headers
    i = 0
    date_index, infections_index, deaths_index, recoveries_index = -1, -1, -1, -1
    for header in header_row:
        if header == 'Date':
            date_index = i
        elif header == 'Infections':
            infections_index = i
        elif header == 'Deaths':
            deaths_index = i
        elif header == 'Recoveries':
            recoveries_index = i
        i += 1

    # print(f"Date: {date_index}, Infections: {infections_index}, "
    #       f"Deaths: {deaths_index}, Recoveries: {recoveries_index}")
    if date_index < 0 or infections_index < 0 or deaths_index < 0 or recoveries_index < 0:
        print("Indexing error!")
        exit(-1)

    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        dates.append(date)
        infections.append(int(row[infections_index]))
        deaths.append(int(row[deaths_index]))
        recoveries.append(int(row[recoveries_index]))

maximum = max(max(infections), max(deaths), max(recoveries))

# Create the chart

fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=infections, name='Infections', mode='lines+markers'))
fig.add_trace(go.Scatter(x=dates, y=deaths, name='Deaths', mode='lines+markers'))
fig.add_trace(go.Scatter(x=dates, y=recoveries, name='Recoveries', mode='lines+markers'))

fig.update_layout(title='COVID-19 Infections, Deaths, and Recoveries',
                  title_font=dict(size=28),
                  font=dict(size=18))
fig.update_xaxes(title_text='Date',
                 title_font=dict(size=22),
                 tickfont=dict(size=16))
fig.update_yaxes(title_text='Cumulative Totals',
                 title_font=dict(size=22),
                 tickfont=dict(size=16),
                 range=[0, maximum])

offline.plot(fig, filename=filename)
