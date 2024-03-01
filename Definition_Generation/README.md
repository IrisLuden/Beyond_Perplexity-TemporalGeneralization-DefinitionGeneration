# Fine-tuning T5 for contextualized definition generation 

This folder contains the results of the contextualized definition generation experiments for the set of targetwords found in the folder 'Targetwords/'. 

We fine-tune T5 following Huang et. al. (2021). Instructions of fine-tuning can be found here: https://github.com/amanotaiga/Definition_Modeling_Project . 


|_> data/
    |_> oxford_orig: upload the original oxford data set found in http://www.tkl.iis.u-tokyo.ac.jp/~ishiwatari/naacl_data.zip
    |_> filder_oxford_data.py filters oxford_orig for the designated targetwords
    |_> oxford
        |_> train.txt    
        |_> train.eg
        |_> valid.txt
        |_> valid.eg
        
        |_> test.txt (the to-be-predicted definitions
        |_> test.eg (insert desired example sentences
|_> 2_7_1_Thesis_experiment_nist_test_best_predictions.txt
    predictions made for example sentences by the fine-tuned model
|_> Judgement Aggregation.ipynb
    Notebook where judgements are aggregated and krippindorff alpha is computed
|_> Shuffled_2_7_1_Annotators_experiment_nist_test_best_predictions.tsv
    The target words are shuffled such that the emerging, stable, and changing targetwords are mixed. This file (excluding the first column) is given to the annotators. 
|_> Annotations_Merged_2_7_1_Annotators_experiment.tsv
    Judgements of the annotators in a single file. Contains the columns: 
    
    - Word: the target word for which the contexxtualized definition is generated
    - Judgement: an empty column in which the annotators can fill in their judgement 
    - Example: the sentence in which the target word is used 
    - Prediction/Definition: the predicted definition by the definition generation model
