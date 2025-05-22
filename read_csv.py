import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/adelgoldast/Desktop/AI/tip.csv'

df = pd.read_csv(file_path)

print(df.head())

# بررسی اولیه
print(df.info())

# جایگزینی مقدارهای خالی
df = df.fillna('-')

df['Tip2'] = '-'

df['tip'] = pd.to_numeric(df['tip'], errors='coerce')

df['Tip2'] = (df['tip'] / df['total_bill']) * 100

df['Tip2'] = df['Tip2'].fillna('-')

#mean_tip2 = df['Tip2'].mean()
#print("Average Tip2:", mean_tip2)

#میانگین‌ها
mean_tip_by_sex = df.groupby('sex')['tip'].mean()

mean_tip_per_day = df.groupby('day')['tip'].mean()

mean_tip_by_time = df.groupby('time')['tip'].mean()


# رسم نمودار
plt.figure(figsize=(10, 6))
mean_tip_per_day.plot(kind='pie', color='skyblue')

plt.figure(figsize=(6, 5))
mean_tip_by_sex.plot(kind='bar', color=['lightcoral', 'lightblue'])

plt.figure(figsize=(6, 5))
mean_tip_by_time.plot(kind='pie', color=['orange', 'green'])


# تنظیمات نمودار
plt.title('Average Tip per Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Tip')
plt.xticks(rotation=45)
plt.show()

plt.title('Average Tip by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Tip')
plt.xticks(rotation=0)
plt.show()

plt.title('Average Tip by Meal Time')
plt.xlabel('Meal Time')
plt.ylabel('Average Tip')
plt.xticks(rotation=0)
plt.show()


# نمایش داده‌ها
print(df.head())

df.to_csv('/Users/adelgoldast/Desktop/AI/tip_cleaned.csv', index=False)
