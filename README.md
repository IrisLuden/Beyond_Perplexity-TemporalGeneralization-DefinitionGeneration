# Beyond Perplexity: Examining Temporal Generalization of Large Language Models via Definition Generation
Master of Logic
university of Amsterdam
June 2023 
By: Iris Luden
Supervision: Raquel Fernandez

# Abstract 
The emergence of large language models (LLMs) has significantly improved performance across various Natural Language Processing (NLP) tasks. However, the field of NLP predominantly follows a static language modeling paradigm, resulting in performance deterioration of LLMs over time. This indicates a lack of temporal generalization, i.e., the ability to extend their capabilities to data beyond their training period. In real-life NLP applications, models are often pre-trained on data from one time period and next deployed for tasks which inherently involves temporally shifted data. So far, performance deterioration of LLMs is primarily attributed to the factual changes over time, leading to attempts of updating a LLMs factual knowledge to avoid performance deterioration. However, not only the facts of the world, but also the language we use to describe it constantly changes. Recent studies have indicated a relationship between performance deterioration and semantic change. While previous publications have demonstrated that LLM performance may deteriorate over time, this is typically measured using perplexity scores and relative performance on downstream tasks. However, such dry comparisons of perplexity and accuracy do not explain the effects of temporally shifted data on LLMs in practice. Given the potential societal impact of NLP applications, it is crucial to not only understand if LLM performance deteriorates over time, but also gain insight into how the degradation of performance (particularly caused by semantic change) is reflected in the output of LLMs. This work investigates how semantic change in temporally shifted data impacts the performance of a LLM on the downstream task of contextualized word definition generation. This approach offers a dual perspective: quantitative measurement of performance deterioration, as well as human-interpretable output through the generated definitions. First, we construct two diachronic corpora of Twitter and Reddit data, such that one overlaps in time with the pre-training period, and the other is temporally shifted. Next, we use a lexical semantic change system to collect a set of semantically changed target words, a set of stable words, and collect a set of emerging new words. Third, we evaluate the performance of the definition generation model in both time periods, and analyze whether semantic change impacts performance. Fourth, we compare the results with cross entropy and perplexity scores for the same inputs. The results indicate that (i) the model’s performance deteriorates for the task of contextualized word definition generation, (ii) the performance deteriorates more for semantically changing words compared to semantically stable words, (iii) the model exhibits significantly lower performance and potential bias for emerging new words, and (iv) the performance does not correlate with loss or (pseudo)-perplexity scores. Overall, our results show that definition generation can be a promising task to assess a model's capacity for temporal generalization with respect to semantic and lexical change. 

# Content

This repository contains the following content: 
1. Two corpora consisting of Twitter and Reddit data. Corpus 1 contains data from July 2015 - April 2019. Corpus 2 contains data from May 2019 - February 2023. 
    (-> Corpora/)
2. A collected set of target words under investigation: changing, stable, and emerging words in 
    (-> Targetwords/)
3. LSCD models on both corpora following (Schlechtweg et. al. (2021) 
    (-> LSCD_Models/)
4. Computed LSCD scores for the target words 
    (-> LSCD_scores)
5. Fine-tuned T5-base for definition generation following Huang et. al. (2021). 
5. Applied the DG model on a collection of example usages for each target word. 
    (Results/Experiment_testset_DG/)
6. Human annotation 
    ('Results/Perplexity_DG_results_annotated_testset.tsv' )
7. Perplexity, psuedo-log-likelihood, and Cross-entropy loss analysis (Results/Perplexity_DG_results_first_20_target_words.tsv)

# Files 
|_> Corpora/

    |_> Corpus1

    |_> Corpus2:

|_> Targetwords/

    |_> ...

|_> LSCD_Models/

    |_> ...

|_> Results

    |_> Experiment_testset_DG

        |_> test.eg

        |_> test.txt

        |_> 2_7_1_Thesis_experiment_nist_test_best_predictions.txt 
            (predicted definitions)

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
Schlechtweg, D., Tahmasebi, N., Hengchen, S., Dubossarsky, H., and
McGillivray, B. (2021). DWUG: A large resource of diachronic word usage
graphs in four languages. In Proceedings of the 2021 Conference on Empir-
ical Methods in Natural Language Processing, pages 7079–7091, Online and
Punta Cana, Dominican Republic. Association for Computational Linguistics.
https://aclanthology.org/2021.emnlp-main.567.

#### fine-tuning contextualized defintion generation
Huang, H., Kajiwara, T., and Arase, Y. (2021). Definition Modelling for
Appropriate Specificity. In Proceedings of the 2021 Conference on Empir-
ical Methods in Natural Language Processing, pages 2499–2509, Online and
Punta Cana, Dominican Republic. Association for Computational Linguistics.
https://aclanthology.org/2021.emnlp-main.194.