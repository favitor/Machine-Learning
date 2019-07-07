import csv
import numpy as np 
from sklearn.svm import SRV
import matplotlib.pyplot as plt 

dates = []
prices = []

def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0]))
			prices.append(float(row[1]))
	return
	
def predict_prices(dates, prices, x):
	dates = np.reshape(dates,(len(dates), 1))

	svr_lin = SRV(kernel= 'linear', C=1e3)
	svr_poly = SRV(kernel= 'poly', C=1e3, degree=2)
	svr_rbf = SRV(kernel= 'rbf', C=1e3, gamma=0.1)
	svr_lin.fit(dates, prices)
	svr_poly.fit(dates, prices)
	svr_rbf.fit(dates, prices)

	plt.scatter(dates, prices, color='black', label='Data')
	plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
	plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
	plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
	plt.xlabel("Date")
	plt.ylabel("Price")
	plt.title("SVR")
	plt.legend()
	plt.show()

	return srv_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('AAPL.csv')

predicted_price = predict_prices(dates, price, 29

print(predicted_price)	