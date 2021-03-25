BUCKET_NAME="churn-analysis-bucket" \
JOB_NAME="xgboost_$(date +"%Y%m%d_%H%M%S")" \
APP_PACKAGE_PATH="./xgboost_trainer/" \
MAIN_APP_MODULE="xgboost_trainer.training" \
RUNTIME_VERSION=2.4 \
PYTHON_VERSION=3.7 \
JOB_DIR=gs://$BUCKET_NAME/xgboost_job_dir \
gcloud ai-platform jobs submit training $JOB_NAME \
        --package-path $APP_PACKAGE_PATH \
        --module-name $MAIN_APP_MODULE \
  	    --runtime-version=$RUNTIME_VERSION \
  	    --python-version=$PYTHON_VERSION \
        --job-dir $JOB_DIR \
        --region us-central1 \
        --config config.yaml \
