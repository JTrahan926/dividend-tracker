import dash
import dash_core_components as dash_cc
import dash_html_components as dash_html
from dash.dependencies import Input, Output
import Main.BL.DividendsBL as divBL
import Main.GUI.GUICentral as gui
import plotly.graph_objs as go

def build():
    mainWindow = dash.Dash()
    ticker1 = 'PEP'
    ticker2 = 'KO'
    dividends_test1 = divBL.getDividendHistory(ticker1)
    dividends_test2 = divBL.getDividendHistory(ticker2)

    mainWindow.layout = dash_html.Div(
        style={
            'backgroundColor': gui.Colors.BACKGROUND,
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
                dash_html.Div(children='This graph compares dividend history of {} and {}'.format(ticker1,ticker2),
                              style={
                                  'textAlign': 'center',
                                  'color': gui.Colors.TEXT
                              }),
            #graph
                dash_html.Div(
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
                        'width':'70%',
                        #'border':'2px solid '+gui.Colors.TEXT,
                        'margin':15
                    }
                )
        ])

        # style={'backgroundColor': gui.Colors.BACKGROUND},
        #
        # children=[
        #
        #
        #     dash_html.H1(
        #         children='Dividends Graph Test',
        #         style={
        #             'textAlign': 'center',
        #             'color': gui.Colors.TEXT
        #         }
        #     ),
        #
        #
        #     dash_html.Div(children='This graph compares dividend history of {} and {}'.format(ticker1,ticker2),
        #                   style={
        #                       'textAlign': 'center',
        #                       'color': gui.Colors.TEXT
        #                   }),
        #
        #
        #     dash_html.Div(children=[
        #         dash_cc.Graph(
        #             id='Graph1',
        #             figure={
        #                 'data': [
        #                     {'x': dividends_test1['Date'],
        #                      'y': dividends_test1['Dividends'],
        #                      'type': 'line',
        #                      'name': ticker1,
        #                      'marker': {'color': gui.Colors.TEXT,
        #                                 'line': {'width': '3'}
        #                                 }
        #                      },
        #                     {'x': dividends_test2['Date'],
        #                      'y': dividends_test2['Dividends'],
        #                      'type': 'line',
        #                      'name': ticker2,
        #                      'marker': {
        #                          'size': 12,
        #                          'color': gui.Colors.GOOD_GREEN,
        #                          'line': {'weight': 50}
        #                      }
        #                      },
        #                 ],
        #                 'layout': {
        #                     'plot_bgcolor': gui.Colors.GRAPH_BACKGROUND,
        #                     'paper_bgcolor': gui.Colors.BACKGROUND,
        #                     'font': {
        #                         'color': gui.Colors.TEXT
        #                     },
        #                     'xaxis': {
        #                         'gridcolor': gui.Colors.TEXT
        #                     },
        #                     'yaxis': {
        #                         'gridcolor': gui.Colors.TEXT
        #                     }
        #                 }
        #             }
        #         )
        #
        #
        #     ]
        #     style={}])
        # )

    return mainWindow