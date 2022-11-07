"""
Based on Mohit Mayank's tutorial on representing the plot of 
Game of Thrones network using Visdcc in Dash.

The original example was modified to account for changes in Dash and 
Visdcc API, and simplified for the purposes of this class.

#### Installation instructions:
In order to run this tutorial, the following libraries must be installed:
* pandas
* networkx
* matplotlib
* pyvis
* dash
* visdcc
Note that installing some of these libraries these libraries on top of your core Python or Anaconda install may cause conflicts and version collission issues.  In order to avoid these issues, I highly recommend doing this within a virtual environment.

#### Virtual environment setup instructions
1. In your project folder, set up a virtual environment: _python3 -m venv /path/to/new/virtual/environment_
2. Launch your virtual environment.  For example, if your virtual environment folder is called _env_, you can launch it by executing _source ./env/bin/activate_. You can find a complete tutorial at https://docs.python.org/3/library/venv.html
3. Install libraries:
    * ./env/bin/pip3 install pandas
    * ./env/bin/pip3 install networkx
    * ./env/bin/pip3 install matplotlib
    * ./env/bin/pip3 install pyvis
    * ./env/bin/pip3 install dash
    * ./env/bin/pip3 install visdcc
    

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
