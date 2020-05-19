from sklearn import preprocessing
import numpy as np
import pandas as pd
# Get dataset
df = pd.read_csv("cleanData2.csv", sep=",")
# Normalize total_bedrooms column
x_array = np.array(df['st_dist'])
normalized_X = preprocessing.normalize([x_array])

print(list(normalized_X))

