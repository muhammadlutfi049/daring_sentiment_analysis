import pandas as pd
import matplotlib.pyplot as plt

coba_list = [1,2,3,4,5,6,7]
df = pd.DataFrame(coba_list, columns=["list"])
df["kuadrat"] = df["list"]**2
print(df.sum())

# plt.plot(df['list'],df['kuadrat'])
# plt.show()
# df.plot()


# print(df[0:5,])
print(df['list'].quantile(0.75))
# tupel = ('rendy','lutpi')
# print(tupel[tupel != 'lutpi'])