import yfinance as yf
import pandas as pd

"""
    Downloads all dividend history data for each ticker in the dividend portfolio (from dividendPortfolioData.csv), saves it in an individual .csv file
"""

def main():
    dividendStocks = pd.read_csv(r'C:\Users\Jaden\PycharmProjects\PortfolioUpkeep\Resources\dividendPortfolioData.csv')['Ticker']

    for ticker in dividendStocks:
        dividends_ser = yf.Ticker(ticker).dividends
        dividends_df = pd.Series.to_frame(dividends_ser)
        dividends_df.to_csv(r'C:\Users\Jaden\PycharmProjects\PortfolioUpkeep\OutputFiles\Dividends\{}_dividends.csv'.format(ticker))
    return

if __name__ == '__main__':
    main()
