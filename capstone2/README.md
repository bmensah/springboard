capstone2
==============================

Data analysis project to determine subscriber churn based on data from music subscription service KKBox.


KKBox is a music streaming service popular in South East Asia with over 10 million users. It functions on a subscription-based business model, with the majority of subscriptions lasting 30 days. An account is marked as churn if there are no new transactions within 30 days after a subscription has expired. KKBox would like to be able to predict which subscribers are likely to renew within a month of their membership ending and which ones will churn.

By using subscribers’ demographic information, listening history, and transaction history, I trained a XGBoost classification model to predict if a particular user will renew their subscription or churn. I used this model to determine which changes KKBox could make to their service that would decrease churn, ultimate goal being to increasing revenue.

Project Organization
------------

    ├── README.md <- The top-level README for developers using this project.
    |
    └── churn_analysis
        ├── capstone2_notebooks   
        |     ├── Capstone2_Data_Wrangling.ipynb <- Data Wrangling: merge raw files and perform initial data cleaning.
        |     ├── Capstone2_EDA.ipynb <- Exploratory Data Analysis: visualize data.
        |     ├── Capstone2_Pre-processing.ipynb <- Pre-processing and Training: process data, define metrics, train various models and choose best.
        |     └── Capstone2_Modeling.ipynb <- Tune hyperparameters and model various scenarios.
        |	 
        ├── models
        |     ├── bo_model.pkl <- XGBoost model tuned via bayesian optimization.
        |     └── rs_model.pkl <- XGBoost model tuned via random search.
        |      
        ├── reports 
        |     ├── Mensah_Capstone2_Proposal.pptx.pdf <- Project problem statement.   
        |     ├── Mensah_Capstone2_Report.pdf <- Project summary report.
        |     ├── Mensah_Capstone2_SlideDeck.pdf <- Project presentation slides.
        |     └── model_metric.txt <- Metrics for the final model chosen. 
        |
        ├── src     
        |     ├── config.yaml <- Hyperparameters for model tuning on Google Cloud Platform (GCP).
        |     ├── training.py <- Code to link data, model, and hyperparameters.
        |     └── training_script.sh <- Script to run hyperparameter tuning on GCP.                                                                   
        |
        └── requirements.txt <- Package versions for reproducing the virtual environment.


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
