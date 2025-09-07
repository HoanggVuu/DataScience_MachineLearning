'''
1. Detect missing values:
  + df.isna() or df.isnull(): Returns a DataFrame of the same shape as df, with True for missing values
  + df.isna().sum() or df.isnull().sum(): Returns the count of missing values in each column
  + df.info(): Provides a summary of the DataFrame, including non-null counts

2. Detect non-missing values:
  + df.notna() or df.notnull(): Returns a DataFrame of the same shape as df, with True for non-missing values
  + df.notna().sum() or df.notnull().sum(): Returns the count of non-missing values in each column

3. Drop missing values:
  + df.dropna(): Returns a DataFrame with rows containing any missing values removed
  + df.dropna(axis=...)
  + df.dropna(how=...)
  + df.dropna(thresh=...)
  + df.dropna(subset=...)

4. Fill missing values:
  + df.fillna(value): Returns a DataFrame with missing values filled with the specified value
  + df.fillna({dictionary}): Fill different columns with different values
  + df.fillna(df.mean()): Fill missing values with the mean of each column
  + df.fillna(method=..., limit=...): Fill missing values using a specified method (e.g., 'ffill', 'bfill')

5. Interpolate missing values:
  + df.interpolate(axis=...): linear interpolation
  + df.interpolate(method = "polynomial", order = n): polynomial interpolation of order n
  + df.interpolate(method = "spline", order = n): spline interpolation of order n
  + df.interpolate(method = "time"): time-based interpolation (requires a datetime index)
  + df.interpolate(method = "nearest"): nearest neighbor interpolation

6. Conditional filling: df['C'] = np.where(df['C'].isna(), df['A'] + df['B'], df['C'])

7. Group-based filling, transform
  + df_grouped = df.groupby('category').transform(lambda x: x.fillna(x.mean()))
'''

import pandas as pd
import numpy as np

df_mkt = (
    pd.read_csv(
        filepath_or_buffer = "05_Pandas_DataR_dataframe/data/marketing_data.csv",
        dtype = {"week": "category", "Year": "category"}
    )
    .pipe(
        lambda df: df.set_axis(
            df.columns.str.lower().str.strip().str.replace(r"[^a-zA-Z]", "_", regex = True), 
            axis = 1
        )
    )
)

print(df_mkt.info())
# RangeIndex: 156 entries, 0 to 155
# Data columns (total 26 columns):
#  #   Column                     Non-Null Count  Dtype   
# ---  ------                     --------------  -----   
#  0   week                       156 non-null    category
#  1   year                       156 non-null    category
#  2   market_share               156 non-null    float64 
#  3   av_price_per_kg            156 non-null    float64 
#  4   non_promo_price_per_kg     156 non-null    float64 
#  5   promo_vol_share            156 non-null    float64 
#  6   total_weigh                156 non-null    int64   
#  7   share_of_ean_weigh         156 non-null    float64 
#  8   avg_price_vs_plb           156 non-null    float64 
#  9   non_promo_price_vs_plb     156 non-null    float64 
#  10  promo_vol_sh_index_vs_plb  156 non-null    float64 
#  11  total_cm_shelf             156 non-null    float64 
#  12  shelf_share                156 non-null    float64 
#  13  top_of_mind                123 non-null    float64 
#  14  spontaneous                123 non-null    float64 
#  15  aided                      123 non-null    float64 
#  16  penetration                123 non-null    float64 
#  17  competitor                 111 non-null    float64 
#  18  grp_radio                  14 non-null     float64 
#  19  reach_radio                14 non-null     float64 
#  20  grp_tv                     52 non-null     float64 
#  21  reach_tv                   52 non-null     float64 
#  22  reach_cinema               18 non-null     float64 
#  23  grp_outdoor                1 non-null      float64 
#  24  grp_print                  22 non-null     float64 
#  25  share_of_spend             116 non-null    float64 
# dtypes: category(2), float64(23), int64(1)
# memory usage: 32.2 KB


#--------------------------------------------------------------------------------------------------------------#
#---------------------------------------- 1. Detect missing values --------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#

##############################
## df.isna() or df.isnull() ##
##############################
'''Returns a DataFrame of the same shape as df, with True for missing values'''

print(df_mkt.isna().head())
#     week   year  market_share  av_price_per_kg  ...  reach_cinema  grp_outdoor  grp_print  share_of_spend
# 0  False  False         False            False  ...          True         True       True            True
# 1  False  False         False            False  ...          True         True       True            True
# 2  False  False         False            False  ...          True         True       True            True
# 3  False  False         False            False  ...          True         True       True            True
# 4  False  False         False            False  ...          True         True       True            True

print(df_mkt.isnull().head())
#     week   year  market_share  av_price_per_kg  ...  reach_cinema  grp_outdoor  grp_print  share_of_spend
# 0  False  False         False            False  ...          True         True       True            True
# 1  False  False         False            False  ...          True         True       True            True
# 2  False  False         False            False  ...          True         True       True            True
# 3  False  False         False            False  ...          True         True       True            True
# 4  False  False         False            False  ...          True         True       True            True

##########################################
## df.isna().sum() or df.isnull().sum() ##
##########################################
'''Returns the count of missing values in each column'''

print(df_mkt.isna().sum())
# week                           0
# year                           0
# market_share                   0
# av_price_per_kg                0
# non_promo_price_per_kg         0
# promo_vol_share                0
# total_weigh                    0
# share_of_ean_weigh             0
# avg_price_vs_plb               0
# non_promo_price_vs_plb         0
# promo_vol_sh_index_vs_plb      0
# total_cm_shelf                 0
# shelf_share                    0
# top_of_mind                   33
# spontaneous                   33
# aided                         33
# penetration                   33
# competitor                    45
# grp_radio                    142
# reach_radio                  142
# grp_tv                       104
# reach_tv                     104
# reach_cinema                 138
# grp_outdoor                  155
# grp_print                    134
# share_of_spend                40
# dtype: int64

print(df_mkt.isnull().sum())
# week                           0
# year                           0
# market_share                   0
# av_price_per_kg                0
# non_promo_price_per_kg         0
# promo_vol_share                0
# total_weigh                    0
# share_of_ean_weigh             0
# avg_price_vs_plb               0
# non_promo_price_vs_plb         0
# promo_vol_sh_index_vs_plb      0
# total_cm_shelf                 0
# shelf_share                    0
# top_of_mind                   33
# spontaneous                   33
# aided                         33
# penetration                   33
# competitor                    45
# grp_radio                    142
# reach_radio                  142
# grp_tv                       104
# reach_tv                     104
# reach_cinema                 138
# grp_outdoor                  155
# grp_print                    134
# share_of_spend                40
# dtype: int64

###############
## df.info() ##
###############
'''Provides a summary of the DataFrame, including non-null counts'''

print(df_mkt.info())
# RangeIndex: 156 entries, 0 to 155
# Data columns (total 26 columns):
#  #   Column                     Non-Null Count  Dtype   
# ---  ------                     --------------  -----   
#  0   week                       156 non-null    category
#  1   year                       156 non-null    category
#  2   market_share               156 non-null    float64 
#  3   av_price_per_kg            156 non-null    float64 
#  4   non_promo_price_per_kg     156 non-null    float64 
#  5   promo_vol_share            156 non-null    float64 
#  6   total_weigh                156 non-null    int64   
#  7   share_of_ean_weigh         156 non-null    float64 
#  8   avg_price_vs_plb           156 non-null    float64 
#  9   non_promo_price_vs_plb     156 non-null    float64 
#  10  promo_vol_sh_index_vs_plb  156 non-null    float64 
#  11  total_cm_shelf             156 non-null    float64 
#  12  shelf_share                156 non-null    float64 
#  13  top_of_mind                123 non-null    float64 
#  14  spontaneous                123 non-null    float64 
#  15  aided                      123 non-null    float64 
#  16  penetration                123 non-null    float64 
#  17  competitor                 111 non-null    float64 
#  18  grp_radio                  14 non-null     float64 
#  19  reach_radio                14 non-null     float64 
#  20  grp_tv                     52 non-null     float64 
#  21  reach_tv                   52 non-null     float64 
#  22  reach_cinema               18 non-null     float64 
#  23  grp_outdoor                1 non-null      float64 
#  24  grp_print                  22 non-null     float64 
#  25  share_of_spend             116 non-null    float64 
# dtypes: category(2), float64(23), int64(1)
# memory usage: 32.2 KB


#--------------------------------------------------------------------------------------------------------------#
#-------------------------------------- 2. Detect non-missing values ------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#

#################################
## df.notna() or df.notnull()  ##
#################################
'''Returns a DataFrame of the same shape as df, with True for non-missing values'''

print(df_mkt.notna().head())
#    week  year  market_share  av_price_per_kg  ...  reach_cinema  grp_outdoor  grp_print  share_of_spend
# 0  True  True          True             True  ...         False        False      False           False
# 1  True  True          True             True  ...         False        False      False           False
# 2  True  True          True             True  ...         False        False      False           False
# 3  True  True          True             True  ...         False        False      False           False
# 4  True  True          True             True  ...         False        False      False           False

print(df_mkt.notnull().head())
#    week  year  market_share  av_price_per_kg  ...  reach_cinema  grp_outdoor  grp_print  share_of_spend
# 0  True  True          True             True  ...         False        False      False           False
# 1  True  True          True             True  ...         False        False      False           False
# 2  True  True          True             True  ...         False        False      False           False
# 3  True  True          True             True  ...         False        False      False           False
# 4  True  True          True             True  ...         False        False      False           False

############################################
## df.notna().sum() or df.notnull().sum() ##
############################################
'''Returns the count of non-missing values in each column'''

print(df_mkt.notna().sum())
# week                         156
# year                         156
# market_share                 156
# av_price_per_kg              156
# non_promo_price_per_kg       156
# promo_vol_share              156
# total_weigh                  156
# share_of_ean_weigh           156
# avg_price_vs_plb             156
# non_promo_price_vs_plb       156
# promo_vol_sh_index_vs_plb    156
# total_cm_shelf               156
# shelf_share                  156
# top_of_mind                  123
# spontaneous                  123
# aided                        123
# penetration                  123
# competitor                   111
# grp_radio                     14
# reach_radio                   14
# grp_tv                        52
# reach_tv                      52
# reach_cinema                  18
# grp_outdoor                    1
# grp_print                     22
# share_of_spend               116
# dtype: int64

print(df_mkt.notnull().sum())
# week                         156
# year                         156
# market_share                 156
# av_price_per_kg              156
# non_promo_price_per_kg       156
# promo_vol_share              156
# total_weigh                  156
# share_of_ean_weigh           156
# avg_price_vs_plb             156
# non_promo_price_vs_plb       156
# promo_vol_sh_index_vs_plb    156
# total_cm_shelf               156
# shelf_share                  156
# top_of_mind                  123
# spontaneous                  123
# aided                        123
# penetration                  123
# competitor                   111
# grp_radio                     14
# reach_radio                   14
# grp_tv                        52
# reach_tv                      52
# reach_cinema                  18
# grp_outdoor                    1
# grp_print                     22
# share_of_spend               116
# dtype: int64