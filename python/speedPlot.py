import pandas as pd
import numpy as np
import glob
import seaborn as sns
import matplotlib.pyplot as plt

files = sorted(glob.glob('splitData/ids_c_*.csv'))

def augment_csv_with_speed(df):
    df['speed'] = df.apply(lambda row: np.linalg.norm([row.vx,row.vy,row.vz]),axis=1)

def drop_repeats(df):
    for id in df:
        cur = float('inf')
        escape_id = 0
        for i,speed in zip(df.index,df[id]):
            if cur == speed:
                escape_id = i
                break
            else:
                cur = speed
        idx = list(range(escape_id,19))
        df.loc[idx,id] = np.nan

df = pd.DataFrame(columns=['id','time_step','speed'])
for i,csv in enumerate(files):
    dfi = pd.read_csv(csv)
    dfi['time_step'] = i
    df = pd.concat([df, dfi[['id','time_step','speed']]])

df = df.pivot(index='time_step', columns='id', values='speed')
drop_repeats(df)
print(df.head())

plt.figure(figsize=(20,20))
ax = sns.lineplot(df,dashes=False,markers=['o'])
ax.set_xticks(range(19))
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
plt.show()