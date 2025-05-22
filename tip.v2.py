import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tip.csv')

# چک کردن مقادیر خالی و جایگزینی آنها
print(df.isnull().sum())
df.fillna('0', inplace=True)

#محاسبه میانگین انعام
df ['Main tip'] = df['tip'] / df['total_bill']  * 100

#میانگین ها
mean_tip_by_sex = df.groupby('sex')['tip'].mean()
median_tip_by_sex = df.groupby('sex')['tip'].median()

mean_tip_per_day = df.groupby('day')['tip'].mean()
median_tip_per_day = df.groupby('day')['tip'].median()

mean_tip_by_time = df.groupby('time')['tip'].mean()
median_tip_by_time = df.groupby('time')['tip'].median()

#تنظیمات نمودار
plt.figure(figsize=(10, 6))
mean_tip_per_sex = df.groupby('sex')['tip'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Tip per sex')
plt.xlabel('Sex')
plt.ylabel('Tip')
plt.show()

plt.figure(figsize=(10, 6))
mean_tip_per_day = df.groupby('day')['tip'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Tip per Day of the Week')
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()

plt.figure(figsize=(10, 6))
mean_tip_per_time = df.groupby('time')['tip'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Tip per Time')
plt.xlabel('Time')
plt.ylabel('Tip')
plt.show()

#فیلتر داده برای روز شنبه و وعده شام
Saturday_dinner = df[(df['day'] == 'Sat') & (df['time']  == 'Dinner')]
Thursday_lunch = df[(df['day'] == 'Thur') & (df['time'] == 'Lunch')]

#محاسبه میانگین انعام بر اساس جنسیت
mean_tip_Saturday_dinner = Saturday_dinner.groupby ('sex') ['tip'].mean()
mean_tip_Thursday_lunch = Thursday_lunch.groupby('sex')['tip'].mean()

# رسم نمودار میانگین انعام در روز شنبه و شام بر اساس جنسیت
plt.figure(figsize=(8, 5))
mean_tip_Saturday_dinner.plot (kind='bar', color=['lightgreen', 'lightblue'])
plt.title('Average Tip by Gender on Saturday Dinner')
plt.xlabel('Sex')
plt.ylabel('Average Tip')
plt.show()

plt.figure(figsize=(8, 5))
mean_tip_Thursday_lunch.plot(kind='bar', color=['red', 'blue'])
plt.title('Average Tip by Gender on Thursday Lunch')
plt.xlabel('Sex')
plt.ylabel('Average Tip')
plt.show()

print(df.head())