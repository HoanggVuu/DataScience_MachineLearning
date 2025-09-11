'''
Draw basic plots using DataFrame.plot() method or DataFrame.plot.<plotting_method>().

##########################

1. Histogram: 
   + df.plot(kind = "hist") 
   + df.plot.hist()

2. Density/KDE plot: 
   + df.plot(kind = "density"/"kde")
   + df.plot.density()
   + df.plot.kde()

3. Box plot: 
   + df.plot(kind = "box")
   + df.plot.box()

4. Pie chart: 
   + df.plot(kind = "pie")
   + df.plot.pie()

5. Bar plot: 
   + df.plot(kind = "bar")
   + df.plot.bar()

6. Barh plot (horizontal): 
   + df.plot(kind = "barh")
   + df.plot.barh()

7. Scatter plot: 
   + df.plot(kind = "scatter", x = <x_column>, y = <y_column>), 
   + df.plot.scatter(x = <x_column>, y = <y_column>)

8. Line plot: 
   + df.plot(kinde = "line")
   + df.plot()
   + df.plot.line()

9. Area plot: 
   + df.plot(kind = "area")
   + df.plot.area()

10. Hexbin plot: 
    + df.plot(kind = "hexbin", x = <x_column>, y = <y_column>, gridsize = <size>)
    + df.plot.hexbin(x = <x_column>, y = <y_column>, gridsize = <size>)
'''

import pandas as pd
import matplotlib.pyplot as plt

df_pokemon = (
    pd.read_csv(
        filepath_or_buffer = "05_Pandas_DataR_dataframe/data/pokemon.csv",
        dtype = {
            "Type 1": "category",
            "Type 2": "category",
            "Generation": "category",
            "Legendary": "bool"
        }
    )
    .drop(columns = ["#"])
    .pipe(lambda df: df.set_axis(df.columns.str.strip().str.replace(r"\s+", "_", regex = True).str.replace(".", ""), axis=1))
    .assign(Generation = lambda df: df['Generation'].cat.as_ordered())
)

print(df_pokemon.info())
# RangeIndex: 800 entries, 0 to 799
# Data columns (total 12 columns):
#  #   Column      Non-Null Count  Dtype   
# ---  ------      --------------  -----   
#  0   Name        800 non-null    object  
#  1   Type_1      800 non-null    category
#  2   Type_2      414 non-null    category
#  3   Total       800 non-null    int64   
#  4   HP          800 non-null    int64   
#  5   Attack      800 non-null    int64   
#  6   Defense     800 non-null    int64   
#  7   Sp_Atk      800 non-null    int64   
#  8   Sp_Def      800 non-null    int64   
#  9   Speed       800 non-null    int64   
#  10  Generation  800 non-null    category
#  11  Legendary   800 non-null    bool    
# dtypes: bool(1), category(3), int64(7), object(1)
# memory usage: 54.7+ KB