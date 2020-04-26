# Python Spring Project | COVID-19 Numbers
## Python Files
### _csv_data_cleaner.py_
Takes data from _countries-aggregated.csv_ and records only the US data from 2020-03-01 to 2020-04-20.
Saves that data to _covid19.csv_
### _plot.py_
Plots Infections, Deaths, and Recoveries over time from _covid19.csv_ using _plotly_.
## Data Files
### _countries-aggregated.csv_
Raw data downloaded from https://github.com/datasets/covid-19
### _covid19.csv_
Only includes US cases from 2020-03-01 to 2020-04-20.
Produced by _csv_data_cleaner.py_