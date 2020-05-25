"""Plots the death rates over time."""
import csv
from datetime import datetime

# Used https://plotly.com/python/line-charts/ for how to set up and style the plotly graph
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import offline
import os

# Where to save the html file
# Source: https://stackoverflow.com/questions/918154/relative-paths-in-python
project_path = os.path.realpath('..')
filename = os.path.join(project_path, "web_app", "templates", "web_app", "graph_d_rates.html")

# Explain d_rate1 and d_rate2
print("d_rate1 is the number of deaths divided by infections")
print("d_rate2 is the number of deaths divided by recoveries")

# Load the data from the csv file
data_file_path = 'data/covid19_d_rates.csv'
dates, d_rate1s, d_rate2s = [], [], []
with open(data_file_path) as f:
    reader = csv.DictReader(f)

    for row in reader:
        date = datetime.strptime(row['Date'], '%Y-%m-%d')
        dates.append(date)
        try:
            d_rate1s.append(float(row['d_rate1']))
        except ValueError:
            d_rate1s.append(None)
        try:
            d_rate2s.append(float(row['d_rate2']))
        except ValueError:
            d_rate2s.append(None)

# Create the chart

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(
    go.Scatter(x=dates, y=d_rate1s, name='d_rate1', mode='lines+markers'),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(x=dates, y=d_rate2s, name='d_rate2', mode='lines+markers'),
    secondary_y=True
)

fig.update_layout(title='COVID-19 Death Rates',
                  title_font=dict(size=28),
                  font=dict(size=18))
fig.update_xaxes(title_text='Date',
                 title_font=dict(size=22),
                 tickfont=dict(size=16))
fig.update_yaxes(title_text='d_rate1 Scale',
                 title_font=dict(size=22),
                 tickfont=dict(size=16),
                 secondary_y=False)
fig.update_yaxes(title_text='d_rate2 Scale',
                 title_font=dict(size=22),
                 tickfont=dict(size=16),
                 secondary_y=True)

offline.plot(fig, filename=filename)
