import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Label import Label

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def entname(name):
    return html.Span(name, style={
        "font-size": "0.8em",
        "font-weight": "bold",
        "line-height": "1",
        "border-radius": "0.35em",
        "text-transform": "uppercase",
        "vertical-align": "middle",
        "margin-left": "0.5rem"
    })


def entbox(children, color):
    return html.Mark(children, style={
        "background": color,
        "padding": "0.45em 0.6em",
        "margin": "0 0.25em",
        "line-height": "1",
        "border-radius": "0.35em",
    })


app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

Suppress_callback_exceptions=True

app.layout = html.Div(children=[html.Div(children=[
    html.H1(children = "QA",style={'textAlign': 'center'}),
    html.Div(children = [
        html.Label('Select the Apprisal'),
        dcc.Dropdown(id="ta_select",
        options=[
            {'label': 'ALL', 'value': 'all'},
            {'label': 'TA2', 'value': 'TA2'},
            {'label': 'TA3', 'value': 'TA3'}
        ],
        value='all'
    )],style = {"margin-left": "60px"},className="one-third column"),
    #html.Br(),
    html.Div(children=[
        html.Label('Put the question on below box'),
        dcc.Textarea(id='question',value='MTL',style={'width': '150%','height': '100%',"margin-right":"80px"})],className="one-third column"),
],className="row"),
html.Br(),
html.Div([html.Button('Submit', id='all_submit')],style={'display':'flex','justifyContent':'center'}),
html.Br(),
html.Div(id='container')
])

@app.callback(
    Output('container', 'children'),
    [Input('all_submit', 'n_clicks'),
     Input('question', 'value'),
     Input('ta_select', 'value')])
def display_output(n_clicks,qa,ta):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'all_submit' in changed_id:
        return html.Div([
            html.Div([
                "This is a text " + qa
            ],style={'display':'flex','justifyContent':'center',"border":"2px black solid","margin-left": "60px","margin-right":"100px"}),
            html.Br(),
            html.Label('Are you satisfaied with the response ?',style={"margin-left": "60px"}),
            dcc.RadioItems(id ="satisfy",
                options=[
                    {'label': 'Yes', 'value': 'yes'},
                    {'label': 'No', 'value': 'no'}
                ],
                value='yes',
                labelStyle={'display': 'inline-block',"margin-left": "60px"}
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
            html.Label("Please check out the below response ",style={"margin-left": "60px"}),
            html.Div([
                "This is a text " + qa
            ],style={'display':'flex','justifyContent':'center',"border":"2px black solid","margin-left": "60px","margin-right":"100px"}),
             html.Div([
                "This is a text " + qa
            ],style={'display':'flex','justifyContent':'center',"border":"2px black solid","margin-left": "60px","margin-right":"100px"}),
             html.Div([
                "This is a text " + qa
            ],style={'display':'flex','justifyContent':'center',"border":"2px black solid","margin-left": "60px","margin-right":"100px"}),
             html.Div([
                "This is a text " + qa
            ],style={'display':'flex','justifyContent':'center',"border":"2px black solid","margin-left": "60px","margin-right":"100px"}),
            html.Br(),
            html.Label("Please let us know if any one of the newly generated response was useful, as this helps to improve our Model",style={"margin-left": "60px"}),

            dcc.RadioItems(id ="satisfy2",
                options=[
                    {'label': '1st', 'value': '1'},
                    {'label': '2nd', 'value': '2'},
                    {'label': '3rd', 'value': '3'},
                    {'label': '4th', 'value': '4'},
                    {'label': 'None', 'value': '5'}
                ],
                value='5',
                labelStyle={'display': 'inline-block',"margin-left": "60px"}
            )

        ])




if __name__ == '__main__':
    app.run_server(debug=True)