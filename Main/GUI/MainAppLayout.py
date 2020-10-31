import dash
import dash_core_components as dash_cc
import dash_html_components as dash_html
from dash.dependencies import Input, Output
import BL.DividendsBL as divBL
import GUI.GUICentral as gui
import plotly.graph_objs as go
import pandas as pd

def build():
    mainWindow = dash.Dash()
    
    mainWindow.layout = dash_html.Div(
        style={
            'backgroundColor': gui.Colors.BACKGROUND,
            'align-items':'center'
        },
        children=[
            #title
                dash_html.H1(
                    children='Dividends Graph Test',
                    style={
                        'textAlign': 'center',
                        'color': gui.Colors.TEXT
                    }
                ),
            #subtitle
                dash_html.Div(  
                                children='Select a Ticker from the Dropdown',
                                style={
                                  #'width': '49%',
                                  #'display': 'inline-block',
                                  'textAlign': 'center',
                                  'color': gui.Colors.TEXT
                              }),
                # Ticker Dropdown
                dash_html.Div(
                            style={'align-items':'center',
                                    'justify-content':'center'},
                            children=[
                            dash_cc.Dropdown(
                                id='ticker-dropdown',
                                style={'width':'30%'},
                                options=generateDropdownOptions(),
                                value=generateDropdownOptions()[0]['value']
                                )
                            ]),
                dash_html.Div(
                            id='ticker-details',
                            style= {
                                    #'width': '49%',
                                    #'display': 'inline-block',
                                    'margin':15
                                }
                            )
            #graph
            #createComparisonGraph(ticker1,ticker2)

        ])

    @mainWindow.callback(
    Output(component_id='ticker-details', component_property='children'),
    [Input(component_id='ticker-dropdown', component_property='value')]
    )
    def updateTickerDetails(input_value):
        ticker = input_value
        return dash_html.Div(
                style={
                    #'width': '49%',
                    #'display': 'inline-block',
                    #'border':'2px solid '+gui.Colors.TEXT,
                    'margin':15
                },
                children=[
                    dash_html.H2(
                        children='Overview for {}'.format(ticker),
                        style={
                            'textAlign': 'center',
                            'color': gui.Colors.TEXT
                        }
                    ),
                    createTickerHistoryGraph(ticker)                         
                ]
            )

    return mainWindow

def generateDropdownOptions():
    dividendTickers = pd.read_csv('../Resources/dividendPortfolioData.csv')['Ticker']
    options = []
    for ticker in dividendTickers:
        options.append({'label':ticker,'value':ticker})
    return options

def createTickerHistoryGraph(ticker):
    dividends = divBL.getDividendHistory(ticker)
    return dash_cc.Graph(
                                id='Graph1',
                                figure={
                                    'data': [
                                        {'x': dividends['Date'],
                                         'y': dividends['Dividends'],
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
                                        'plot_bgcolor': gui.Colors.GRAPH_BACKGROUND,
                                        'paper_bgcolor': gui.Colors.BACKGROUND,
                                        'font': {
                                        'color': gui.Colors.TEXT
                                        },
                                        'xaxis': {
                                            'gridcolor': gui.Colors.TEXT
                                        },
                                        'yaxis': {
                                            'gridcolor': gui.Colors.TEXT
                                        }
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
                                        {'x': dividends_test1['Date'],
                                         'y': dividends_test1['Dividends'],
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
                                        'plot_bgcolor': gui.Colors.GRAPH_BACKGROUND,
                                        'paper_bgcolor': gui.Colors.BACKGROUND,
                                        'font': {
                                        'color': gui.Colors.TEXT
                                        },
                                        'xaxis': {
                                            'gridcolor': gui.Colors.TEXT
                                        },
                                        'yaxis': {
                                            'gridcolor': gui.Colors.TEXT
                                        }
                                    }
                                }
                            )
                ],
                style={
                    'width': '49%',
                    'display': 'inline-block',
                    #'border':'2px solid '+gui.Colors.TEXT,
                    'margin':15
                }
            )