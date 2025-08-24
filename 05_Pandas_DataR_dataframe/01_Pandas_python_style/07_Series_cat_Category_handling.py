'''
pd.Series.cat is an accessor object for categorical properties of the Series values.

When converted to the 'category' dtype, the memory usage of the Series is reduced (upto 90% less memory), 
and operations on the Series can be performed more efficiently.


Flow of contents:
0. Creat a Categorical Series
1. Core attributes: .cat.categories, .cat.codes, .cat.ordered
2. Adding and Removing: .cat.add_categories(), 
                        .cat.remove_categories(), .cat.remove_unused_categories(), 
                        .cat.set_categories()
3. Renaming: .cat.rename_categories()
4. Reordering: .cat.reorder_categories()
5. Ordered categories: .cat.as_ordered() (Support meaningful min(), max(), and sorting operations)
6. Unordered categories: .cat.as_unordered() (Treat categories as nominal with no inherent order)
'''

import pandas as pd
import numpy as np

