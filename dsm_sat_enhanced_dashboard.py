
import dash
from dash import dcc, html, Input, Output, State, dash_table
import pandas as pd
import plotly.graph_objects as go
import io
import base64

app = dash.Dash(__name__)
app.title = "DSM+SAT Enhanced Dashboard"

app.layout = html.Div([
    html.H2("DSM+SAT | Enhanced DSM Dashboard", style={'textAlign': 'center', 'color': '#0f62fe'}),
    dcc.Upload(
        id='upload-data',
        children=html.Div(['📁 Drag and Drop or Click to Upload Energy Data']),
        style={'width': '100%', 'height': '80px', 'lineHeight': '80px',
               'borderWidth': '1px', 'borderStyle': 'dashed',
               'borderRadius': '5px', 'textAlign': 'center'},
        multiple=False
    ),
    html.Div(id='upload-data-output')
])

@app.callback(
    Output('upload-data-output', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def update_output(contents, filename):
    if contents is None:
        return html.Div(["Upload household energy data to begin analysis."])
    
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    
    summary = df.describe().to_dict()
    mean_usage = df['Consumption'].mean()
    df['Persona'] = df['Consumption'].apply(
        lambda x: 'Saver' if x < mean_usage * 0.8 else ('Overconsumer' if x > mean_usage * 1.2 else 'Moderate'))
    
    persona_counts = df['Persona'].value_counts().to_dict()

    return html.Div([
        html.H4(f"Summary for {filename}"),
        html.P(f"Mean Consumption: {mean_usage:.2f} kWh"),
        html.Ul([html.Li(f"{k}: {v} users") for k, v in persona_counts.items()]),
        dash_table.DataTable(data=df.to_dict('records'), page_size=5, style_table={'overflowX': 'auto'})
    ])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=10000)
