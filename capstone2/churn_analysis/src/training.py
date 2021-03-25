###############################
# 
# developed by Bradley Mensah, March 2021
# as a part of Springboard Data Science bootcamp
# Capstone 2 Project: Churn Analysis
# Code based on the following tutorial provided by Google:
# https://cloud.google.com/ai-platform/training/docs/getting-started-scikit-xgboost#create-training-module
#
# As well as the following tutorial by Rob Salgado:
# https://towardsdatascience.com/hyperparameter-tuning-on-google-cloud-platform-with-scikit-learn-7d6155195efb
#
##############################

# [START setup]
import datetime
import os
import subprocess
import sys
import argparse
import hypertune
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import recall_score
from sklearn.model_selection import train_test_split


# Create argument parser for parameters
parser = argparse.ArgumentParser()

parser.add_argument(
        "--objective",
        help="evaluation metric",
        default="binary:logistic",
        type=str
        )
parser.add_argument(
       "--eta",
       help="learning rate",
       default=0.3,
       type=float
        )
parser.add_argument(
        "--max_depth",
        help="tree maximum depth",
        default=6,
        type=int
        )
perser.add_argument(
        "--min_child_weight",
        help="minimum sum of instance weight needed in a child",
        default=1,
        type=int
        )
parder.add_argument(
        "--colsample_bytree",
        help="subsample ratio of columns when constructing each tree",
        default=0.1,
        type=float
        )
parder.add_argument(
        "--gamma",
        help="Minimum loss reduction required to make a further partition on a leaf node of the tree.",
        default=0.1,
        type=float
        )

args = parser.parse_args()

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
data = pd.read_csv(data_filename)#.values
target = pd.read_csv(target_filename)#.values

# Convert one-column 2D array into 1D array for use with xgboost
target = target.reshape((target.size,))
# [END load-into-pandas]

# [START train-and-save-model]
# Load data into DMatrix object
#dtrain = xgb.DMatrix(data, label=target)

# Split data into training and verification splits
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3)

# Define model with tuning params
model = XGBClassifier(
        objective=args.objective,
        eta=args.eta,
        max_depth=args.max_depth,
        min_child_weight=args.min_child_weight,
        colsample_bytree=args.colsample_bytree,
        gamma=args.gamma
        )
#bst = xgb.train({}, dtrain, 20)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Define score to evaluate the classifier on recall
score = recall_score(y_test, y_pred)

# Call the hypertune library and set metric
hpt = hypertune.HyperTune()
hpt.report_hyperparameter_tuning_metric(
        hyperparameter_metric_tag="recall",
        metric_value=score,
        global_step=1000
        )

# Export the classifier to a file
model_filename = 'model.bst'
bst.save_model(model_filename)
# [END train-and-save-model]

# [START upload-model]
# Upload the saved model file to Cloud Storage
gcs_model_path = os.path.join('gs://', BUCKET_NAME, datetime.datetime.now().strftime('%Y%m%d_%H%M%S'), model_filename)
subprocess.check_call(['gsutil', 'cp', model_filename, gcs_model_path], stderr=sys.stdout)
# [END upload-model]




