import datetime as dt
import time
import json
import nltk

def correct_date(year, month, day):
    '''Returns True if the date exists
    Returns False otherwise'''
    try: 
        dt.datetime(year, month, day)
        return True
    except: 
        return False
    
def find_start_end_times(year, month, day):
    ''' Checks if the desired day exists 
        For a given day, returns the datetime of this day and the next
        if not, returns none
        if yes, returns the timestamp of the day and of the day after'''
    
    if correct_date(year, month, day + 1):
        starttime = dt.datetime(year, month, day)
        endtime = dt.datetime(year, month, day+1)

    # last day of the month:
    else:   
        # last month of the year 
        if month == 12: 
            
            starttime = dt.datetime(year, month, day)
            
            year += 1
            month = 1
            day = 1 
            endtime = dt.datetime(year, month, day)

        # in case it's just another month of the year, flip 
        elif correct_date(year, month, day):
            starttime = dt.datetime(year, month, day)
            endtime = dt.datetime(year, month + 1, 1)
        else: 
            return None, None
        
    return int(starttime.timestamp()), int(endtime.timestamp())

def filter_text(text, word_threshold=10):
    '''Returns False if the text is too short, empty or removed
    Automatically also filters the [removed] posts'''
    if len(text.split()) < word_threshold:
        return False
    else:
        return True 
    
def search_posts_month(api_praw, month, year, N=500):
    '''Requests at most N posts and N comments per day. 
    returns the texts and corresponding ids in lists'''
    
    text_ids = []
    all_texts = []
    
    start_all = time.time()
    
    for day in range(1, 32):
        
        starttime, endtime = find_start_end_times(year, month, day)

        # retrieve posts 
        if starttime != None: 
            
            # retrieve posts for this day except if the text is too short 
            posts = [p for p in api_praw.search_submissions(limit=N, since=starttime, until=endtime, is_video=False)
                         if filter_text(p['selftext'])]
            
            text_ids += [p['id'] for p in posts]
            all_texts += [p['selftext'] for p in posts ]
            
            # retrieve comments 
                        # retrieve posts for this day except if the text is too short 
            comments = [p for p in api_praw.search_comments(limit=N, since=starttime, until=endtime, is_video=False)
                         if filter_text(p['body'])]
            
            text_ids += [c['id'] for c in comments]
            all_texts += [c['body'] for c in comments]  
            print(day, "Number of posts", len(posts), "number of comments", len(comments))
        
    end_all = time.time()
    print(f"Searching month {month} took {int(end_all-start_all)} seconds.\n")
    print(f"Month {month} yielded {len(text_ids)} requests")
    
    return all_texts, text_ids

def save_month(texts_list, text_ids, year, month): 
    ''' Given the results of a month, saves the texts and ids in the corresponding files'''
    
    id2text = {}
    
    with open(f'Reddit_data/{str(year)}/texts/texts_{str(year)}_{str(month)}.txt', 'wb') as o: 
        with open(f'Reddit_data/{str(year)}/ids/text_ids_{str(year)}_{str(month)}.txt', 'wb') as o2: 
            
            for i in range(len(texts_list)):

                text = texts_list[i] + '\n'

                # in case the text contains characters that cannot be read 
                o.write(text.encode('utf-8'))
                o2.write((text_ids[i] + '\n').encode('utf-8'))
                
                id2text[text_ids[i]] = text
                
    with open(f'Reddit_data/{year}/id2text_{year}_{month}.json', 'w') as fp:
        json.dump(id2text, fp)
    
    print(f"Saved in 'Reddit_data/{year}_{month}.txt")

def request_and_save(api_praw, year, N=500, start_month=1, end_month=12):
    ''' Requests documents from Reddit for a given year 
    Saves the documents in a file per month 
    Requests for every day individually'''
    
    total_nr_posts = 0
    
    for month in range(start_month, end_month + 1):
        
        print(f"Searching month {month}...")        
        month_posts, month_ids = search_posts_month(api_praw, month, year, N)
        save_month(month_posts, month_ids, year, month)
        
        total_nr_posts += len(month_posts)

    print(f"The year {year} yielded a total of {total_nr_posts} posts")
    
def yield_extra_submissions(year, month):
    ''' Requests by weekly dates and adds it to the existing data files.
        Checks whether there are no duplicate IDs before the posts/comments are added'''
    
    # open file of ids 
    with open(f'Reddit_data/{year}/ids/text_ids_{year}_{month}.txt', 'r', encoding='utf-8') as f: 
        ids_data = f.readlines()
        ids_data = [i.strip('\n') for i in ids_data]
        existing_ids = set(ids_data)

    N = 500

    text_ids = []
    all_texts = []

    start_all = time.time()

    # go over each week 
    for day in range(6, 32, 7):

        starttime, endtime = find_start_end_times_weekly(year, month, day)

        # retrieve posts
        if starttime != None: 

            # retrieve posts for this day except if the text is too short 
            posts = [p for p in api_praw.search_submissions(limit=N, since=starttime, until=endtime, is_video=False)
                         if filter_text(p['selftext'])]
            text_ids += [p['id'] for p in posts if p['id'] not in existing_ids]
            all_texts += [p['selftext'] for p in posts if p['id'] not in existing_ids]
            print(len(text_ids))
                        
            # retrieve comments 
            comments = [p for p in api_praw.search_comments(limit=N, since=starttime, until=endtime, is_video=False)
                         if filter_text(p['body'])]
            text_ids += [c['id'] for c in comments if c['id'] not in existing_ids]
            all_texts += [c['body'] for c in comments if c['id'] not in existing_ids]  
            print(len(text_ids))

            print("Number of posts", len(posts), "number of comments", len(comments))

    print("This month yielded a total of", len(text_ids), "useful posts")
    end_all = time.time()

    print(f"Searching month {month} took {int(end_all-start_all)} seconds\n")
    print(f"Month {month} yielded {len(text_ids)} useful requests")
    
    # add data to existing files 
    id2text = {}
    with open(f'Reddit_data/{year}/texts/texts_{year}_{month}.txt', 'ab') as o: 
        with open(f'Reddit_data/{year}/ids/text_ids_{year}_{month}.txt', 'ab') as o2: 

            for i in range(len(all_texts)):
                
                text = all_texts[i] + '\n'

                # in case the text contains characters that cannot be read 
                o.write(text.encode('utf-8'))
                o2.write((text_ids[i] + '\n').encode('utf-8'))
                id2text[text_ids[i]] = text
                
    # write new documents to files
    with open(f'Reddit_data/{year}/id2text_{year}_{month}2.json', 'a') as fp:
        json.dump(id2text, fp)
    
    return True


# For data cleaning 

def filter_non_English(text, stopwords):
    '''Returns False if none of the stopwords occur in the text'''
    text = text.lower()
    
    for sw in stopwords:
        if f' {sw} ' in text:
            return True
    return False

def collect_clean_texts(year, month):
    
    outfile = open(f'Reddit_data/{year}/texts_clean/{year}_{month}_cleaned_texts.txt', 'wb')
    
    sentence_tokenizer = nltk.tokenize.sent_tokenize
    words_tokenizer = nltk.tokenize.TreebankWordTokenizer()
    stopwords = set(nltk.corpus.stopwords.words('english')) - {'o', 'a', 'd', 't', 's', 'm', 'y', 'ma', 'no', 'me', 'do'}
    
    # collect the frequency counts of the words in each month. 
    monthly_freqs = Counter()

    # read month-specific file
    with open(f'Reddit_data/{year}/texts/texts_{year}_{month}.txt', 'r', encoding='utf-8') as f: 

        texts = f.readlines()
        
        # remove the enters and empty text s
        texts = [t.strip('\n') for t in texts]
        texts = [t for t in texts if t != '']

        # make the text lower case and clean the text 
        for text in texts: 

            # some exceptional characters
            text = text.replace("’", "'")
            text = text.replace("…", "...")

            
            # check if the text is in English 
            if filter_non_English(text, stopwords):
                
                sentences = sentence_tokenizer(text)

                for s in sentences:

                    words = words_tokenizer.tokenize(s)

                    # clean the words 
                    words = [word.strip('#"$%&()*+,-/:;<=>@[\]^_`{|}~”“') for word in words]
                    words = [word.lower() for word in words if (word != '')]

                    # writes every sentence on a separate line
                    # if the sentence is at least 10 terms long
                    if len(words) >= 10 and len(words) < 400:
                        text = ' '.join(words)
                        outfile.write(text.encode('utf-8'))
                        outfile.write('\n'.encode('utf-8'))

                        # add the words to the counter
                        monthly_freqs += Counter(words)
    outfile.close()

    # write monthly counter to a file 
    with open(f'Reddit_data/{year}/texts_clean/Monthly_freqs_{year}_{month}.json', 'w') as o:
        json.dump(monthly_freqs, o)
        
    print(f"Completed cleaning and saving {year}-{month}")


### OLD files (not used)

def find_start_end_times_weekly(year, month, day):
    '''Checks if the desired day exists 
        For a given day, returns the datetime of this day and the next
        If not, returns none
        If yes, returns the timestamp of the day and of the day after'''
    
    if correct_date(year, month, day + 7):
        starttime = dt.datetime(year, month, day)
        endtime = dt.datetime(year, month, day+7)

    # the last day of the month:
    else:   
        # last month of the year 
        if month == 12: 
            
            starttime = dt.datetime(year, month, day)
            
            year += 1
            month = 1
            day = 1 
            endtime = dt.datetime(year, month, day)

        # just another month of the year, flip 
        elif correct_date(year, month, day):
            starttime = dt.datetime(year, month, day)
            endtime = dt.datetime(year, month + 1, 1)
        else: 
            return None, None
        
    return int(starttime.timestamp()), int(endtime.timestamp())
