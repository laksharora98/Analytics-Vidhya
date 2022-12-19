This is a project to learn Time Series Analysis by predicting Energy Consumption.

The .ipynb file can be opened as a jupyter notebook. The dataset should be present in the same folder as a .csv file.

In this project we do the following:

* Seasonal Decomposition to determine seasonality
* Creating training and validation splits
* Implement Triple Exponential Smoothing (Holt Winters Algorithm)
* ARIMA:
    * Determine stationarity using ADF test
    * Convert from non-stationary to stationary data using Log Transformation and Differencing
    * Determine AR and MA parameters using ACF and PACF plots
    * Implement ARIMA
* SARIMA:
    * Determine seasonal stationarity using ADF test
    * Convert from non-stationary to stationary data using Log Transformation and Seasonal Differencing
    * Determine AR and MA parameters using ACF and PACF plots
    * Implement SARIMA
* Fb Prophet - Use inbuilt cross validation function to do evaluate with same train and validate splits as before
* Compare all four models on RMSE
![image](https://user-images.githubusercontent.com/91553008/208332629-786edb10-bbde-49b3-b4df-a5b7aa9fc68b.png)
