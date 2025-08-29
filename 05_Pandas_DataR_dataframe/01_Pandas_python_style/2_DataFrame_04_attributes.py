'''
Flow of contents:

1. Shape and Size attributes:
   + df.shape: Returns a tuple (rows, columns)
   + df.size: Returns total number of elements (rows * columns)
   + df.ndim: Returns number of dimensions (always 2 for DataFrame)

2. Data types and Structure attributes:
   + df.dtypes: Returns data types of each column
   + df.columns: Returns column labels
   + df.index: Returns row labels
   + df.axes: Returns a list of both row and column labels

3. Data Access attributes:
   + df.values: Returns the underlying numpy array of the DataFrame
   + df.T: Returns the transpose of the DataFrame
   + df.empty: Returns True if DataFrame is empty, else False

4. Advanced attributes:
   + df.attrs: Dictionary for storing custom metadata
   + df.style: Returns a Styler object for HTML/CSS formatting
   + df.flags: Configuration object controlling DataFrame behavior. 
'''

import pandas as pd

df_baseball = pd.read_csv(
    filepath_or_buffer = "05_Pandas_DataR_dataframe/data/baseball.csv",
    dtype = {"Team": "category", "Position": "category", "PosCategory": "category"}
)

df_baseball.head()
#               Name Team       Position  Height  Weight    Age PosCategory
# 0    Adam_Donachie  BAL        Catcher      74     180  22.99     Catcher
# 1        Paul_Bako  BAL        Catcher      74     215  34.69     Catcher
# 2  Ramon_Hernandez  BAL        Catcher      72     210  30.78     Catcher
# 3     Kevin_Millar  BAL  First_Baseman      72     210  35.43   Infielder
# 4      Chris_Gomez  BAL  First_Baseman      73     188  35.71   Infielder

df_baseball.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1015 entries, 0 to 1014
# Data columns (total 7 columns):
#  #   Column       Non-Null Count  Dtype   
# ---  ------       --------------  -----   
#  0   Name         1015 non-null   object  
#  1   Team         1015 non-null   category
#  2   Position     1015 non-null   category
#  3   Height       1015 non-null   int64   
#  4   Weight       1015 non-null   int64   
#  5   Age          1015 non-null   float64 
#  6   PosCategory  1015 non-null   category
# dtypes: category(3), float64(1), int64(2), object(1)
# memory usage: 36.5+ KB

'''
Here, if leave the "Team", "Position", "PosCategory" columns as "object" type, 
the memory usage will be 55.6+ KB.
'''


#------------------------------------------------------------------------------------------------------#
#------------------------------------ 1. Shape and Size attributes ------------------------------------#
#------------------------------------------------------------------------------------------------------#