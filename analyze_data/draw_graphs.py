import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import json


def draw_graphs():
    data = json.load(open('results.json', 'r', encoding='utf-8'))

    picks_data = data[0]['picks']
    bans_data = data[1]['bans']

    df = pd.DataFrame(picks_data.items(), columns=['Hero', 'Picks'])
    df.sort_values(by=['Picks'], ascending=False, inplace=True)
    counter = df.loc[15:, 'Picks'].sum()
    df.drop(df.tail(88).index, inplace=True)
    df.loc[-1] = ['Others', counter]

    df2 = pd.DataFrame(bans_data.items(), columns=['Hero', 'Bans'])
    df2.sort_values(by=['Bans'], ascending=False, inplace=True)
    counter = df2.loc[10:, 'Bans'].sum()
    df2.drop(df2.tail(83).index, inplace=True)
    df2.loc[-1] = ['Others', counter]

    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])

    fig.add_trace(go.Pie(values=df['Picks'].values, labels=df['Hero'].values,
                         title='<i>Top-15 Most <b>Picked</b> Heroes</i>', name='Pick'), 1, 1)
    fig.add_trace(go.Pie(values=df2['Bans'].values, labels=df2['Hero'].values,
                         title='<i>Top-15 Most <b>Banned</b> Heroes</i>', name='Ban'), 1, 2)
    fig.update_layout(title_text='MLBB Tournament Meta (starting from 2024)')
    fig.update_traces(textinfo='label+percent')
    fig.show()
