# import dash_bootstrap_components as dbc
# from dash import html, dcc, callback, Output, Input, Dash
# import pandas as pd
# import plotly.express as px


# df = pd.read_csv('DataFoot.csv', sep=',')

# all_fclubs = df["Club"].unique()


# layout = dbc.Container([
#     dbc.Row ([
#         dbc.Col(
#                 html.Div([
#                 html.H3("Подробная информация о футболистах по клубам"),
#                 html.Hr(style={'color': 'black'}),
#             ], style={'textAlign': 'center'})
#         )
#     ]),

#     html.Br(),

#      dbc.Row ([
#         dbc.Col([
#             html.P("Выберите клуб:")
#         ],width=2),
#         dbc.Col([
#             dcc.Dropdown(
#                 id = 'crossfilter-fclubs',
#                 # заполняем дропдаун уникальными значениями клубов из датасета
#                 options = [{'label': i, 'value': i} for i in all_fclubs],
#                 # значение клуба, выбранное по умолчанию
#                 value = all_fclubs[0],
#                 # возможность множественного выбора
#                 multi = False
                
#             )
#         ],width=3),
#         dbc.Col([
#             html.P("Выберите футболиста:")
#         ],width=2),
#         dbc.Col([
#             dcc.Dropdown(
#                 id = 'crossfilter-fplayer',
#                 multi = False
#             )
#         ],width=3)
#     ]),

#     html.Br(),

#         dbc.Row ([
#             dbc.Col([
#                 dbc.Card([
#                     dbc.Row([
#                         dbc.CardHeader("Имя футболиста")
#                     ]),
#                     dbc.Row([
#                         dbc.Col([
#                             dbc.CardImg(src='/static/images/player.png')], width= 5),
#                         dbc.Col([
#                             dbc.CardBody(
#                                 html.P(
#                                 id='card_text1',
#                                 className="card-value"),
#                             )], width= 6),
#                         dbc.Col([
#                             html.P(' '),
#                         ], width=6, style={'padding': '15px 35px 15px 5px'}), 
#                     ])
#                 ], color = "primary", outline=True, style={'textAlign': 'center'}),
#             ],width=4),
#             dbc.Col([
#                 dbc.Card([
#                     dbc.Row([
#                         dbc.CardHeader("Клуб")
#                     ]),
#                     dbc.Row([
#                         dbc.Col([
#                             dbc.CardImg(src='/static/images/fclub.png')], width= 5),
#                         dbc.Col([
#                             dbc.CardBody(
#                                 html.P(
#                                 id='card_text2',
#                                 className="card-value"),
#                             )], width= 6),
#                         dbc.Col([
#                             html.P('(сокращенное наименование)'),
#                         ], width=6, style={'padding': '15px 35px 15px 5px'}),
#                     ])
#                 ], color = "primary", outline=True, style={'textAlign': 'center'}),
#             ],width=4),
#             dbc.Col([
#                 dbc.Card([
#                     dbc.Row([
#                         dbc.CardHeader("Забитые мячи")
#                     ]),
#                     dbc.Row([
#                         dbc.Col([
#                             dbc.CardImg(src='/static/images/goals.png')], width= 5),
#                         dbc.Col([
#                             dbc.CardBody(
#                                 html.P(
#                                 id='card_text3',
#                                 className="card-value"),
#                             )], width= 6),
#                         dbc.Col([
#                             html.P(' '),
#                         ], width=6, style={'padding': '15px 35px 15px 5px'}),
#                     ])
#                 ], color = "primary", outline=True, style={'textAlign': 'center'}),
#             ],width=4),
#             dbc.Col([
#                 dbc.Card([
#                     dbc.Row([
#                         dbc.CardHeader("Матчи")
#                     ]),
#                     dbc.Row([
#                         dbc.Col([
#                             dbc.CardImg(src='/static/images/fmatch.png')], width= 6),
#                         dbc.Col([
#                             dbc.CardBody(
#                                 html.P(
#                                 id='card_text4',
#                                 className="card-value"),
#                             )], width= 6),
#                         dbc.Col([
#                             html.P(' '),
#                         ], width=6, style={'padding': '15px 35px 15px 5px'}),
#                     ])
#                 ], color = "primary", outline=True, style={'textAlign': 'center'}),
#             ],width=4),
#             dbc.Col([
#                 html.Br(),
#                 dbc.Row([
#                     html.H5('Лучший игрок клуба'),
#                     html.Div(id = 'table1'),
#                 ],style = {'textAlign': 'center'})
#             ], width = 4)
#         ], style = {'textAlign': 'center'}),
# ]),


# @callback(
#     [Output('crossfilter-fplayer', 'options'),
#     Output('crossfilter-fplayer', 'value'),
#     ],
#     Input('crossfilter-fclubs', 'value')
# )
# def update_region(club):
#     all_fplayer=df[(df['Club'] == club)]['Player Names'].unique()
#     dd_fplayer = [{'label': i, 'value': i} for i in all_fplayer]
#     dd_fplayer_value = all_fplayer[0] 
#     return dd_fplayer, dd_fplayer_value
    


# @callback(
#     [Output('card_text1','children'),
#     Output('card_text2','children'),
#     Output('card_text3','children'),
#     Output('card_text4','children'),
#     Output('table1', 'children')],
#     [Input('crossfilter-fplayer', 'value'),
#     Input('crossfilter-fclubs', 'value')]
# )


# def update_card(player, club):
#     if not player:
#         return "Игрок не найден", "Нет данных", "0", "0", html.Div("Данные об игроке не найдены")

#     df_player=df[(df['Player Names'] == player)&(df['Year'] == 2019)]
#     df_player18=df[(df['Player Names'] == player)&(df['Year'] == 2018)]
#     xG_player=df[(df['Club'] == club)&(df['Year'] == 2019)].sort_values(by='xG', ascending=False)

#     if df_player.empty or df_player18.empty:
#         return "Игрок не найден", "Нет данных", "0", "0", html.Div("Данные об игроке не найдены") 

#     ct1=df_player.iloc[0]['Player Names']
#     ct2=df_player.iloc[0]['Club']
#     ct3=df_player.iloc[0]['Goals']
#     ct4=df_player.iloc[0]['Matches_Played']
#     xG19=df_player.iloc[0]['xG']
#     xG18=df_player18.iloc[0]['xG']
#     xG_table=xG_player.iloc[0:1][['Player Names','xG']]

#     if xG18 != 0:
#         delta_xG = round((xG19 - xG18) / xG18, 2) * 100
#     else:
#         delta_xG = 0


#     table = dbc.Table.from_dataframe(
#         xG_table, striped=True, bordered=True, hover=True, index=False)
   


#     return ct1, ct2, ct3, ct4, table


# import dash_bootstrap_components as dbc
# from dash import html, dcc, callback, Output, Input, Dash
# import pandas as pd
# import plotly.express as px

# # Загрузка и фильтрация данных
# df = pd.read_csv('DataFoot.csv', sep=',')
# df = df[(df['Year'] >= 2016) & (df['Year'] <= 2020)]

# all_fclubs = df["Club"].unique()

# layout = dbc.Container([
#     dbc.Row([
#         dbc.Col(
#             html.Div([
#                 html.H3("Подробная информация о футболистах по клубам"),
#                 html.Hr(style={'color': 'black'}),
#             ], style={'textAlign': 'center'})
#         )
#     ]),

#     html.Br(),

#     dbc.Row([
#         dbc.Col([
#             html.P("Выберите клуб:")
#         ], width=2),
#         dbc.Col([
#             dcc.Dropdown(
#                 id='crossfilter-fclubs',
#                 options=[{'label': i, 'value': i} for i in all_fclubs],
#                 value=all_fclubs[0],
#                 multi=False
#             )
#         ], width=3),
#         dbc.Col([
#             html.P("Выберите футболиста:")
#         ], width=2),
#         dbc.Col([
#             dcc.Dropdown(
#                 id='crossfilter-fplayer',
#                 multi=False
#             )
#         ], width=3),
#         dbc.Col([
#             html.P("Выберите год:")
#         ], width=2),
#         dbc.Col([
#             dcc.Dropdown(
#                 id='crossfilter-year',
#                 options=[{'label': year, 'value': year} for year in range(2016, 2020)],
#                 value=2016,
#                 multi=False
#             )
#         ], width=2)
#     ]),

#     html.Br(),

#     dbc.Row([
#         dbc.Col([
#             dbc.Card([
#                 dbc.Row([
#                     dbc.CardHeader("Имя футболиста")
#                 ]),
#                 dbc.Row([
#                     dbc.Col([
#                         dbc.CardImg(src='/static/images/player.png')
#                     ], width=5),
#                     dbc.Col([
#                         dbc.CardBody(
#                             html.P(
#                                 id='card_text1',
#                                 className="card-value"),
#                         )
#                     ], width=6),
#                     dbc.Col([
#                         html.P(' '),
#                     ], width=6, style={'padding': '15px 35px 15px 5px'}),
#                 ])
#             ], color="primary", outline=True, style={'textAlign': 'center'}),
#         ], width=4),
#         dbc.Col([
#             dbc.Card([
#                 dbc.Row([
#                     dbc.CardHeader("Клуб")
#                 ]),
#                 dbc.Row([
#                     dbc.Col([
#                         dbc.CardImg(src='/static/images/fclub.png')
#                     ], width=5),
#                     dbc.Col([
#                         dbc.CardBody(
#                             html.P(
#                                 id='card_text2',
#                                 className="card-value"),
#                         )
#                     ], width=6),
#                     dbc.Col([
#                         html.P('(сокращенное наименование)'),
#                     ], width=6, style={'padding': '15px 35px 15px 5px'}),
#                 ])
#             ], color="primary", outline=True, style={'textAlign': 'center'}),
#         ], width=4),
#         dbc.Col([
#             dbc.Card([
#                 dbc.Row([
#                     dbc.CardHeader("Забитые мячи")
#                 ]),
#                 dbc.Row([
#                     dbc.Col([
#                         dbc.CardImg(src='/static/images/goals.png')
#                     ], width=5),
#                     dbc.Col([
#                         dbc.CardBody(
#                             html.P(
#                                 id='card_text3',
#                                 className="card-value"),
#                         )
#                     ], width=6),
#                     dbc.Col([
#                         html.P(' '),
#                     ], width=6, style={'padding': '15px 35px 15px 5px'}),
#                 ])
#             ], color="primary", outline=True, style={'textAlign': 'center'}),
#         ], width=4),
#         dbc.Col([
#             dbc.Card([
#                 dbc.Row([
#                     dbc.CardHeader("Матчи")
#                 ]),
#                 dbc.Row([
#                     dbc.Col([
#                         dbc.CardImg(src='/static/images/fmatch.png')
#                     ], width=6),
#                     dbc.Col([
#                         dbc.CardBody(
#                             html.P(
#                                 id='card_text4',
#                                 className="card-value"),
#                         )
#                     ], width=6),
#                     dbc.Col([
#                         html.P(' '),
#                     ], width=6, style={'padding': '15px 35px 15px 5px'}),
#                 ])
#             ], color="primary", outline=True, style={'textAlign': 'center'}),
#         ], width=4),
#         dbc.Col([
#             html.Br(),
#             dbc.Row([
#                 html.H5('Лучший игрок клуба'),
#                 html.Div(id='table1'),
#             ], style={'textAlign': 'center'})
#         ], width=4)
#     ], style={'textAlign': 'center'}),
# ])

# @callback(
#     [Output('crossfilter-fplayer', 'options'),
#      Output('crossfilter-fplayer', 'value')],
#     [Input('crossfilter-fclubs', 'value'),
#      Input('crossfilter-year', 'value')]
# )
# def update_player_dropdown(club, year):
#     all_fplayer = df[(df['Club'] == club) & (df['Year'] == year)]['Player Names'].unique()
#     dd_fplayer = [{'label': i, 'value': i} for i in all_fplayer]
#     dd_fplayer_value = all_fplayer[0] if all_fplayer else None
#     return dd_fplayer, dd_fplayer_value

# @callback(
#     [Output('card_text1', 'children'),
#      Output('card_text2', 'children'),
#      Output('card_text3', 'children'),
#      Output('card_text4', 'children'),
#      Output('table1', 'children')],
#     [Input('crossfilter-fplayer', 'value'),
#      Input('crossfilter-fclubs', 'value'),
#      Input('crossfilter-year', 'value')]
# )
# def update_card(player, club, year):
#     if not player:
#         return "Игрок не найден", "Нет данных", "0", "0", html.Div("Данные об игроке не найдены")
    
#     df_player = df[(df['Player Names'] == player) & (df['Year'] == year)]
#     df_player_prev = df[(df['Player Names'] == player) & (df['Year'] == year - 1)]
#     xG_player = df[(df['Club'] == club) & (df['Year'] == year)].sort_values(by='xG', ascending=False)

#     if df_player.empty or df_player_prev.empty:
#         return "Игрок не найден", "Нет данных", "0", "0", html.Div("Данные об игроке не найдены")

#     ct1 = df_player.iloc[0]['Player Names']
#     ct2 = df_player.iloc[0]['Club']
#     ct3 = df_player.iloc[0]['Goals']
#     ct4 = df_player.iloc[0]['Matches_Played']
#     xG_curr = df_player.iloc[0]['xG']
#     xG_prev = df_player_prev.iloc[0]['xG']
#     xG_table = xG_player.iloc[0:1][['Player Names', 'xG']]

#     if xG_prev != 0:
#         delta_xG = round((xG_curr - xG_prev) / xG_prev, 2) * 100
#     else:
#         delta_xG = 0

#     table = dbc.Table.from_dataframe(
#         xG_table, striped=True, bordered=True, hover=True, index=False)

#     return ct1, ct2, ct3, ct4, table


import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input, Dash
import pandas as pd
import plotly.express as px


# Загрузка и фильтрация данных
df = pd.read_csv('DataFoot.csv', sep=',')
df = df[(df['Year'] >= 2016) & (df['Year'] <= 2020)]

layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([
                html.H3("Подробная информация о футболистах по клубам"),
                html.Hr(style={'color': 'black'}),
            ], style={'textAlign': 'center'})
        )
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            html.P("Выберите год:")
        ], width=2),
        dbc.Col([
            dcc.Dropdown(
                id='crossfilter-year',
                options=[{'label': year, 'value': year} for year in range(2016, 2021)],
                value=2016,
                multi=False
            )
        ], width=3),
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            html.P("Выберите клуб:")
        ], width=2),
        dbc.Col([
            dcc.Dropdown(
                id='crossfilter-fclubs',
                multi=False
            )
        ], width=3),
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            html.P("Выберите футболиста:")
        ], width=2),
        dbc.Col([
            dcc.Dropdown(
                id='crossfilter-fplayer',
                multi=False
            )
        ], width=3),
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.Row([
                    dbc.CardHeader("Имя футболиста")
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.CardImg(src='/static/images/player.png')
                    ], width=5),
                    dbc.Col([
                        dbc.CardBody(
                            html.P(
                                id='card_text1',
                                className="card-value"),
                        )
                    ], width=6),
                    dbc.Col([
                        html.P(' '),
                    ], width=6, style={'padding': '15px 35px 15px 5px'}),
                ])
            ], color="primary", outline=True, style={'textAlign': 'center'}),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.Row([
                    dbc.CardHeader("Клуб")
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.CardImg(src='/static/images/fclub.png')
                    ], width=5),
                    dbc.Col([
                        dbc.CardBody(
                            html.P(
                                id='card_text2',
                                className="card-value"),
                        )
                    ], width=6),
                    dbc.Col([
                        html.P('(сокращенное наименование)'),
                    ], width=6, style={'padding': '15px 35px 15px 5px'}),
                ])
            ], color="primary", outline=True, style={'textAlign': 'center'}),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.Row([
                    dbc.CardHeader("Забитые мячи")
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.CardImg(src='/static/images/goals.png')
                    ], width=5),
                    dbc.Col([
                        dbc.CardBody(
                            html.P(
                                id='card_text3',
                                className="card-value"),
                        )
                    ], width=6),
                    dbc.Col([
                        html.P(' '),
                    ], width=6, style={'padding': '15px 35px 15px 5px'}),
                ])
            ], color="primary", outline=True, style={'textAlign': 'center'}),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.Row([
                    dbc.CardHeader("Матчи")
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.CardImg(src='/static/images/fmatch.png')
                    ], width=6),
                    dbc.Col([
                        dbc.CardBody(
                            html.P(
                                id='card_text4',
                                className="card-value"),
                        )
                    ], width=6),
                    dbc.Col([
                        html.P(' '),
                    ], width=6, style={'padding': '15px 35px 15px 5px'}),
                ])
            ], color="primary", outline=True, style={'textAlign': 'center'}),
        ], width=4),
        dbc.Col([
            html.Br(),
            dbc.Row([
                html.H5('Лучший игрок клуба'),
                html.Div(id='table1'),
            ], style={'textAlign': 'center'})
        ], width=4)
    ], style={'textAlign': 'center'}),
])

@callback(
    [Output('crossfilter-fclubs', 'options'),
     Output('crossfilter-fclubs', 'value')],
    Input('crossfilter-year', 'value')
)
def update_club_dropdown(year):
    filtered_df = df[df['Year'] == year]
    all_fclubs = filtered_df['Club'].unique()
    club_options = [{'label': club, 'value': club} for club in all_fclubs]
    club_value = all_fclubs[0] 
    return club_options, club_value

@callback(
    [Output('crossfilter-fplayer', 'options'),
     Output('crossfilter-fplayer', 'value')],
    [Input('crossfilter-fclubs', 'value'),
     Input('crossfilter-year', 'value')]
)
def update_player_dropdown(club, year):
    filtered_df = df[(df['Club'] == club) & (df['Year'] == year)]
    all_fplayer = filtered_df['Player Names'].unique()
    player_options = [{'label': player, 'value': player} for player in all_fplayer]
    player_value = all_fplayer[0] 
    return player_options, player_value

@callback(
    [Output('card_text1', 'children'),
     Output('card_text2', 'children'),
     Output('card_text3', 'children'),
     Output('card_text4', 'children'),
     Output('table1', 'children')],
    [Input('crossfilter-fplayer', 'value'),
     Input('crossfilter-fclubs', 'value'),
     Input('crossfilter-year', 'value')]
)
def update_card(player, club, year):
    if not player:
        return "Игрок не найден", "Нет данных", "0", "0", html.Div("Данные об игроке не найдены")
    
    df_player = df[(df['Player Names'] == player) & (df['Year'] == year)]
    df_player_prev = df[(df['Player Names'] == player) & (df['Year'] == year - 1)]
    xG_player = df[(df['Club'] == club) & (df['Year'] == year)].sort_values(by='xG', ascending=False)

    if df_player.empty or df_player_prev.empty:
        return "Игрок не найден", "Нет данных", "0", "0", html.Div("Данные об игроке не найдены")

    ct1 = df_player.iloc[0]['Player Names']
    ct2 = df_player.iloc[0]['Club']
    ct3 = df_player.iloc[0]['Goals']
    ct4 = df_player.iloc[0]['Matches_Played']
    xG_curr = df_player.iloc[0]['xG']
    xG_prev = df_player_prev.iloc[0]['xG']
    xG_table = xG_player.iloc[0:1][['Player Names', 'xG']]

    if xG_prev != 0:
        delta_xG = round((xG_curr - xG_prev) / xG_prev, 2) * 100
    else:
        delta_xG = 0

    table = dbc.Table.from_dataframe(
        xG_table, striped=True, bordered=True, hover=True, index=False)

    return ct1, ct2, ct3, ct4, table













