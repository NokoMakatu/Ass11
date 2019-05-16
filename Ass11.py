import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

df = pd.read_csv('tips.csv')
print(df)
df['paid'] = df.tip + df.total_bill
paid = df.paid
print(df)
dinner = df[df.time == 'Dinner']
lunch = df[df.time == 'Lunch']
print(dinner)
print(lunch)

cor = df["total_bill"].corr(df["tip"])
print(cor)

mpl.bar("dinner", np.mean(dinner.tip))
mpl.bar("lunch", np.mean(lunch.tip))
mpl.ylabel("Tips")
mpl.xlabel("Time")
mpl.title("Lunch vs Dinner Tips")
mpl.show()