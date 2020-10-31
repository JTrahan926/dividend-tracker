import os.path
import pandas as pd
import yfinance as yf

def getDividendHistory(ticker: str):
    """ Gets the dividend history of a given ticker from yfinance

    :param ticker: (str) NYSE stock ticker
    :return: pandas DataFrame of dividends and dates the dividend was paid out for the given stock
    """

    dividends_ser = yf.Ticker(ticker).dividends
    df = pd.DataFrame(dividends_ser).reset_index()
    df.columns = ['Date','Dividends']
    return df