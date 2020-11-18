import dash
import dash_core_components as dash_cc
import dash_html_components as dash_html
import dash_table
from   dash.dependencies import Input, Output
import BL.DividendsBL as divBL
import GUI.GUICentral as gui
import plotly.graph_objs as go
import pandas as pd

def build():
    mainWindow = dash.Dash()
    
    mainWindow.layout = dash_html.Div(
        style={
            'backgroundColor' : 'black',
            'align-items'     : 'center',
            'padding'         : 15
        },
        children=[
            #title
                dash_html.Div(
                    children=[
                            dash_html.H1('Dividends Graph Test'),
                            dash_html.H2(  
                                children='Select a Ticker from the List',
                                style={
                                  'textAlign': 'center',
                                  'color'    : gui.Colors.TEXT
                                }
                            )
                    ],
                    style={
                        'backgroundColor': gui.Colors.BACKGROUND,
                        'textAlign'      : 'center',
                        'color'          : gui.Colors.TEXT,
                        'border'         :'2px solid '+gui.Colors.TEXT
                    }
                ),
                # Ticker selector and ticker details (everything below title)
                dash_html.Div(
                        style={ 
                                'justify-content':'center'
                        },
                        children=[
                            dash_html.Div(
                                style={
                                    'backgroundColor': gui.Colors.BACKGROUND,
                                    'width'          :'15%',
                                    'display'        :'inline-block'
                                },
                                children=[
                                    dash_table.DataTable(
                                        id='ticker-table',
                                        columns=[{"name": "TICKER", "id": "TICKER"}],
                                        style_cell={
                                            'textAlign'       : 'center',
                                            'color'           : gui.Colors.TEXT,
                                            'backgroundColor' : gui.Colors.BACKGROUND,
                                            'border'          : '2px solid '+gui.Colors.TEXT,
                                            'fontSize'        : 35
                                        },
                                        style_header={'display':'none'},
                                        style_table={
                                            'overflowY':'auto',
                                            'height'   :800
                                        },
                                        cell_selectable=True,
                                        data=generateTickerTableData(),
                                        selected_cells=[{'row':0,'column':0}]
                                    )   
                                ]
                            ),
                            dash_html.Div(
                                id='ticker-details',
                                style= {
                                    'width'   : '85%',
                                    'display' : 'inline-block'
                                }
                            )
                        ])

        ])

    @mainWindow.callback(
    Output(component_id='ticker-details', component_property='children'),
    [Input(component_id='ticker-table', component_property='selected_cells'),
     Input(component_id='ticker-table', component_property='data')]
    )
    def updateTickerDetails(selected_cells,table_data):
        # find selected ticker by getting 0th index of selected rows and querying data by 'Ticker' column
        ticker = table_data[selected_cells[0]['row']]['TICKER']
        return dash_html.Div(
                style={
                    #'width': '49%',
                    #'display': 'inline-block',
                    'margin':15
                },
                children=[
                    dash_html.H2(
                        children='Overview for {}'.format(ticker),
                        style={
                            'backgroundColor': gui.Colors.BACKGROUND,
                            'textAlign'      : 'center',
                            'border'         : '2px solid '+gui.Colors.TEXT,
                            'color'          : gui.Colors.TEXT
                        }
                    ),
                    dash_html.Div(
                        style={
                            'border':'2px solid '+gui.Colors.TEXT
                        },
                        children=[createTickerHistoryGraph(ticker)]
                        )                         
                ]
            )

    return mainWindow

def generateTickerTableData():
    dividendTickers = pd.read_csv('../Resources/dividendPortfolioData.csv')['Ticker']
    return [{'TICKER':i} for i in dividendTickers]

def createTickerHistoryGraph(ticker):
    dividends = divBL.getDividendHistory(ticker)
    return dash_cc.Graph(
                        id='Graph1',
                        figure={
                            'data': [
                                {
                                 'x'   : dividends['Date'],
                                 'y'   : dividends['Dividends'],
                                 'type': 'line',
                                 'name': ticker,
                                 'mode': 'lines',
                                 'line': {
                                        'color': gui.Colors.BAD_RED,
                                        'width':3
                                         }
                                }
                                    ],
                            'layout': {
                                'plot_bgcolor' : gui.Colors.GRAPH_BACKGROUND,
                                'paper_bgcolor': gui.Colors.BACKGROUND,
                                'font'         : {'color': gui.Colors.TEXT},
                                'xaxis'        : {'gridcolor': gui.Colors.TEXT},
                                'yaxis'        : {'gridcolor': gui.Colors.TEXT},
                                'title'        :'Dividend History for {}'.format(ticker)
                                      }
                                }
                            )




def createComparisonGraph(ticker1, ticker2):
    dividends_test1 = divBL.getDividendHistory(ticker1)
    dividends_test2 = divBL.getDividendHistory(ticker2)
    return dash_html.Div(
                children=[
                            dash_cc.Graph(
                                id='Graph1',
                                figure={
                                    'data': [
                                        {'x'   : dividends_test1['Date'],
                                         'y'   : dividends_test1['Dividends'],
                                         'type': 'line',
                                         'name': ticker1,
                                         'mode': 'lines',
                                         'line': {
                                             'color': gui.Colors.BAD_RED,
                                             'width':3
                                         }
                                        },
                                        {'x': dividends_test2['Date'],
                                         'y': dividends_test2['Dividends'],
                                         'type': 'line',
                                         'name': ticker2,
                                         'mode': 'lines',
                                         'line': {
                                             'color': gui.Colors.GOOD_GREEN,
                                             'width':3
                                        }
                                         },
                                    ],
                                    'layout': {
                                        'plot_bgcolor' : gui.Colors.GRAPH_BACKGROUND,
                                        'paper_bgcolor': gui.Colors.BACKGROUND,
                                        'font'         : {'color': gui.Colors.TEXT},
                                        'xaxis'        : {'gridcolor': gui.Colors.TEXT},
                                        'yaxis'        : {'gridcolor': gui.Colors.TEXT}
                                    }
                                }
                            )
                ],
                style={
                    'width'  : '49%',
                    'display': 'inline-block',
                    'margin' : 15
                }
            )