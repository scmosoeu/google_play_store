# IMPORT DASH COMPONENTS
import dash_core_components as dcc
import dash_html_components as html

# PLOTLY IMPORTS
import plotly.graph_objs as go
import plotly.figure_factory as ff

# IMPORT OTHERS
import pandas as pd
import numpy as np

df = pd.read_csv('google_play_store_data/googleplaystore_user_reviews.csv')
df.dropna(inplace=True)
df.reset_index(drop=True,inplace=True)

sentiments = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(
                figure={
                    'data':[
                        go.Pie(
                            labels=['Positive','Negative','Neutral'],
                            values=[
                                len(df[df['Sentiment']=='Positive']),
                                len(df[df['Sentiment']=='Negative']),
                                len(df[df['Sentiment']=='Neutral'])
                            ]
                        )
                    ],
                    'layout':go.Layout(
                        title='Sentiments',
                        plot_bgcolor='#111',
                        paper_bgcolor='#111',
                        font={'color':'white','size':16},
                        legend={'orientation':'h','x':0.2}
                    )
                }
            )
        ],style={
            'width':'40%',
            'display':'inline-block',
            'fontWeight':'bold'
        }),
        html.Div([
            dcc.Graph(
                figure={
                    'data':[
                        go.Bar(
                            x=df.groupby('Sentiment')['Sentiment_Polarity'].mean().index,
                            y=df.groupby('Sentiment')['Sentiment_Polarity'].mean(),
                            name='Sentiment Polarity'
                        ),
                        go.Bar(
                            x=df.groupby('Sentiment')['Sentiment_Subjectivity'].mean().index,
                            y=df.groupby('Sentiment')['Sentiment_Subjectivity'].mean(),
                            name='Sentiment Subjectivity'
                        )
                    ],
                    'layout':go.Layout(
                        title='Sentiment Overview',
                        barmode='group',
                        plot_bgcolor='#111',
                        paper_bgcolor='#111',
                        font={'color':'white','size':16}
                    )
                }
            )
        ],style={'width':'60%','display':'inline-block'})
    ]),
    html.Div([

    ])
])
