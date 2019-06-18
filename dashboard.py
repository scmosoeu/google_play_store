# DASH IMPORTS
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

# PYTHON IMPORTS
import pandas as pd
import numpy as np

# OTHER IMPORTS
from app import app
from sentiment_analysis.user_reviews import sentiments
from sentiment_analysis import play_store_overview

app.layout = html.Div([
    dcc.Tabs(id='tabs',children=[
        dcc.Tab(label='Sentiments',value='sentiments',
            selected_style={
                'backgroundColor':'#111',
                'color':'white',
                'fontWeight':'bold',
                'fontSize':20
            }),
        dcc.Tab(label='Overview',value='overview',
            selected_style={
                'backgroundColor':'#111',
                'color':'white',
                'fontWeight':'bold',
                'fontSize':20
            })
    ],style={'fontWeight':'bold','fontSize':20,'lineHeight':0}),
    html.Div(id='content')
])

@app.callback(Output('content','children'),
             [Input('tabs','value')])

def display_content(selected_tab):

    if selected_tab == 'sentiments':
        return sentiments
    elif selected_tab == 'overview':
        return play_store_overview.overview

if __name__ == '__main__':
    app.run_server(debug=True)
