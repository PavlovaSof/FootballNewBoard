import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv('DataFoot.csv', sep=',')

all_countries = df["Country"].unique()

layout = dbc.Container([
    html.Div([
        html.P(
            "Страничка с показателями по футболисту. Используйте фильтры, чтобы увидеть результат"
            )
        ], style = {
            'backgroundColor': 'rgb(21, 71, 130)',
            'padding': '10px 5px'
        }),
          html.Div([
            html.Div([
                html.Label('Страны'),
                dcc.Dropdown(
                    id = 'crossfilter-country',
                    options = [{'label': i, 'value': i} for i in all_countries],
                    # значение страны, выбранное по умолчанию
                    value = ['Spain'],
                    # отсутствие возможности множественного выбора
                    multi = False
                )
            ],
            style = {'width': '48%', 'display': 'inline-block'}),
       
            html.Div([
                html.Label('Основные показатели'),
                dcc.RadioItems(
                options = [
                    {'label':'Забитые голы', 'value': 'Goals'},
                    {'label':'Сыгранные матчи', 'value': 'Matches_Played'},
                    {'label':'Время игр', 'value': 'Mins'},
                    {'label':'Перспективность', 'value': 'xG'},
                ],
                id = 'crossfilter-index',
                value = 'Goals',
                labelStyle={'display': 'inline-block'}
                )
            ],
            style = {'width': '48%',  'float': 'right', 'display': 'inline-block'}),
        ], style = {
            'borderBottom': 'thin lightgrey solid',
            'backgroundColor': 'rgb(21, 71, 130)',
            'padding': '10px 5px'
        }),
          html.Div(
            dcc.Slider(
                id = 'crossfilter-years',
                min = df['Year'].min(),
                max = df['Year'].max(),
                value = 2020,
                step = None,
                marks = {str(year):
                    str(year) for year in df['Year'].unique()}
                ),
            style = {'width': '95%', 'padding': '0px 20px 20px 20px'}
        ),
       


    html.Div(
            dcc.Graph(id = 'line'),
            style = {'width': '100%', 'display': 'inline-block'}
        ),
    
     
])



@callback(
    Output('line', 'figure',allow_duplicate=True),
    [Input('crossfilter-country', 'value'),
    Input('crossfilter-index', 'value'),
    Input('crossfilter-years', 'value')],
    prevent_initial_call=True
)

def update_scatter(country, indication, year):
    filtered_data = df[(df['Year'] <= year) & (df['Country'] == country)]
    figure = px.line(
        filtered_data,
        x = "Year",
        y = indication,
        color = "Player Names",
        title = "Значения показателей по игрокам",
        markers = True,
    )
    return figure


