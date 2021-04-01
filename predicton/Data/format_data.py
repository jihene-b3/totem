import pandas as pd 
import numpy as np 
# by adding cropped date with day, mont, year, hour, minute
def format_data(df_totem):
   """
   Change the format of the DateTime and cleans data.
   
   """  
   df_totem = df_totem.sort_index(ascending=True)
     
   df_totem.rename(columns={'Date': 'DateTime','''Vélos ce jour / Today's total''': 'Day_Total','Vélos depuis le 1er janvier / Grand total':'Grand Total', 'Heure / Time':'Time'}, inplace=True)

   df_totem['Heure / Time'] = df_totem['Heure / Time'].replace('', np.nan)
   df_totem.dropna(subset=['Heure / Time'], inplace=True)
   df_totem["Date"] = pd.to_datetime(df_totem["Date"].astype(str)+ ' ' + df_totem['Heure / Time'].astype(str), format="%d/%m/%Y %H:%M:%S", errors='coerce')
   df_totem.rename(columns={'Date': 'DateTime','''Vélos ce jour / Today's total''': 'Day_Total','Vélos depuis le 1er janvier / Grand total':'Grand Total', 'Heure / Time':'Time'}, inplace=True)
   #df_totem['Heure / Time'] = df_totem['Heure / Time'].astype('str')   
   df_totem['Day_Of_Week'] = df_totem.DateTime.dt.dayofweek
   df_totem['Day_Of_Year'] = df_totem.DateTime.dt.dayofyear
   df_totem["Day"] = pd.DatetimeIndex(df_totem["DateTime"]).day
   df_totem["weekday"] =  df_totem["DateTime"].dt.day_name()
   df_totem['Month'] = df_totem.DateTime.dt.month
   df_totem['Year'] = df_totem.DateTime.dt.year
   df_totem["hour"] = df_totem.Date.dt.hour
   df_totem["minute"] = df_totem.Date.dt.minute
   
   df_totem.drop(columns=['Grand total','Heure / Time','Unnamed: 4','Remarque'], inplace=True)
   #df_totem = df_totem.set_index(['DateTime'])
   return df_totem