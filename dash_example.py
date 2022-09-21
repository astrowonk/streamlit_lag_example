from dash import Dash, dcc, html, Input, Output
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
fig = df.plot.scatter(x='a', y='b', color='c', backend='plotly')

graphs = html.Div([dcc.Graph(figure=fig) for x in range(4)])

layout = html.Div(
    [dcc.Textarea(
        id='the_input',
        style={
            'width': '100%',
            'height': 300
        },
    ),graphs])



app = Dash("test_lag",
           title="Test Lag",
           meta_tags=[
               {
                   "name": "viewport",
                   "content": "width=device-width, initial-scale=1"
               },
           ])

app.layout = layout
if __name__ == "__main__":
    app.run_server(debug=True)
