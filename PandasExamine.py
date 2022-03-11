import numpy as np
import pandas as pd
from colorama import Fore

def ExaminePandasEx0(dfs):
  stores_df = pd.read_csv('./store-sales/stores.csv')
  sales_df = pd.read_csv('./store-sales/daily_sales.csv')
  result = stores_df.equals(dfs[0]) and sales_df.equals(dfs[1])
  if result:
    print(Fore.GREEN + 'SUCCESS!')
  else:
    print(Fore.RED + 'WRONG OUTPUT!')

def ExaminePandasEx1_1(df):
  sales_df = pd.read_csv('./store-sales/daily_sales.csv')
  sales_df_meats = sales_df[sales_df['family']=='MEATS']
  result = sales_df_meats.equals(df)
  if result:
    print(Fore.GREEN + 'SUCCESS!')
  else:
    print(Fore.RED + 'WRONG OUTPUT!')

def ExaminePandasEx1_2(df):
  sales_df = pd.read_csv('./store-sales/daily_sales.csv')
  sales_df_meats_max = sales_df[sales_df['family']=='MEATS'].groupby('store_nbr')['onpromotion'].max().reset_index()
  result = sales_df_meats_max.equals(df.reset_index()) or sales_df_meats_max.equals(df)
  if result:
    print(Fore.GREEN + 'SUCCESS!')
  else:
    print(Fore.RED + 'WRONG OUTPUT!')

def ExaminePandasEx2(df):
  stores_df = pd.read_csv('./store-sales/stores.csv')
  sales_df = pd.read_csv('./store-sales/daily_sales.csv')
  sales_df_2016 = sales_df[sales_df['year']==2016]
  sales_df_2016_extend = pd.merge(sales_df_2016, stores_df, how='inner', on='store_nbr')
  by_city_n_family = sales_df_2016_extend.groupby(['city'])['sales'].sum().reset_index()
  by_city_n_family_sorted = by_city_n_family.sort_values(by='sales', ascending=False).reset_index(drop=True)

  result = by_city_n_family_sorted.equals(df)
  if result:
    print(Fore.GREEN + 'SUCCESS!')
  else:
    print(Fore.RED + 'WRONG OUTPUT!')