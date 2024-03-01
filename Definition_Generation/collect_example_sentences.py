# imports 
from collections import defaultdict, Counter
from gensim.models.word2vec import PathLineSentences
import os
import nltk
import string
import pandas as pd
import sys

## Get the line number  and the target words 
def filter_rule(word):
    ''' Returns False if a word is an url or an emoji '''
    if 'https:/' in word or 'http://' in word or 'www.' in word: 
        return False
    elif '\\u' in ascii(word): 
        return False
    elif '\\U' in ascii(word): 
        return False
    else:
        return True

def read_lines(foldername):
    ''' Reads all files in corpus
    returns all data in a list'''
    for _, _, files in os.walk(foldername):
        data_lines = []
        for file in files:
            with open(foldername+ file, 'r', encoding='utf-8') as f: 
                data_lines += f.readlines()                
    return data_lines

def collect_corpus_index(sentences):
    '''Maps every word to the set of line numbers on which they occur'''
    words2lines = {}
    i = 0
    for sentence in sentences: 
        for word in sentence: 
            if filter_rule(word):
                if word not in words2lines: 
                    words2lines[word] = set()
                words2lines[word].add(i)
        i += 1 
    return words2lines

def read_corpus(foldername):

    corpuslines = []
    for folder, _, files in os.walk(foldername): 

        for file in files: 

            with open(folder+file, 'r', encoding='utf-8') as f: 
                lines = f.readlines()
                corpuslines += lines

    return corpuslines 


def clean_sentence(sentence):
    ''' Tokenizes the sentence and joins back together with spaces'''
    words = TreebankWordTokenizer().tokenize(sentence)
    words = [w for w in words if not ('\\u' in ascii(w) or '\\U' in ascii(w))]
#     return TreebankWordDetokenizer().detokenize(words)
    return ' '.join(words) # alternatively, because the model is fine-tuned on these sentences formatted like this
    
    
def filter_examples(line_numbers, examples, word):
    '''filter the example sentences according to the sentence lengths '''

    final_examples = []
    final_line_numbers = []

    # filter based on number of sentences
    for example, number in zip(examples, line_numbers):
        
        # reduce many user tags from twitter
        example = re.sub('(user )+', 'user ', example)
        
        # split the example line into sentences
        sentences = nltk.sent_tokenize(example)
        sentences = [clean_sentence(s) for s in sentences]
        
        # in case it's a single sentence 
        if len(sentences) == 1:
            
            # check if sentence is long enough
            if len(sentences[0].split()) > 11:
                final_examples.append(sentences[0])
                final_line_numbers.append(number)
        else: 
            # find the sentence with the target
            for index, sentence in enumerate(sentences): 
                
                if word in sentence: 
                    
                    if len(sentence.split(" ")) > 11:
                        final_examples.append(sentence)
                        final_line_numbers.append(number)
                        break
                    else: 
                        if index == 0: 
                            sentence = ' '.join(sentences[0:2])
                            
                        elif index == len(sentences)-1: 
                            sentence = ' '.join(sentences[index-1:])
                        else: 
                            sentence = ' '.join(sentences[index-1:index+1])
                        if len(sentence.split()) > 11:
                            final_examples.append(sentence)
                            final_line_numbers.append(number)
                        break

    return final_examples, final_line_numbers

def random_subselection(example_sentences, line_numbers, N=100):
    '''randomly select a set of at most 100 sentences in case there are too many
    while keeping track of the same line numbers '''
    subselection = random.sample(list(zip(example_sentences, line_numbers)), N)
    
    example_sentences = [e[0] for e in subselection]
    line_numbers = [e[1] for e in subselection]
    
    return example_sentences, line_numbers 

    
def yield_example_sentences(target_words, Ci, w2l, corpuslines, N=100):
    ''' Yield at most N example sentences for each target word in the corpus. 
        Only yields sentences with at least 11 terms. '''
    
    results_list = []
    
    for word in target_words: 
        
        line_numbers = list(w2l[word])
        example_sentences = [corpuslines[l].strip('\n') for l in line_numbers]

        final_example_sentences, final_line_numbers = filter_examples(line_numbers, example_sentences, word)
        
        if len(final_line_numbers) > N:
            final_example_sentences, final_line_numbers = random_subselection(final_example_sentences, final_line_numbers, N=N)
        
        # write for the output (could be written in a file directly)
        for number, sentence in zip(final_line_numbers, final_example_sentences):
            results_list.append(f'{word}%{Ci}.{number}\t{sentence}')
    return results_list

def write_example_sentences(path, sentences): 
    ''' write sentences in file. 
    Also write a dummy .txt file for the empty dictionary definitions''' 
    with open(path + 'test'' .eg', 'a', encoding='utf-8') as o1: 
        with open(path + 'test.txt', 'a', encoding='utf-8') as o2:
            for line in sentences:
                o1.write(line)
                o1.write('\n')
                
                target_id = line.split("\t")[0]
                o2.write(target_id)
                o2.write('\tpos\tsamples\tdummy definition\t[]\t[]')
                o2.write('\n')
        
    print("finished writing files")
    
if __name__ == "__main__": 
    
    args = sys.argv

    if len(args) < 4:
        print("Usage: python filter_oxford_data.py <path-stable> <path-changing> <path-emerging>")
    else: 
        
        # read the two corpora 
        texts_C1 = list(PathLineSentences('Corpora/Corpus1/'))
        texts_C2 = list(PathLineSentences('Corpora/Corpus2/'))

        w2l_C1 = collect_corpus_index(texts_C1)
        w2l_C2 = collect_corpus_index(texts_C2)

        lines_C1 = read_corpus('Corpora/Corpus1/')
        lines_C1 = read_corpus('Corpora/Corpus2/')

        # Load target words
        stable_targets = list(pd.read_csv(sys.argv[1])['Word'])
        changing_targets = list(pd.read_csv(sys.argv[2])['Word'])
        emerging_targets = list(pd.read_csv(sys.argv[3])['Word'])

        # collect example sentences for changing 
        examples_C1 = yield_example_sentences(changing_words + stable_words, 'C1', w2l_C1, lines_C1)
        examples_C2 = yield_example_sentences(changing_words + stable_words + emerging_words , 'C2', w2l_C2, lines_C2)

        # SAVE
        write_example_sentences('data/oxford/', examples_C1)
        write_example_sentences('data/oxford', examples_C2)
