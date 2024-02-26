# Collecting Twitter data 

By: Iris Luden 

Tweets are collected following Loureiro et. al. (2022): TimeLMs: Diachronic Language Models from Twitter

Code can be found here: https://github.com/cardiffnlp/timelms

#### Summary
Tweets are collected using sampler_api.py. A bearer token is required to access the twitter API. 
Loureiro et. al. (2022) sample tweets every hour. We modified the code do sample only once every four hours, as there is a limit to the number of requests that can be amde each month to the Twitter API. 

The tweets are combined into the desired time periods using scripts/combine.py. We combined the tweets into the years: 2015, 2016, 2017, 2018, 2019a, 2019b, 2020, 2021, 2022, 2023_12

The tweets are preprocessed using scripts/preprocess.py. Here, (near-)duplicates are rempoved, and users accounts are anonymified. Tweets of specific users (like bots) are removed from the data set. 

#### Collect_Clean_Twitter_Corpus 

In this notebook, we clean all tweets by: 
- making texts lower case
- tokenized using Tweet Tokenizer of NLTK, cleaned from punctuation
- tweets of less than 10 words are disregarded
