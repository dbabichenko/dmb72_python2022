"""
Author: Mohit Mayank

Idea: Plot Game of Thrones network using Visdcc in Dash.
"""
# imports
import dash
import visdcc
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

# create app
app = dash.Dash()

# load data
df = pd.read_csv("data/book1.csv")
df = df.loc[df['weight']>10, :]
node_list = list(set(df['Source'].unique().tolist() + df['Target'].unique().tolist()))
nodes = [{'id': node_name, 'label': node_name, 'shape': 'dot', 'size': 7} for i, node_name in enumerate(node_list)]
# create edges from df
edges = []
for row in df.to_dict(orient='records'):
    source, target = row['Source'], row['Target']
    edges.append({
        'id': source + "__" + target,
        'from': source,
        'to': target,
        'width': 2,
    })

# define layout
app.layout = html.Div([
      visdcc.Network(id = 'net', 
                     data = {'nodes': nodes, 'edges': edges},
                     options = dict(height= '600px', width= '100%'))
])

# define callback
def myfun(x):
    return {'nodes':{'color': x}}

# define main calling
if __name__ == '__main__':
    app.run_server(debug=True)
