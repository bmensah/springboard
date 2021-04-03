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
        |     ├── Capstone2_Data_Wrangling.ipynb
        |     ├── Capstone2_EDA.ipynb
        |     ├── Capstone2_Pre-processing.ipynb
        |     └── Capstone2_Modeling.ipynb
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
        |     ├── config.yaml <- Configuration file to 
        |     ├── training.py <- Training data to 
        |     └── training_script.sh                                                                   
        |
        └── requirements.txt <- Package versions for reproducing the virtual environment.


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
