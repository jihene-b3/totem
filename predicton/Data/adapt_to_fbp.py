import pandas as pd 
import datetime as dt 
import predicto.Data.format_data
 
def adapt_to_fbp(df_totem):
    """
    Function adjusts Dataset to Prophet's requirments. 
    
    """ 
    df_totem.drop(columns=['Month','Year', 'hour','Day_Of_Week','Day_Of_Year','Day','weekday','minute','DateTime','Date'], inplace=True)
    df_totem.columns =['y','ds']
    df_totem = df_totem.astype({"y": int})
    df_totem['ds'] = pd.to_datetime(df_totem['DateTime'])
    return df_totem