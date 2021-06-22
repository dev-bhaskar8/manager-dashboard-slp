import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)
sheetId2 = "16pb9hkyaWsBLwYAAUlLDW3oSk9pTa2c5ARMavxysrXk"
sheetName2 = "SnapShot"
sheetURL2 = f"https://docs.google.com/spreadsheets/d/{sheetId2}/gviz/tq?tqx=out:csv&sheet={sheetName2}"
df = pd.read_csv(sheetURL2,index_col=None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


@app.callback(dash.dependencies.Output('slp', 'figure'),
    [dash.dependencies.Input('names', 'value')])
def name_selection(names = 1):
    try:
        graphdf = df.iloc[names,:].dropna()
        graphdf=graphdf[1:]
        index = graphdf.index
        graphdf = graphdf.reset_index()
        graphdf.rename(columns={'index':'Days'},inplace=True)
        graphdf.rename(columns={names:'SLP'},inplace=True)
        fig1 = px.bar(graphdf,x='Days',y='SLP',color='Days')
        fig1.update_layout(
        title="Daily Compounded SLP",
        xaxis_title="Days",
        yaxis_title="SLP",
        showlegend=False
        )
                
        fig2 = px.line(graphdf,x='Days',y='SLP',color_discrete_sequence=['#ffcc00'])
        fig2.update_traces(line=dict(width=10))
        fig1.add_trace(fig2.data[0])
        return fig1

    except:
        graphdf = df.iloc[1,:].dropna()
        graphdf=graphdf[1:]
        index = graphdf.index
        graphdf = graphdf.reset_index()
        graphdf.rename(columns={'index':'Days'},inplace=True)
        graphdf.rename(columns={1:'SLP'},inplace=True)
        fig1 = px.bar(graphdf,x='Days',y='SLP',color='Days')
        fig1.update_layout(
        title="Daily Compounded SLP",
        xaxis_title="Days",
        yaxis_title="SLP",
        showlegend=False
        )
                
        fig2 = px.line(graphdf,x='Days',y='SLP',color_discrete_sequence=['#ffcc00'])
        fig2.update_traces(line=dict(width=10))
        fig1.add_trace(fig2.data[0])
        return fig1
    

    
app.layout = html.Div(children=[
    html.H1(children='Manager Dashboard'),
    html.Div(children='''
        Made with 💙by  Vaas.\n
    '''),
    html.Div(children='''
        Scholar Name:
    '''),
    dcc.Dropdown(
                id='names',
                options=[{'label': df['name'][i], 'value': i} for i in df['name'].index],
                value='Fertility rate, total (births per woman)'
            ),
    dcc.Graph(
        id='slp',
        #figure=fig1
    ),
    
])

if __name__ == '__main__':
    app.run_server(debug=True, port=int(os.environ.get("PORT", 3966)), host='0.0.0.0')
