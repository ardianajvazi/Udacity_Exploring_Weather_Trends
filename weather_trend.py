# Import libraries we are using.
import plotly.plotly as py # using to draw our graph online
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

# Assign the data with our CSV file to a variable called data.
dataCities = pd.read_csv('city_results.csv')
dataGlobal = pd.read_csv('Global_results.csv')

Seattle = dataCities[(dataCities.city=='Seattle')]
NewYork = dataCities[(dataCities.city=='New York')]
Global = dataGlobal


trace1 = go.Scatter(
    x=Global['year'],
    y=Global['global_avg_temp'],
    mode='lines',
    name='Global_Avg_Temp'
)
trace2 = go.Scatter(
    x=Seattle['year'],
    y=Seattle['city_avg_temp'],
    mode='lines',
    name='Seattle_Avg_Temp'
)
trace3 = go.Scatter(
    x=NewYork['year'],
    y=NewYork['city_avg_temp'],
    mode='lines',
    name='NewYork_Avg_Temp'
)

layout = go.Layout(
    title='Exploring Weather Trends',
        xaxis=dict(
            title='Year'
        ),
        yaxis=dict(
            title='Temperature in ( C )'
        )
    )

fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

# Plot data in the notebook
py.plot(fig, filename='Exploring Weather Trends')
