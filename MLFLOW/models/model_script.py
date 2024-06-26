
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import  xgboost
import pandas as pd
import mlflow
import math
import argparse


df = pd.read_csv('data/Housing.csv')
df_clean = df[['price', 'bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 
       'lat', 'long', 'sqft_living15', 'sqft_lot15']].copy()

X = df_clean.drop('price',axis=1)
y = df_clean['price'].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

d_train = xgboost.DMatrix(X_train, label = y_train)
d_test = xgboost.DMatrix(X_test, label = y_test)

def parse_args():
    parser= argparse.ArgumentParser(description='Model arguments')
    parser.add_argument('--learning-rate', type = float, default= 0.3, help="texto de ajuda aqui")
    parser.add_argument('--max-depht', type = int, default= 6, help="texto de ajuda aqui")
    parser.add_argument('--seed', type = int, default= 42, help="texto de ajuda aqui")

    return parser.parse_args()



def main():
    args =  parse_args()
    xgb_params = {
        'learning_rate':args.learning_rate,
        'seed': args.seed,
        'max_depht': args.max_depht
    }
    mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")
    mlflow.set_experiment('house-pott-script')
    with mlflow.start_run():
        mlflow.xgboost.autolog()
        xgb = xgboost.train(xgb_params, d_train, evals = [(d_train,'train')])
        xgb_predicted = xgb.predict(d_test)
        mse = mean_squared_error(y_test, xgb_predicted)
        rmse =  math.sqrt(mse)
        r2 = r2_score(y_test, xgb_predicted)
        mlflow.log_metric('mse',mse)
        mlflow.log_metric('rmse',rmse)
        mlflow.log_metric('r2',r2)
        

if __name__ == '__main__':
    main()