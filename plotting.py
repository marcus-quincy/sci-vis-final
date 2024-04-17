import pandas as pd
import numpy as np
import glob
import seaborn as sns
import matplotlib.pyplot as plt

def augment_csv_with_speed(df):
    df['speed'] = df.apply(lambda row: np.linalg.norm([row.vx,row.vy,row.vz]),axis=1)

def augment_csv_with_distance(df):
    cx = df['x'].mean()
    cy = df['y'].mean()
    cz = df['z'].mean()
    df['dist'] = df.apply(lambda row: np.linalg.norm([row.x - cx, row.y - cy, row.z -cz]), axis=1) 

def find_repeat_time_idx(df):
    drop_idx = {}
    for id in df:
        cur = float('inf')
        for i,speed in zip(df.index,df[id]):
            if cur == speed:
                drop_idx[id] = i
                break
            else:
                cur = speed
    return drop_idx

def drop_repeats(df, drop_idx):
    for id,idx in drop_idx.items():
        idx = list(range(idx,19))
        df.loc[idx,id] = np.nan


files = sorted(glob.glob('splitData/ids_c_*.csv'))
df = pd.DataFrame(columns=['id','time_step','speed','dist'])

for i,csv in enumerate(files):
    dfi = pd.read_csv(csv)
    dfi['time_step'] = i
    augment_csv_with_distance(dfi)
    df = pd.concat([df, dfi[['id','time_step','speed','dist']]])

speed_pivot = df.pivot(index='time_step', columns='id', values='speed')
dist_pivot = df.pivot(index='time_step', columns='id', values='dist')
drop_idx = find_repeat_time_idx(speed_pivot)
drop_repeats(speed_pivot,drop_idx)
drop_repeats(dist_pivot,drop_idx)

speed_df = speed_pivot
dist_df = dist_pivot
print(df.head())

plt.figure(figsize=(20,20))
ax = sns.lineplot(speed_df,dashes=False,markers=['o'])
ax.set_xticks(range(19))
ax.set_xlabel('Time Step')
ax.set_ylabel('Speed')
ax.set_title('Star Speed Over Time')
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
plt.show()

plt.figure(figsize=(20,20))
ax = sns.lineplot(dist_df,dashes=False,markers=['o'])
ax.set_xticks(range(19))
ax.set_xlabel('Time Step')
ax.set_ylabel('Distance from Center of Cluster')
ax.set_title('Star Distance from Center Over Time')
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
plt.show()