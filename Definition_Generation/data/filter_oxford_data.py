# Remove target words entries from oxford dictionary data set 

# By: Iris Luden 
# Created at: March 2023
    
import pandas as pd 
import os


# create new directory 
os.mkdir('data/oxford_new/')

# 1. read target words 
changing_targets = set(pd.read_csv('Targetwords/Changing_targets_20.tsv')['Word'])
stable_targets = set(pd.read_csv('Targetwords/Stable_targets_20.tsv')['Word'])
emerging_targets = set(pd.read_csv('Targetwords/Emerging_targets_20.tsv')['Word'])

# combine in single set 
targetwords = changing_targets.union(emerging_targets).union(stable_targets)
print(len(targetwords))


# helper functions 

def read_dictionary_data(filename): 
    ''' reads the oxford dictionary format
    loads into a list'''
    data = []
    with open(filename, 'r') as o: 
        for line in o: 
            data.append(line.split("\t"))
            
    return data 

def remove_target(targetwords, data):
    ''' filters the target words from data list'''
    new_data = []
    remove_count = 0
    
    for line in data: 
        word = line[0].split("%")[0]
        if word not in targetwords: 
            new_data.append(line)
        else: 
            print(word)
            remove_count += 1
    print(f"A total of {remove_count} lines were removed")
    return new_data

# write filtered back to files 
def write_to_file(path, filename, data): 
    ''' write back to files'''
    with open(path + filename, ' w') as w: 
        for line in data: 
            w.write('\t' .join(line))
                    
    print(f"finished writing file to {path + filename}")
    
files = ['train.txt', 'train.eg', 'test.txt', 'test.eg', 'valid.txt', 'valid.eg']


for file in files: 
    data = read_dictionary_data(path + file)
    data_new = remove_targetwords(targetwords, data)
    write_to_file('data/oxford_new/', file, data)

    