import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html
from pages import statistic, player, clubs, infoInCards
import pandas as pd

df = pd.read_csv('DataFoot.csv', sep=',')


external_stylesheets = [dbc.themes.CYBORG]  # Выбрали тему из https://bootswatch.com/
app = Dash(__name__, external_stylesheets=external_stylesheets,  use_pages=True)
app.config.suppress_callback_exceptions = True



# Задаем аргументы стиля для боковой панели. Мы используем position:fixed и фиксированную ширину
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#004680", # Задаем цвет фона боковой панели 
}
# Справа от боковой панели размешается основной дашборд. Добавим отступы
CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
sidebar = html.Div(
    [
        html.H2("Показатели футболистов", className="display-6"),
        html.Hr(),
        html.P(
            "Учебный проект студентов БСБО-13-21", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Общая статистика", href="/", active="exact"),
                dbc.NavLink("Деятельность футболистов по странам", href="/page-1", active="exact"),
                dbc.NavLink("Статистика по клубам", href="/page-2", active="exact"),
                dbc.NavLink("Параметры футболиста", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return statistic.layout
    elif pathname == "/page-1":
        return player.layout
    elif pathname == "/page-2":
        return clubs.layout
    elif pathname == "/page-3":
        return infoInCards.layout
    
    # Если пользователь попытается перейти на другую страницу, верните сообщение 404. Мы изменим её в следующей практической.
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == '__main__':
        app.run_server(debug=True)



