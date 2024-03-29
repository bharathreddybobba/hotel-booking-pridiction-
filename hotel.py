
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import scipy.stats as st
import warnings
warnings.filterwarnings("ignore")

df= pd.read_csv("//content//hotel_bookings.csv.zip")

df

df.isnull().sum()

#Handling the missing

missing_value=["N/a","na",np.nan]
df = pd.read_csv("//content//hotel_bookings.csv.zip",na_values=missing_value)

df.isnull()

sns.heatmap(df.isnull(),yticklabels=False)

df

df.dropna(how="all")

df.fillna(method="ffill")

df.interpolate()

sns.distplot(["adults"])

sns.distplot(df["adults"],kde=False,bins=30)

sns_plot=sns.jointplot(x='agent',y="lead time",data=df,kinds="scatter")

sns.displot(df['agent'],kde=False);

sns.boxplot(df['agent']),

sns.boxplot(df['adults']),

#biv

sns.heatmap(df.corr(),annot = True)
plt.show()

sns.pairplot(df)
plt.show()

np.corrcoef(df['adr'],df['agent'])

st.pearsonr(df['stays_in_weekend_nights'],df['stays_in_week_nights'])

sns.scatterplot(df['agent'],df['company'])

from scipy.stats import spearmanr

spearmanr(df['agent'],df['company'])

spearmanr(df['agent'],df['adults'])

st.pearsonr(df['stays_in_weekend_nights'],df['stays_in_week_nights'])

df.plot(kind='scatter', x='hotel', y='adults')

ho=pd.DataFrame(df['hotel'])
dw=pd.DataFrame(df['days_in_waiting_list'])

lr = sm.OLS(ho, dw).fit()
lr.params
lr.summary()

fig = plt.gcf()
fig.set_size_inches(10,10)
plt.scatter(hotel, days_in_waiting_list)
plt.plot(hotel, 1.012e+06 + 25881*hotel, 'r' )
plt.show()

outliers=[]
def detect_outlier(df):
    
    threshold=3
    mean_1 = np.mean(df)
    std_1 =np.std(df)
    
    
    for y in df:
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers

outlier_datapoints = detect_outlier(df)
print(outlier_datapoints)

sorted(df)

q1, q3= np.percentile(df,[25,75])

iqr = q3 - q1

lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr)

from scipy.stats import skew

df['agent'].hist(grid = False)

df['agent'].skew()

sns.distplot(df['agent'], hist = True)

log_Total = np.log(df['agent'])
log_Total.head(5)

log_Total.skew()

sqrt_Total = np.sqrt(df['agent'])

sqrt_Total.head(5)

sqrt_Total.skew()

sns.distplot(sqrt_Total, hist = True)



