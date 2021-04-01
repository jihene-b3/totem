import pandas as pd
from download import download
from predicton.io import url,path_target

class Load_db:
  def __init__(self, url=url, target_name=path_target):
    download(url, target_name, replace=False)
  
  @staticmethod
  def save_as_df():
    df_totem = pd.read_csv(path_target, na_values="", low_memory=False)
    return df_totem