# Python Spring Project | COVID-19 Numbers
## Going through the Midterm
### Creating _covid19.csv_
Downloaded data in _countries-aggregated.csv_ from https://github.com/datasets/covid-19,
and used _csv_data_cleaner.py_ to convert the data to the desired format for _covid19.csv_.
### Including the death rates
Run _calculate_d_rates.py_ to compute the death rates.
### Plotting a graph
Run either _plot.py_ or _plot_d_rates.py_ to generate a plot.
### Getting data from an API
Use _download_json_data_v2.py_ to download COVID-19 data from an API and save it in _covid19_from_json_v2.csv_.
The similarly named _download_json_data.py_ is inferior as its API call does not return any recovery numbers at this time.
Again, calculate death rates using _calculate_d_rates.py_ and plot the graph using either _plot.py_ or _plot_d_rates.py_.
## Python Files
### _csv_data_cleaner.py_
Takes data from _countries-aggregated.csv_ and records only the US data from 2020-03-01 to 2020-04-20.
Saves that data to _covid19.csv_
### _plot.py_
Plots Infections, Deaths, and Recoveries over time from _covid19.csv_ using _plotly_.
### _calculate_d_rates.py_
Calculates two types of death rates for each day.
Adds the death rates to the data from _covid19.csv_ and saves it in _covid19_d_rates.csv_
### _plot_d_rates.py_
Plots the death rates over time.  
d_rate1 is the number of deaths divided by infections.  
d_rate2 is the number of deaths divided by recoveries.
### _download_json_data.py_
Downloads COVID-19 data from an API in JSON format and saves it to a csv file.  
WARNING: API currently returns no recovery numbers!  
API URL: https://covid19.mathdro.id/api/daily
### _download_json_data_v2.py_
Just like _download_json_data.py_, but uses a different API. The API returns data for each country, but we add all the values to find the worldwide numbers.  
This API does return recovery numbers.  
API URL: https://thevirustracker.com/timeline/map-data.json
## Data Files
### _countries-aggregated.csv_
Raw data downloaded from https://github.com/datasets/covid-19
### _covid19.csv_
Only includes US cases from 2020-03-01 to 2020-04-20.  
Created by _csv_data_cleaner.py_
### _covid19_d_rates.csv_
Contains the same data as _covid19.csv_ with the addition of the death rates.  
Created by _calculate_d_rates.py_
### _covid19_from_json.csv_
Same columns as _covid19.csv_, but downloaded from an API.  
Created by _download_json_data.py_
### _covid19_from_json_d_rates.csv_
Contains the same data as _covid19_from_json.csv_ with the addition of the death rates.  
Created by _calculate_d_rates.py_
### _covid19_from_json_v2.csv_
Same columns as _covid19_from_json.csv_, but from a different API.  
Created by _download_json_data_v2.py_