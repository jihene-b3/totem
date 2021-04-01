import predicton as pr 
from predicton.io.Load_db import Load_db 
from predicton.Data import adapt_to_fbp,format_data
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from download import download 
import warnings 
from fbprophet import Prophet
import datetime as dt 

#%%
# Import data 
#df = pr.Load_db().save_as_df()

df = pr.Load_db().save_as_df()

#%% pretreatment 
df = pr.format_data(df)
#%%
df = pr.adapt_to_fbp(df)
#%%Train 
m = Prophet(interval_width=0.95)
model = m.fit(df)
#%%Forcast Away
future = m.make_future_dataframe(periods=10, freq='D')
forecast = m.predict(future)
forecast.tail()

#%%Plot
plot1=m.plot(forecast)