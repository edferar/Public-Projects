import mlflow
mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")
logged_model = 'runs:/15aaa1cd79f044979067aae5bd203a25/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd

df = pd.read_csv('data/Housing.csv')
data = df[['bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 
       'lat', 'long', 'sqft_living15', 'sqft_lot15']].copy()

#data = df_clean.drop('price',axis=1)
result = loaded_model.predict(pd.DataFrame(data))
data['predicted'] = result
data.to_csv('data/Housing-predict.csv')