#from crypt import methods
from flask import Flask,request, url_for, redirect, render_template
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import quandl
import datetime
import numpy as np
app = Flask(__name__)

log_reg=pickle.load(open('model.pkl','rb'))
app.config['SERVER_NAME']="192.168.192.122:5000"
@app.route('/')
def hello_world():
    return render_template("spam_detect.html")

@app.route('/predict/<int:string>',methods=['POST','GET'])
def predict(string):
    start_date = datetime.date(2009, 3,8)
    end_date = datetime.date.today()
    data = quandl.get('FSE/SAP_X', start_date=start_date, end_date=end_date)# Load data from Quandl
    data.to_csv('stock_market.csv')# Save data to CSV file
    df = pd.DataFrame(data, columns=['Close'])# Create a new DataFrame with only closing price and date
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
    print("predicted stock market price of year are:",model.predict([[2020]]))
    print("predicted stock market price of year are:",model.predict([[2052]]))
    a=model.predict([[string]])
    return "the predicted value is "+str(a[0])

if __name__=='__main__':
    predict(3001)
    app.run(debug=True)