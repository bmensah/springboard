#!/bin/bash
BUCKET_NAME="churn-analysis-bucket" 
JOB_NAME="xgboost_$(date +"%Y%m%d_%H%M%S")" 
TRAINER_PACKAGE_PATH="./xgboost_trainer/" 
MAIN_TRAINER_MODULE="xgboost_trainer.training" 
HPTUNING_CONFIG="config.yaml"
RUNTIME_VERSION=2.4 
PYTHON_VERSION=3.7 
JOB_DIR="gs://$BUCKET_NAME/xgboost_job_dir" 
gcloud ai-platform jobs submit training $JOB_NAME \
        --package-path $TRAINER_PACKAGE_PATH \
        --module-name $MAIN_TRAINER_MODULE \
  	    --runtime-version=$RUNTIME_VERSION \
  	    --python-version=$PYTHON_VERSION \
        --job-dir $JOB_DIR \
        --region us-central1 \
        --config $HPTUNING_CONFIG \

# Stream logs into console
gcloud ai-platform jobs stream-logs $JOB_NAME
