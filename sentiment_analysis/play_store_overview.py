# DASH IMPORTS
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

# PLOTLY IMPORTS
import plotly.graph_objs as go

# OTHER IMPORTS
import pandas as pd
import numpy as np
from app import app

df = pd.read_csv('google_play_store_data/googleplaystore.csv')
df.dropna(inplace=True)
df = df[df['Content Rating'] != 'Unrated']
df.reset_index(drop=True,inplace=True)

overview = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(
                id='my-pie-chart',
                figure={
                    'data':[
                        go.Pie(
                            labels=df['Content Rating'].value_counts().index,
                            values=df['Content Rating'].value_counts()
                        )
                    ],
                    'layout':go.Layout(
                        hovermode='closest',
                        title='Content Rating',
                        font={'size':12}
                    )
                }
            )
        ],style={'display':'inline-block','fontWeight':'bold'}),
        html.Div(id='type',style={'display':'inline-block'})
    ]),
    html.Div([
        html.Div(id='Seee',style={'display':'inline-block'}),
        html.Div(id='000',style={'display':'inline-block'})
    ])
])

@app.callback(Output('type','children'),
             [Input('my-pie-chart','clickData')])

def type_info(clickData):

    if clickData is not None:
        content = clickData['points'][0]['label']
        return html.H3('{}'.format(content))
