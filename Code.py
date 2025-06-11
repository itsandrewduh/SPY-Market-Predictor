#Importing SPY data
pip install yfinance
import yfinance as yf
df = yf.download('SPY')
#Getting SPY data
def get_data():
  df = yf.download(TICKER)
  df.columns = df.columns.get_level_values(0)
  TICKER = 'SPY'
  FAST = 10
  SLOW = 27
  LOOKBACK = 10000
