import numpy as np
import pandas as pd
import quandl
import datetime
#import matplotlib.pyplot as plt

# Set start and end date for stock prices
start_date = datetime.date(2009, 3,8)
end_date = datetime.date.today()
# data = quandl.get('FSE/SAP_X', start_date=start_date, end_date=end_date)# Load data from Quandl
# data.to_csv('stock_market.csv')# Save data to CSV file
df=pd.read_csv("stock_market.csv")
#df = pd.DataFrame(data, columns=['Close'])# Create a new DataFrame with only closing price and date
df = df.reset_index()# Reset index column so that we have integers to represent time 
import matplotlib.dates as mdates
years = mdates.YearLocator() # Get every year
yearsFmt = mdates.DateFormatter('%Y') # Set year format
from sklearn.model_selection import train_test_split
train, test = train_test_split(df, test_size=0.20,random_state=0)
X_train = np.array(train.index).reshape(-1, 1)
y_train = train['Close']

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
X_test = np.array(test.index).reshape(-1, 1)
y_test = test['Close']

# Generate array with predicted values
y_pred = model.predict(X_test)
import pickle
with open("model.pkl","wb") as f:
    p=pickle.dump(model,f)
    f.close()
with open("model.pkl","rb") as f:
    p=pickle.load(f)
    f.close()
print("predicted stock market price of year are:",p.predict([[2901]]))
print("predicted stock market price of year are:",model.predict([[2052]]))

