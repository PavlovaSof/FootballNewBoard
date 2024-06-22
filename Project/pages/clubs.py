from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv('DataFoot.csv', sep=',')

all_clubs = df['Club'].unique()

layout = dbc.Container([
    html.Div([
        html.P(
            "Показатели футболистов в своих клубах. "
            " Используйте фильтры, чтобы увидеть результат."
            )
        ], style = {
            'backgroundColor': 'rgb(21, 71, 130)',
            'padding': '10px 5px'
        }),
          html.Div([
            html.Div([
                html.Label('Выберите клуб: '),
                dcc.Dropdown(
                    id = 'crossfilter-clubs',
                    options = [{'label': j, 'value': j} for j in all_clubs],
                    # значение клуба, выбранное по умолчанию
                    value = ['BAR'],
                    # без возможности множественного выбора
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
                ],
                id = 'crossfilter-indic',
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
                id = 'crossfilter-yearss',
                min = df['Year'].min(),
                max = df['Year'].max(),
                value = 2016,
                step = None,
                marks = {str(year):
                    str(year) for year in df['Year'].unique()}
                ),
            style = {'width': '95%', 'padding': '0px 20px 20px 20px'}
        ),
        html.Div(
            dcc.Graph(id = 'pie'),
            style = {'width': '100%', 'display': 'inline-block'}
        ),
        html.Div(
        dcc.Graph(id='bar'),
        style={'width': '100%', 'display': 'inline-block'}
    ),
])


@callback(
    Output('bar', 'figure', allow_duplicate=True),
    [Input('crossfilter-clubs', 'value'),
    Input('crossfilter-indic', 'value'),
    Input('crossfilter-yearss', 'value')],
    prevent_initial_call=True
)
def update_stacked_area(club, indication, year):
    filtered_data = df[(df['Year'] <= year) & (df['Club'] == club)]
    figure = px.bar(
        filtered_data,
        x='Year',
        y=indication,
        color='Club'
    )
    return figure

@callback(
    Output('pie', 'figure', allow_duplicate=True),
    [Input('crossfilter-clubs', 'value'),
    Input('crossfilter-indic', 'value'),
    Input('crossfilter-yearss', 'value')],
    prevent_initial_call=True
)

def update_pie(club, indication, year):
    filtered_data = df[(df['Year'] <= year) & (df['Club'] == club)]
    figure = px.pie(filtered_data, values=indication,
             names="Player Names", 
             color_discrete_sequence=px.colors.sequential.Rainbow)
    
    return figure


