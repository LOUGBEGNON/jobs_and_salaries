import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline

plt.figure(figsize=(8, 6))
sns.barplot(x='work_year', y='salary', data=df)
plt.xlabel('work_year')
plt.ylabel('salary')
plt.title('Increment in salary per Year')
plt.show()