# Remove target words entries from oxford dictionary data set 

# By: Iris Luden 
# Created at: March 2023
    
import pandas as pd 
import os
import sys 


# helper functions 
def read_dictionary_data(filename): 
    ''' reads the oxford dictionary format
    loads into a list'''
    data = []
    with open(filename, 'r') as o: 
        for line in o: 
            data.append(line.split("\t"))
            
    return data 

def remove_targetwords(targetwords, data):
    ''' filters the target words from data list'''
    new_data = []
    
    for line in data: 
        word = line[0].split("%")[0]
        if word not in targetwords: 
            new_data.append(line)
    return new_data

# write filtered back to files 
def write_to_file(path, filename, data): 
    ''' write back to files'''
    with open(path + filename, 'w') as w: 
        for line in data: 
            w.write('\t' .join(line))
                    
    print(f"finished writing file to {path + filename}")

if __name__ == "__main__": 
    args  = sys.argv

    if len(args) < 4:
        print("Usage: python filter_oxford_data.py <path-stable> <path-changing> <path-emerging>")
    else: 

        # read target words 
        stable_targets = set(pd.read_csv(sys.argv[1])['Word'])
        changing_targets = set(pd.read_csv(sys.argv[2])['Word'])
        emerging_targets = set(pd.read_csv(sys.argv[3])['Word'])
        targetwords = changing_targets.union(emerging_targets).union(stable_targets)

        path = 'oxford_orig/'
        files = ['train.txt', 'train.eg', 'test.txt', 'test.eg', 'valid.txt', 'valid.eg']

        # remove target words from data 
        for file in files: 
            data = read_dictionary_data(path + file)
            data_new = remove_targetwords(targetwords, data)
            write_to_file('oxford/', file, data)