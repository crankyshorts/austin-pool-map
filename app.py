import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import sqlite3
import pandas as pd

app = dash.Dash(__name__)

# Load data
conn = sqlite3.connect("pools.db")
df = pd.read_sql("SELECT * FROM pools", conn)
conn.close()

# Create a map visualization
fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="name",
                         mapbox_style="open-street-map")

app.layout = html.Div([
    html.H1("Austin Pool Map"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)