import dash
import dash_core_components as dcc #Generate graphs
import dash_html_components as html #Generate html in the backend
import pandas as pd
import BalanceSheet
from dash import dependencies

df = BalanceSheet.bsimport('AAPL')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# Stylesheet (CSS?)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# The first part is the "layout" of the app and it describes what the application looks like
app.layout = html.Div(children=[
    dcc.Input(id='stock',value='AAPL',type='text'),
    html.H4(children='Balance Sheet'),
    html.Table(id='bsdataframe')
])

# The second part is the "callback" of the app and it describes interactive elements
@app.callback(
     dash.dependencies.Output('bsdataframe','children'),
     [dash.dependencies.Input(component_id='stock', component_property='value')]
 )
def generate_table(input_value,max_rows=10):
    global bsdataframe
    bsdataframe = BalanceSheet.bsimport(input_value)
    return [html.Tr([html.Th(col) for col in bsdataframe.columns])] + [html.Tr([
        html.Td(bsdataframe.iloc[i][col]) for col in bsdataframe.columns
    ]) for i in range(min(len(bsdataframe), max_rows))]

#Run App (With hot-reloading)
if __name__ == '__main__':
    app.run_server(debug=True)