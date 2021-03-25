###############################
# 
# developed by Bradley Mensah, March 2021
# as a part of Springboard Data Science bootcamp
# Capstone 2 Project: Churn Analysis
# Code based on the following tutorial provided by Google:
# https://cloud.google.com/ai-platform/training/docs/getting-started-scikit-xgboost#create-training-module

##############################

# [START setup]
import datetime
import os
import subprocess
import sys
import pandas as pd
import xgboost as xgb

# Google Cloud Storage bucket
BUCKET_NAME = 'churn-analysis-bucket'
# [END setup]

# [START download-data]
data_filename = 'X_train.csv'
target_filename = 'y_train.csv'
data_dir = 'gs://churn-analysis-bucket'

# gsutil outputs everything to stderr so we need to divert it to stdout.
subprocess.check_call(['gsutil', 'cp', os.path.join(data_dir, data_filename), data_filename], stderr=sys.stdout)
subprocess.check_call(['gsutil', 'cp', os.path.join(data_dir, target_filename), target_filename], stderr=sys.stdout)
# [END download-data]

# [START load-into-pandas]
# Load data into pandas, then use `.values` to get NumPy arrays
data = pd.read_csv(data_filename).values
target = pd.read_csv(target_filename).values

# Convert one-column 2D array into 1D array for use with xgboost
target = target.reshape((target.size,))
# [END load-into-pandas]

# [START train-and-save-model]
# Load data into DMatrix object
dtrain = xgb.DMatrix(data, label=target)

# Train XGBoost model
bst = xgb.train({}, dtrain, 20)

# Export the classifier to a file
model_filename = 'model.bst'
bst.save_model(model_filename)
# [END train-and-save-model]

# [START upload-model]
# Upload the saved model file to Cloud Storage
gcs_model_path = os.path.join('gs://', BUCKET_NAME, datetime.datetime.now().strftime('%Y%m%d_%H%M%S'), model_filename)
subprocess.check_call(['gsutil', 'cp', model_filename, gcs_model_path], stderr=sys.stdout)
# [END upload-model]




