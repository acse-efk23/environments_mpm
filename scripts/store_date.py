import numpy as np
import pandas as pd
from envtest import create_data

date_data = create_data(20230201)
print(date_data)
df = pd.DataFrame(np.random.randn(6,4), index = date_data, columns = list("ABCD"))
print(df)
