'''
The Series.sparse accessor in pandas provides specialized functionality 
for working with sparse data structures.

Sparse Series are designed to efficiently store data 
where a significant portion of values are identical (typically zeros or NaN), 
offering substantial memory savings for such datasets.

###############################

Flow of contents:

0. Create a Sparse Series

1. Attributes:
   + .sparse.density
   + .sparse.fill_value
   + .sparse.npoints
   + .sparse.sp_values
3. Methods:
   + .sparse.to_dense()
   + .sparse.from_coo()
   + .sparse.to_coo()   
'''

import pandas as pd
import numpy as np