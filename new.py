import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd


###Coming from elastic search directly 
ta_list = []

app = dash.Dash(external_stylesheets=[dbc.themes.SPACELAB],suppress_callback_exceptions=True)

suppress_callback_exceptions=True

first_card = dbc.Card(
    dbc.CardBody(
        [
        dbc.Row([
            dbc.Col(
                [
                html.H5("Select The Apprisal", className="card-title"),
                dcc.Dropdown(id="ta_select",
                    options=[
                        {'label': 'ALL', 'value': 'all'},
                        {'label': 'TA2', 'value': 'TA2'},
                        {'label': 'TA3', 'value': 'TA3'}
                    ],
                    value='all'
                )
                ]
            ),
            dbc.Col([
                html.H5("Put the question on below box", className="card-title"),
                dcc.Textarea(id='question',value='MTL',style={'width': '90%','height': '50%',"margin-right":"80px"}),
                html.Br(),
                dbc.Button("Submit", color="primary",id='all_submit'),


            ])
        ]
        )

        ]
    )
,style={"border":"1px black solid"})




app.layout = dbc.Container(
    [
        html.H1("Iris k-means clustering"),
        html.Hr(),
        first_card,
        html.Br(),
        html.Div(id='container')
    ],
    fluid=True,
)


@app.callback(
    Output('container', 'children'),
    [Input('all_submit', 'n_clicks'),
     Input('question', 'value'),
     Input('ta_select', 'value')])
def display_output(n_clicks,qa,ta):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'all_submit' in changed_id:
        ##Retriver
        ##Reader
        text = "This is a text " + qa
        new_text = text.replace(qa, f"***{qa}***")
        return html.Div([
            html.Div([
                 dbc.Card(
                    dbc.CardBody(dcc.Markdown(new_text,dangerously_allow_html=True,)),
                style={"border":"1px black solid",'color': 'black', 'fontSize': "18px"})
            ]),
            html.Br(),
            dbc.Label("Are you satisfaied with the response?",style={'color': 'black', 'fontSize': "18px"}),
            dbc.RadioItems(id ="satisfy",
                options=[
                    {'label': 'Yes', 'value': 'yes'},
                    {'label': 'No', 'value': 'no'}
                ],
                value=[],
                inline=True,
                style={'color': 'black', 'fontSize': "18px"}
            ),  
            html.Div(id='dynamic-output')
        ])
@app.callback(
    Output('dynamic-output', 'children'),
    [Input('satisfy', 'value'),
     Input('question', 'value'),
     Input('ta_select', 'value')])
def display_nextbatch(satisfy,qa,ta):
    print(satisfy)
    if satisfy == "no":
        return html.Div([
            html.Br(),
            dbc.Label("Please check out the additional response ",style={'color': 'black', 'fontSize': "18px"}),
            html.Div([
                                 dbc.Card(
                    dbc.CardBody("This is a text " + qa)
                ,style={"border":"1px black solid",'color': 'black', 'fontSize': "18px"})
            ]),
             html.Br(),
             html.Div([
                                dbc.Card(
                    dbc.CardBody("This is a text " + qa)
                ,style={"border":"1px black solid",'color': 'black', 'fontSize': "18px"})
            ]),
             html.Br(),
             html.Div([
                dbc.Card(
                    dbc.CardBody("This is a text " + qa)
                ,style={"border":"1px black solid",'color': 'black', 'fontSize': "18px"})
            ]),
             html.Br(),
             html.Div([
                dbc.Card(
                    dbc.CardBody("This is a text " + qa)
                ,style={"border":"1px black solid",'color': 'black', 'fontSize': "18px"})
            ]),
            html.Br(),
            dbc.Label("Please let us know if any one of the newly generated response was useful, as this helps to improve our Model",style={'color': 'black', 'fontSize': "18px"}),
            dbc.RadioItems(id ="satisfy2",
                options=[
                    {'label': '1st', 'value': '1'},
                    {'label': '2nd', 'value': '2'},
                    {'label': '3rd', 'value': '3'},
                    {'label': '4th', 'value': '4'},
                    {'label': 'None', 'value': '5'}
                ],
                value=[],
                inline=True,
                style={'color': 'black', 'fontSize': "18px"}
            )

        ])











if __name__ == '__main__':
    app.run_server(debug=True)