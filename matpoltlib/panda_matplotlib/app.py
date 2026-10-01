import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

type_values = df["Type1"].value_counts(ascending=True)

plt.barh(type_values.index , type_values.values)

plt.show()