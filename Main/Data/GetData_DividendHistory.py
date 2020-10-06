#!/usr/bin/env python3

import yfinance as yf
import pandas as pd

"""
    Downloads all dividend history data for each ticker in the dividend portfolio (from dividendPortfolioData.csv), saves it in an individual .csv file
"""

def main():
    dividendStocks = pd.read_csv('../../Resources/dividendPortfolioData.csv')['Ticker']

    for ticker in dividendStocks:
    	print('Downloading Dividend History for {}'.format(ticker))
        dividends_ser = yf.Ticker(ticker).dividends
        dividends_df = pd.Series.to_frame(dividends_ser)
        dividends_df.to_csv('../../Resources/OutputFiles/Dividends/{}_dividends.csv'.format(ticker))
    	print('Finished Downloading Dividend History for {} to {}'.format(ticker,ticker+'_dividends.csv'))
    return

if __name__ == '__main__':
    main()
