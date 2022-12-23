import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

money_df = pd.read_csv('M2SLMoneyStock.csv')
spending_df = pd.read_csv('PCEPersonalSpending.csv')
df = money_df.join(spending_df)
