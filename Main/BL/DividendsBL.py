import os.path
import pandas as pd
import yfinance as yf

DIVIDENDS_CSV_PATH = 'C:\\Users\\Jaden\\PycharmProjects\\PortfolioUpkeep\\OutputFiles\\Dividends\\'

def getDividendHistory(ticker: str):
    """ Gets the dividend history of a given ticker

        Checks to see if the info is already downloaded in the /OutputFiles/Dividends directory, if
    it doesn't find it, downloads it manually (slow).

    :param ticker: (str) NYSE stock ticker
    :return: pandas DataFrame of dividends and dates the dividend was paid out for the given stock
    """

    if(os.path.exists(DIVIDENDS_CSV_PATH+ticker+'_dividends.csv')):
        return pd.read_csv(DIVIDENDS_CSV_PATH+ticker+'_dividends.csv')

    else:
        dividends_ser = yf.Ticker(ticker).dividends
        return pd.Series.to_frame(dividends_ser)