import numpy as np
import pandas as pd
df = pd.read_csv(r'jobs_in_data.csv')
df.info()

import numpy as np
import pandas as pd
df = pd.read_csv(r'jobs_in_data.csv')
df.info()

#Displaying the number of duuplicate data
df.duplicated().sum()

df.work_year.value_counts()

# 5
df.job_title.value_counts()

#6
df.job_title.value_counts()

# 7
df.salary_currency.value_counts()

import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline

plt.figure(figsize=(8, 6))
sns.barplot(x='work_year', y='salary', data=df)
plt.xlabel('work_year')
plt.ylabel('salary')
plt.title('Increment in salary per Year')
plt.show()