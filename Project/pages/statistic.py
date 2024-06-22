from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv('DataFoot.csv', sep=',')

all_countries = df['Country'].unique()

layout = dbc.Container([
    html.Div([
        html.P(
            "Анализ основных показателей футболистов с 2016 по 2020 годы."
            " Используйте фильтры, чтобы увидеть результат."
            )
        ], style = {
            'backgroundColor': 'rgb(0,70,128)',
            'padding': '10px 5px'
        }),
          html.Div([
            html.Div([
                html.Label('Выберите страну: '),
                dcc.Dropdown(
                    id = 'crossfilter-count',
                    options = [{'label': i, 'value': i} for i in all_countries],
                    # значение страны, выбранное по умолчанию
                    value = ['Spain'],
                    # возможность множественного выбора
                    multi = True
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
                id = 'crossfilter-ind',
                value = 'Goals',
                labelStyle={'display': 'inline-block'}
                )
            ],
            style = {'width': '48%',  'float': 'right', 'display': 'inline-block'}),
        ], style = {
            'borderBottom': 'thin lightgrey solid',
            'backgroundColor': 'rgb(0,70,128)',
            'padding': '10px 5px'
        }),
          html.Div(
            dcc.Slider(
                id = 'crossfilter-year',
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
            dcc.Graph(id = 'bar'),
            style = {'width': '100%', 'display': 'inline-block'}
        ),
       

        html.Div(
            dcc.Graph(id = 'choropleth'),
            style = {'width': '100%', 'display': 'inline-block'}
        ),

])


@callback(
    Output('bar', 'figure',allow_duplicate=True),
    [Input('crossfilter-count', 'value'),
    Input('crossfilter-ind', 'value'),
    Input('crossfilter-year', 'value')],
    prevent_initial_call=True

)

def update_stacked_area(countries, indication, year):
    if not countries:
        return px.bar(title="Нет данных для отображения")
    
    filtered_data = df[(df['Year'] <= year) & (df['Country'].isin(countries))]
    if filtered_data.empty:
        return px.bar(title="Нет данных для отображения")
    
    figure = px.bar(
        filtered_data,
        x='Year',
        y=indication,
        color='Player Names'
    )
    return figure



@callback(
    Output('choropleth', 'figure'),
    Input('crossfilter-ind', 'value')
)
def update_choropleth(indication):
    figure = px.choropleth(
        df,
        locations='Country',
        locationmode = 'country names',
        color=indication,
        hover_name='Country',
        hover_data = {'Country':True,'Year':True,
                    'Goals':True,'Matches_Played':True,
                    'xG':True},
        labels={'Country':'Страна', 'Year':'Год',
                'Goals':'Голы', 'Matches_Played':'Сыграно матчей',
                'xG':'Перспективность'},
        color_continuous_scale=px.colors.sequential.BuPu,
        animation_frame='Year',
        )
   
    figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                        showlegend=False)
    return figure

