def Aggregate_Features(df,col1,col2):
 agg_df = df.groupby(col1)[col2].agg(Total='sum', Count='count', Average='mean',StdDev='std').reset_index()
 df=df.merge(agg_df, on=col1, how='left')
 return df

def get_time(df,col):
 import pandas as pd 
 df[col] = pd.to_datetime(df[col])
 df['Hour'] = df[col].dt.hour
 df['Day'] = df[col].dt.day 
 df['Month'] = df[col].dt.month
 df['Year'] = df[col].dt.year
 return df

def label_encode(df,col):
  from sklearn.preprocessing import LabelEncoder
  le = LabelEncoder()
  df[f'{col}_encoded'] = le.fit_transform(df[col]) 
  return df


#Scaler
def scaler(df):
 from sklearn.preprocessing import StandardScaler
 scaler = StandardScaler()
 scaled_values = scaler.fit_transform(df[["Amount","Value","Total",'Count',"Average","StdDev"]])
 df[["Amount","Value","Total",'Count',"Average","StdDev"]] = scaled_values
 return df


def missing_values(df):
 from sklearn.impute import SimpleImputer
 imputer = SimpleImputer(strategy="constant",fill_value=0)
 values=imputer.fit_transform(df[["StdDev"]]) 
 df[["StdDev"]]=values 
 return df




#wrap functions
from functools import partial

func1 = partial(Aggregate_Features, col1="CustomerId",col2="Amount")
func2 = partial(get_time,col="TransactionStartTime")
func3 = partial(label_encode,col="ProductCategory")
func4 = partial(label_encode,col="ChannelId")
func5 = partial(scaler)
func6 = partial(missing_values)
# define Custom Transformer Class
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureAdder(BaseEstimator, TransformerMixin):
    def __init__(self, funcs=None):
        self.funcs = funcs if funcs is not None else []

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_copy = X.copy()
        for func in self.funcs:
            X_copy = func(X_copy) 
        return X_copy

from sklearn.pipeline import Pipeline
pipe = Pipeline([('feature_adder', FeatureAdder(funcs=[func1,func2,func3,func4,func5,func6]))])








