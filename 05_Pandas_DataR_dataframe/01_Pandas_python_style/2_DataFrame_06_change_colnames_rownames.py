'''
1. Changing Column Names:
   + df = df.reindex(columns=new_names)
   + df.columns = new_list
   + df.columns = df.columns.str.replace(' ', '_')
   + df.columns = df.columns.apply(str.upper)
   + df.columns = [f'col_{i}' for i in range(df.shape[1])]
   + df.rename(columns={'old_name': 'new_name'}, inplace=False)
   + df.rename(columns=lambda x: x.strip().lower())
   + df.rename_axis('features', axis=1, inplace=False)
   + df.set_axis(new_list, axis=1, inplace=False)
   + df.add_prefix('pre_')
   + df.add_suffix('_suf')
   + df.rename(columns={'old1':'new1'}, level=0, inplace=False) # for MultiIndex

2. Changing Row Names (Index):
   + df = df.set_index('col_name') ||set an existed column as index||
   + df = df.reindex(new_index_list)
   + df.index = new_list
   + df.index = df.index.str.replace(' ', '_')
   + df.index = df.index.apply(str.upper)
   + df.reset_index(drop=True, inplace=False)
   + df.reindex(new_list, inplace=False)
   + df.rename(index={'old_name': 'new_name'}, inplace=False)
   + df.rename_axis('samples', inplace=False)
   + df.set_axis(new_list, axis=0, inplace=False)
   + df.rename(index={'old1':'new1'}, level=0, inplace=False) # for MultiIndex
'''

import pandas as pd

df_lifexp = pd.read_csv("05_Pandas_DataR_dataframe/data/life_expectancy.csv")
print(df_lifexp.dtypes)
# Country                             object
# Year                                 int64
# Status                              object
# Life expectancy                    float64
# Adult Mortality                    float64
# infant deaths                        int64
# Alcohol                            float64
# percentage expenditure             float64
# Hepatitis B                        float64
# Measles                              int64
#  BMI                               float64
# under-five deaths                    int64
# Polio                              float64
# Total expenditure                  float64
# Diphtheria                         float64
#  HIV/AIDS                          float64
# GDP                                float64
# Population                         float64
#  thinness  1-19 years              float64
#  thinness 5-9 years                float64
# Income composition of resources    float64
# Schooling                          float64

df_emp = pd.read_csv("05_Pandas_DataR_dataframe/data/emp.csv")
print(df_emp.dtypes)
# id              int64
# name           object
# salary        float64
# start_date     object
# dept           object