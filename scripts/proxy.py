def get_time(df,col):
 import pandas as pd 
 df[col] = pd.to_datetime(df[col])
 return df
 
def removeoutliers(df):
 from scipy import stats
 import numpy as np
 z_scores = np.abs(stats.zscore(df[["Recency","Frequency","Monetary"]]))
 outlier=(z_scores > 3).any(axis=1)
 df=df[(z_scores < 3).all(axis=1)]  
 return (df,outlier) 


def scaler(df):
 from sklearn.preprocessing import StandardScaler
 scaler = StandardScaler()
 scaled_values = scaler.fit_transform(df[["Recency","Frequency","Monetary"]])
 df[["Recency","Frequency","Monetary"]] = scaled_values
 return df 

def clustering(df,col):
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=3, random_state=42)
  df['Cluster'] = kmeans.fit_predict(df[col])
  return df 