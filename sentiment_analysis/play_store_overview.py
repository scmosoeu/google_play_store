# DASH IMPORTS
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

# PLOTLY IMPORTS
import plotly.graph_objs as go
import plotly.figure_factory as ff

# OTHER IMPORTS
import pandas as pd
import numpy as np
from app import app

df = pd.read_csv('google_play_store_data/googleplaystore.csv')
df.dropna(inplace=True)
df = df[df['Content Rating'] != 'Unrated'] # Unrated only had 2 rows in the dataset
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
        ],style={'display':'inline-block'}),
        html.Div([
            dcc.Graph(
                figure={
                    'data':[
                        go.Bar(
                            x=df.groupby('Content Rating')['Category'].nunique().index,
                            y=df.groupby('Content Rating')['Category'].nunique()
                        )
                    ],
                    'layout':go.Layout(
                        title='Number of Categories',
                        yaxis={'title':'count'}
                    )
                }
            )
        ],style={
            'display':'inline-block',
            'fontSize':12,
            'fontWeight':'bold',
            'width':'60%',
            'float':'right'
        })
    ]),
    html.Div([
        html.Div(id='type',style={'display':'inline-block'}),
        html.Div(id='ratings',style={
            'display':'inline-block',
            'fontSize':12,
            'fontWeight':'bold',
            'width':'60%',
            'float':'right'
        })
    ])
])

@app.callback(Output('ratings','children'),
             [Input('my-pie-chart','clickData')])

def ratings_info(clickData):
    if clickData is not None:
        filtered_df = df[df['Content Rating'] == clickData['points'][0]['label']]
        fig = ff.create_distplot(
            hist_data=[filtered_df['Rating']],
            group_labels=['{}'.format(clickData['points'][0]['label'])],
            colors=['seagreen']
        )
        fig.layout.update({'title':'Apps for {} Ratings Distribution'.format(clickData['points'][0]['label'])})
        return dcc.Graph(
            figure=fig
        )

@app.callback(Output('type','children'),
             [Input('my-pie-chart','clickData')])

def type_info(clickData):

    if clickData is not None:

        filtered_df = df[df['Content Rating'] == clickData['points'][0]['label']]
        data = [
            go.Bar(
                x=filtered_df.groupby('Type')['Type'].count().index,
                y=filtered_df.groupby('Type')['Type'].count()
            )
        ]

        layout = go.Layout(
            title='App types for {}'.format(clickData['points'][0]['label']),
            yaxis={'title':'count'},
            font={'size':12}
        )
        return dcc.Graph(
            figure={
                'data':data,
                'layout':layout
            }
        )
