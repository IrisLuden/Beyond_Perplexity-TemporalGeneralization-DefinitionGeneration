# Beyond Perplexity: Examining Temporal Generalization of Large Language Models via Definition Generation

Paper (CLIN33): [TO DO insert link]

## Authors

Iris Luden
dr. Mario Giulianelli
prof. dr. Raquel Fernandez

# Abstract 
The advent of large language models (LLMs) has significantly improved performance across various Natural Language Processing tasks. However, the performance of LLMs has been shown to deteriorate over time, indicating a lack of temporal generalization. 
To date, performance deterioration of LLMs is primarily attributed to the factual changes in the real world over time. However, not only the facts of the world, but also the language we use to describe it constantly changes. Recent studies have indicated a relationship between performance deterioration and semantic change. This is typically measured using perplexity scores and relative performance on downstream tasks. Yet, perplexity and accuracy do not explain the effects of temporally shifted data on LLMs in practice. 

In this work, we propose to assess lexico-semantic temporal generalization of a language model by exploiting the task of contextualized word definition generation. This in-depth semantic assessment enables interpretable insights into the possible mistakes a model may perpetrate due to meaning shift, and can be used to complement more coarse-grained measures like perplexity scores. To assess how semantic change impacts performance, we design the task by differentiating between semantically stable, changing, and emerging target words, and experiment with $\texttt{T5-base}$, fine-tuned for contextualized definition generation. 

Our results indicate that (i) the model’s performance deteriorates for the task of contextualized word definition generation, (ii) the performance deteriorates more for semantically changing words compared to semantically stable words, (iii) the model exhibits significantly lower performance and potential bias for emerging words, and (iv) the performance does not correlate with cross-entropy or (pseudo)-perplexity scores. Overall, our results show that definition generation can be a promising task to assess a model’s capacity for temporal generalization with respect to semantic change. 

# Content

This repository contains the following content: 
1. Two corpora consisting of Twitter and Reddit data. Corpus 1 contains data from July 2015 - April 2019. Corpus 2 contains data from May 2019 - February 2023. 
    (-> Corpora/)
2. A collected set of target words under investigation: changing, stable, and emerging words in 
    (-> Targetwords/)
3. Computed LSCD scores for the target words 
    (-> LSCD_scores)
4. Fine-tuning T5-base for definition generation following Huang et. al. (2021). 
5. Applied the DG model on a collection of example usages for each target word. 
    (Results/Experiment_testset_DG/)
6. Human annotation 
    ('Results/Perplexity_DG_results_annotated_testset.tsv' )
7. Compute loss for the collected example sentences (Perplexity, psuedo-log-likelihood, and Cross-entropy loss analysis (Results/Perplexity_DG_results_first_20_target_words.tsv) ) 

# Files 
|_> Corpora/

    |_> Corpus1

    |_> Corpus2

|_> Collect_Corpus_Reddit

|_> Collect_Corpus_Twitter

|_> Corpus_statistics.ipynb

|_> Targetwords

|_> LSCD_scores

|_> Definition_Generation 
    |_> data/oxford/
    
|_> Compute_Loss

|_> Results 
    |_> Experiment_testset_DG
        |_> test.eg
        |_> test.txt
        |_> 2_7_1_Thesis_experiment_nist_test_best_predictions.txt 
    |_> Perplexity_DG_results_annotated_testset.tsv
    |_> Perplexity_DG_results_first_20_target_words.tsv

# References

#### Reddit API
Baumgartner, J., Zannettou, S., Keegan, B., Squire, M., and Blackburn, J.
(2020). The Pushshift Reddit Dataset. Proceedings of the International AAAI
Conference on Web and Social Media, 14:830–839. https://doi.org/10.1
609/icwsm.v14i1.7347.

#### Twitter API 
Loureiro, D., Barbieri, F., Neves, L., Espinosa Anke, L., and Camacho-collados,
J. (2022a). TimeLMs: Diachronic language models from Twitter. In Pro-
ceedings of the 60th Annual Meeting of the Association for Computational
Linguistics: System Demonstrations, pages 251–260, Dublin, Ireland. Associ-
ation for Computational Linguistics. https://aclanthology.org/2022.ac
l-demo.25.

#### LSCD
Schlechtweg, D., Hätty, A., del Tredici, M., & im Walde, S. S. A Wind of Change: Detecting and Evaluating Lexical Semantic Change across Times and Domains.
https://aclanthology.org/P19-1072/

#### Fine-tuning T5 for Contextualized Defintion Generation
Huang, H., Kajiwara, T., and Arase, Y. (2021). Definition Modelling for
Appropriate Specificity. In Proceedings of the 2021 Conference on Empir-
ical Methods in Natural Language Processing, pages 2499–2509, Online and
Punta Cana, Dominican Republic. Association for Computational Linguistics.
https://aclanthology.org/2021.emnlp-main.194

# Citing

If you use our work in your research, please use the following bib entry to cite the [to do]
```
insert BibTeX entry 
```


# Contact

In case of questions, contact [irisluden@gmail.com]
