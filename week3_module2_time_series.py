# Chinmayee Mishra Nov 26, 2022

# In this code, data for random walk model, AR(p), MA(q) and APMA(p,q) models have been generated. Given a time series data the best model selection and order estimation has been made. Especially in case of ARMA(p, q) model, PACF is used to determine the value of 'p' and 'q'. 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf

# Time series models
def time_series_model(model, parameters):
    c, theta, sigmat = parameters
    rt = np.zeros(dimension)
    if model == "rw":
        rt = c[0] + sigmat * zt
    elif model == "ar2":
        for i in np.arange(2, timesteps):
            rt[i] = c[0] + c[1] * rt[i - 1] + c[2] * rt[i - 2] + sigmat * zt[i]
    elif model == "ma2":
        for i in np.arange(2, timesteps):
            rt[i] = c[0] + sigmat * zt[i] + theta[0] * zt[i - 1] + theta[1] * zt[i - 2]
    elif model == "arma22":
        for i in np.arange(2, timesteps):
            rt[i] = c[0] + c[1] * rt[i - 1] + c[2] * rt[i - 2] + sigmat * zt[i] + theta[0] * zt[i - 1] + theta[1] * zt[i - 2]

    return np.cumsum(rt, axis = 0)

timesteps = 1000
instances = 1
dimension = (timesteps, instances)
zt = np.random.normal(0, 1, dimension)
sigmat = 0.2

# Generate a random walk instance
rw_parameters = (np.array([0, 0, 0]), np.array([0, 0]), sigmat)
# Generate ar2
ar2_parameters = (np.array([0, 0.4, -0.3]), np.array([0.2, -0.5]), sigmat)
time_series = time_series_model("arma22", rw_parameters)

# Plot the data
plt.title("Time Series Model")
plt.xlabel("time")
plt.ylabel("returns")
plt.plot(np.arange(timesteps), time_series)

# Next step is to evaluate the auto-correlation and PACF for the generated data. ACF basically gives the correlation between a time-lagged value (say, between t and t+h) where the intermediate values ocurring during the interval 'h' is ignored. PACF evaluates a conditional correlation such that the intermediate values which may have an effect on the correlation between the extreme points of 'h' interval are taken care of. 
# Note that for the plot_acf/plot_pacf functions, the argument has to be a 1D array i.e., instances should be initiated to 1.
plot_acf(time_series)
plot_pacf(time_series)
plt.show()

# We shall import a time series data and do the same analysis as before.
url='https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
df = pd.read_csv(url,sep=",")
opsd = df['Consumption']
plt.plot(opsd)
plot_acf(opsd)
plot_pacf(opsd)
plt.show()
# From the plot it is clear that this is a particularly correlated data. 