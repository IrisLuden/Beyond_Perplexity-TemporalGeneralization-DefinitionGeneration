# Definition generation results

Author: Iris Luden 


# Files 

|_> Shuffled: contains the columns:
    - Word_id 
    - Word
    - Corpus	
    - Line number	
    - Example 
    - Prediction	
    - Judgement
    
|_> Annotators file: Contains only the columns

    - Word: the target word for which the contexxtualized definition is generated
    - Judgemnt: an empty column in which the annotators can fill in their judgement 
    - Example: the sentence in which the target word is used 
    - Prediction/Definition: the predicted definition by the definition generation model

|_> Perplexities: contains the metadata. Columns are: 

    - Word_id: targetword%Corpusid.lineid
    - Word: target word only
    - Example: example sentence from corpus determined by corpusid
    - Prediction: definition generated for the example sentence
    - Examples NLL: cross-entropy/negative-log-likelihood of T5-base for the example sentence in the corresponding row
    - Definitions NLL: negative log-likelihood of T5-base for the generated definition in the corresponding row
    - Words NLL: negative log-likelihood of T5-base for predicting the masked target word in the example sentence of the corresponding row
    - Examples PPL: perplexity of the example sentence 
    - Words PPL: perplexity of the masked target word prediction task
    - Definitions PPL: perplexity on the definition
    - Examples PLL left: pseudo-log-likelihood of the example sentence when calculating the pseudo-log-likelihood only using the left hand context of the sentence
    - Definitions PLL left:	pseudo-log-likelihood of the definition when calculating the pseudo-log-likelihood only using the left hand context of the sentence
    - Examples PLL bi: pseudo-log-likelihood when calculating the pseudo-log-likelihood only using context of both sides of the target word
    - Definitions PLL bi: 	pseudo-log-likelihood when calculating the pseudo-log-likelihood only using the context of both sides of the target word 

