capstone3
==============================

### Springboard data science course capstone 3 project

# Applying Sentiment Analysis to Improve Customer Satisfaction for Airlines


Zendesk’s 2020 Customer Experience Trends Report explains that 80% of customers who have had two or more bad experiences with a brand will consider switching to a different brand. The report also details that customer service was the second most important factor in brand loyalty for surveyed customers (the first being price). Therefore, it is imperative to determine how satisfied customers are with customer service interactions in order to increase retention. 

As air travel is looking to rebound post-covid19, it is imperative now more than ever that airlines perform review monitoring to address and ease the concerns of returning customers. 

From this context, I developed the following problem statement: 

**What opportunities exist for airlines to increase customer retention by 5% within one quarter through developing loyalty programs, offering more destinations, or improving brand reputation?**

	In order to answer this question, I sourced labelled tweets in order to train a model to distinguish between a positive and negative tweet. I also sourced airline customers’ tweets and the airlines’ responses. Both datasets were found on Kaggle. The labelled data was a 1.6 million tweet dataset (800,000 positive tweets, 800,000 negative tweets). The airline tweets were a part of a larger dataset of customer service tweets for over 100 companies.



**Data source citations:**
 
[Labelled Sentiment Tweets](https://www.kaggle.com/kazanova/sentiment140):
**Citation:** Go, A., Bhayani, R. and Huang, L., 2009. Twitter sentiment classification using distant supervision. CS224N Project Report, Stanford, 1(2009), p.12.
 
[Customer Service Tweets](https://www.kaggle.com/thoughtvector/customer-support-on-twitter):
**Citation:** Thought Vector and Axelbrooke, Stuart (December 2017). Customer Service on Twitter, Version 10. Retrieved 4 May 2021 from: https://www.kaggle.com/thoughtvector/customer-support-on-twitter.
**License:** CC BY-NC-SA 4.0


Project Organization
------------

    ├── LICENSE
    │
    ├── README.md          <- The top-level README for developers using this project.
    │
    │
    ├── notebooks          <- Jupyter notebooks with data wrangling, EDA, preprocessing, and modeling.
    │   └── Cap3_Wrangling_and_EDA.ipynb            
    │   └── Cap3_Processing_and_Modeling.ipynb                      
    │
    ├── reports            <- Final summary report of project and slide deck presenting results.
    │   └── Mensah_Capstone3_Report.pdf
    │   └── Cap3_SlideDeck.pdf     
    │
    └──requirements.txt   <- The requirements file for reproducing the analysis environment. 


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
