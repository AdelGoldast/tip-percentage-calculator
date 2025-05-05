import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tip.csv')

# جایگزینی مقدارهای خالی
df.fillna('-', inplace=True)

#محاسبه میانگین انعام
df ['Main tip'] = df['tip'] / df['total_bill']  * 100

#میانگین ها
mean_tip_by_sex = df.groupby('sex')['tip'].mean()

mean_tip_per_day = df.groupby('day')['tip'].mean()

mean_tip_by_time = df.groupby('time')['tip'].mean()

#تنظیمات نمودار
plt.figure(figsize=(10, 6))
mean_tip_per_sex = df.groupby('sex')['tip'].mean().plot(kind='pie', color='skyblue')
plt.title('Average Tip per sex')
plt.xlabel('Sex')
plt.ylabel('Tip')
plt.show()

plt.figure(figsize=(10, 6))
mean_tip_per_day = df.groupby('day')['tip'].mean().plot(kind='pie', color='skyblue')
plt.title('Average Tip per Day of the Week')
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()

plt.figure(figsize=(10, 6))
mean_tip_per_time = df.groupby('time')['tip'].mean().plot(kind='pie', color='skyblue')
plt.title('Average Tip per Time')
plt.xlabel('Time')
plt.ylabel('Tip')
plt.show()


print(df.head())







