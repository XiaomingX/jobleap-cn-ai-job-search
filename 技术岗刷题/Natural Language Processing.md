# 100 Natural Language Processing (NLP) Interview Questions and Answers (Detailed)

Below are 100 interview questions focused on NLP, spanning fundamental concepts, classical techniques, and modern deep learning-based approaches. The questions progress from basics like tokenization and POS tagging to advanced topics like transformers, large language models, and practical applications.

---

### 1. What is NLP (Natural Language Processing)?
**Answer:**  
NLP is a field at the intersection of linguistics, computer science, and AI that enables machines to understand, interpret, and generate human language. Tasks include text classification, sentiment analysis, machine translation, and more. NLP algorithms process language as text or speech input, breaking it down into structures and patterns computers can manipulate, facilitating applications like chatbots, search engines, and voice assistants.

### 2. What is the difference between NLP and NLU (Natural Language Understanding)?
**Answer:**  
- **NLP:** Covers the full pipeline of processing natural language—understanding, analyzing, and generating language.
- **NLU:** Focuses specifically on interpreting meaning and understanding the user’s intent.  
NLU is a subset of NLP that deals with semantics and comprehension. While NLP might include tasks like tokenization or POS tagging, NLU aims to grasp deeper meaning, context, and user intent behind the text.

### 3. What are common preprocessing steps in NLP?
**Answer:**  
Preprocessing often includes:
- **Tokenization:** Splitting text into words or subwords.
- **Lowercasing:** Ensuring consistent case handling.
- **Stopword Removal:** Removing common words (like “the,” “and”) that don’t add meaning.
- **Stemming/Lemmatization:** Reducing words to their base or root form.
- **Punctuation and Number Handling:** Removing or normalizing special characters and numbers.
These steps transform raw text into a cleaner, standardized form suitable for downstream algorithms.

### 4. What is Tokenization and why is it important?
**Answer:**  
Tokenization is the process of splitting text into units called tokens, often words, subwords, or characters. It’s essential because most NLP models process text at the token level. Proper tokenization respects language boundaries, ensuring that words are correctly identified. Subword tokenization methods like Byte-Pair Encoding (BPE) handle rare words and reduce out-of-vocabulary issues.

### 5. Compare Stemming and Lemmatization.
**Answer:**  
Both reduce words to a base form:
- **Stemming:** Uses heuristic rules to chop word endings (e.g., “studies” → “studi”). Fast but can produce non-real words.
- **Lemmatization:** Uses vocabulary and morphological analysis to return the dictionary form (lemma) of a word (e.g., “studies” → “study”). Slower but more accurate, producing actual words.

### 6. What are Stopwords and why might you remove them?
**Answer:**  
Stopwords are common words like “the,” “is,” or “of” that occur frequently but carry little semantic meaning. Removing them can reduce noise and improve computational efficiency. However, for some tasks (like sentiment analysis), stopwords can be contextually important. Deciding to remove them depends on the specific application.

### 7. What is Bag-of-Words (BoW) representation?
**Answer:**  
BoW is a simple text representation where documents are seen as unordered collections of words. It records word frequencies without capturing grammar, syntax, or word order. Although simple and easy to implement, BoW loses contextual information and doesn’t handle synonyms or polysemy well.

### 8. How does TF-IDF improve on simple term frequency counts?
**Answer:**  
TF-IDF (Term Frequency–Inverse Document Frequency) weighs words by how important they are in a corpus. While term frequency counts how frequently a word appears, IDF downweights words common across many documents, emphasizing words that are more discriminative. TF-IDF often improves retrieval and text classification accuracy compared to raw counts.

### 9. Explain N-grams and their use in language modeling.
**Answer:**  
N-grams are sequences of N consecutive tokens. For example, bigrams are pairs of words, trigrams are triples. N-gram language models estimate the probability of a word given the previous N-1 words. While simple, N-grams capture local context and are foundational in tasks like autocomplete or speech recognition. However, they suffer from data sparsity and can’t handle long-range dependencies.

### 10. What are Word Embeddings?
**Answer:**  
Word embeddings map words into dense, low-dimensional vectors that capture semantic relationships. Unlike one-hot vectors, embeddings learned from data (e.g., Word2Vec, GloVe) represent similar words with similar vectors. This improves generalization and helps downstream tasks like classification, similarity searches, and semantic analysis.

### 11. How does Word2Vec learn embeddings?
**Answer:**  
Word2Vec uses either CBOW (Continuous Bag-of-Words) or Skip-gram architecture:
- **CBOW:** Predicts a word given its surrounding context words.
- **Skip-gram:** Predicts context words given a target word.
By training on large corpora, Word2Vec positions words with similar contexts closer in the embedding space, capturing semantic meaning efficiently.

### 12. Compare Word2Vec and GloVe embeddings.
**Answer:**  
- **Word2Vec:** Predictive model that uses local context windows to learn embeddings.
- **GloVe:** A count-based model using global co-occurrence statistics.  
GloVe uses a matrix factorization-like approach, capturing global corpus statistics. Word2Vec focuses on local context. Both produce high-quality embeddings, but GloVe often yields slightly more stable embeddings due to global information integration.

### 13. What is OOV (Out-of-Vocabulary) issue in NLP and how to handle it?
**Answer:**  
OOV occurs when a model encounters a token not seen during training, lacking a representation. Traditional word-level embeddings fail to represent these words. Solutions:
- Subword tokenization methods (BPE, SentencePiece) that split rare words into known subwords.
- Character-level models that build embeddings from characters.
- Using large pretrained language models with extensive vocabularies.

### 14. Explain Subword Tokenization (BPE).
**Answer:**  
Byte-Pair Encoding (BPE) merges frequent pairs of characters or subunits iteratively to form a vocabulary of subwords. This balances vocabulary size and coverage, reducing OOV words. For example, “unfamiliar” might be split into “un” + “fam” + “iliar,” enabling the model to understand rare words as compositions of known units.

### 15. What is POS (Part-of-Speech) tagging?
**Answer:**  
POS tagging assigns grammatical categories (noun, verb, adjective, etc.) to each token. It helps understand syntactic structure, informing downstream tasks like parsing, information extraction, or sentiment analysis. Traditional approaches use statistical models (HMMs, CRFs), while modern methods leverage neural networks.

### 16. What is Named Entity Recognition (NER)?
**Answer:**  
NER identifies and classifies named entities (persons, locations, organizations, dates) in text. It helps structure unstructured text, enabling tasks like knowledge base population or question answering. Models often use CRFs, LSTMs, or transformer-based architectures to capture context for accurate labeling.

### 17. How do Dependency Parsing and Constituency Parsing differ?
**Answer:**  
- **Dependency Parsing:** Finds grammatical relationships between words (who did what to whom). Each word is linked to a head word, forming a dependency tree.
- **Constituency Parsing:** Breaks sentences into nested constituents (phrases) following a hierarchical structure.  
Both parsing methods reveal syntactic structure but differ in their representation frameworks and applications.

### 18. What is a Language Model?
**Answer:**  
A Language Model predicts the likelihood of a word sequence, assigning probabilities to sequences of words. It powers tasks like speech recognition, machine translation, and text generation. Language models range from N-gram models to neural-based ones (RNN/LSTM, Transformers) that can generate fluent and coherent text.

### 19. How do RNN-based Language Models differ from N-gram models?
**Answer:**  
RNN-based models use hidden states to remember past words, allowing them to capture longer contexts without enumerating all N-grams. N-gram models become impractical for large contexts due to combinatorial explosion. RNNs (and LSTMs, GRUs) model variable-length dependencies more efficiently.

### 20. What is a Seq2Seq Model?
**Answer:**  
Seq2Seq models map an input sequence (e.g., a sentence in one language) to an output sequence (e.g., the translated sentence) using an encoder-decoder architecture. The encoder compresses the input into a context vector, and the decoder generates output step-by-step. This architecture forms the backbone of machine translation, text summarization, and other sequence transduction tasks.

### 21. Compare Greedy Decoding vs. Beam Search in Seq2Seq generation.
**Answer:**  
- **Greedy Decoding:** Picks the highest probability word at each step. Fast but can produce suboptimal translations because it doesn’t reconsider earlier choices.
- **Beam Search:** Maintains multiple candidate sequences and selects the best final sequence. It’s slower but improves output quality by exploring more possibilities than greedy decoding.

### 22. What is the Attention Mechanism in seq2seq models?
**Answer:**  
Attention allows the decoder to focus on relevant parts of the input at each output step, computing a weighted average of encoder states based on similarity to the decoder’s current state. This reduces the encoder’s burden to encode everything into one vector and improves translation accuracy, handling long sentences better than vanilla seq2seq without attention.

### 23. Explain the Transformer model’s key innovation.
**Answer:**  
The Transformer replaces recurrence and convolution with self-attention to model long-range dependencies in parallel. This parallel processing speeds up training and improves handling of long contexts. Its encoder-decoder architecture, with multi-head attention and feed-forward layers, became the foundation for state-of-the-art language models.

### 24. What are Pretrained Language Models (e.g., BERT)?
**Answer:**  
Pretrained models like BERT are trained on massive text corpora using self-supervised tasks (masked language modeling). They learn contextual embeddings that capture rich semantic information. By fine-tuning these models on downstream tasks (classification, NER, QA), performance improves drastically with minimal additional data and training time.

### 25. What is BERT, and how does it differ from previous LMs?
**Answer:**  
BERT (Bidirectional Encoder Representations from Transformers) uses masked language modeling and next sentence prediction tasks to learn bidirectional context. Unlike earlier LMs that read text left-to-right or right-to-left, BERT reads entire sequences at once (masking some tokens) to learn richer, more holistic representations.

### 26. How do you fine-tune BERT for a downstream task?
**Answer:**  
For classification, you typically add a task-specific head (e.g., a fully connected layer) on top of BERT’s final hidden states and train on labeled data. Fine-tuning adjusts all parameters to the new task. Minimal architectural changes are required because BERT’s embeddings and attention layers already learned general language patterns.

### 27. What is GPT (Generative Pre-trained Transformer)?
**Answer:**  
GPT is a unidirectional transformer-based model trained for language modeling (predicting the next word). By pretraining on large corpora, GPT develops strong generative capabilities. Fine-tuned GPT variants excel at text generation, completion, and increasingly complex NLP tasks when coupled with few-shot prompting.

### 28. Explain the concept of a Masked Language Model (MLM).
**Answer:**  
An MLM randomly masks certain tokens in the input and trains the model to predict those masked tokens. This technique encourages the model to learn bidirectional context. BERT popularized MLM, enabling the model to understand how each word relates to others in both directions.

### 29. Describe the Next Sentence Prediction (NSP) task in BERT.
**Answer:**  
NSP trains the model to determine if the second sentence in a pair follows logically from the first. BERT uses NSP to gain an understanding of sentence-level relationships and coherence. While controversial and sometimes replaced by other tasks, NSP was included originally to help BERT capture inter-sentence context.

### 30. What is SentencePiece, and how does it help tokenization?
**Answer:**  
SentencePiece is a language-independent subword tokenizer. It learns a vocabulary of subword units from text and segments text into these subwords. Unlike word-based tokenizers, SentencePiece can handle languages without spaces, reduce OOV issues, and create efficient, consistent vocabularies for complex scripts.

### 31. How can Byte-Pair Encoding (BPE) be used in NLP?
**Answer:**  
BPE starts with characters and iteratively merges the most frequent pairs into subwords. This forms a balanced vocabulary handling both frequent words and rare terms as compositional subwords. BPE reduces OOV problems and is widely used in Transformer-based models (like GPT) to efficiently represent large vocabularies.

### 32. What is a CRF (Conditional Random Field) and its use in NLP?
**Answer:**  
A CRF is a probabilistic model for labeling sequences (e.g., POS tagging, NER). It considers all possible labelings of a sequence and chooses the labeling with the highest conditional probability, factoring in dependencies between labels. CRFs often produce more consistent and globally optimal label sequences than independent classifiers.

### 33. Compare CRF and BiLSTM-CRF for NER tasks.
**Answer:**  
- **CRF alone:** Relies on hand-crafted features or simpler representations. Effective but may not capture complex patterns fully.
- **BiLSTM-CRF:** Uses a BiLSTM to produce contextual embeddings, then passes them into a CRF layer. This combination captures long-range dependencies and enforces label consistency, often achieving state-of-the-art accuracy in NER and other sequence labeling tasks.

### 34. Explain Sentiment Analysis and common approaches.
**Answer:**  
Sentiment Analysis identifies the sentiment (positive, negative, neutral) expressed in text. Early approaches used lexicons or bag-of-words with logistic regression. Modern methods employ word embeddings and deep models (BiLSTM, Transformers) for richer context understanding. Pretrained language models fine-tuned on sentiment datasets often achieve superior accuracy.

### 35. What is Text Classification, and which algorithms are commonly used?
**Answer:**  
Text Classification assigns predefined categories (topics, sentiments) to documents. Traditional methods use features like TF-IDF and train SVMs or logistic regressions. Neural methods use CNNs, RNNs, or Transformers to extract rich contextual embeddings. Pretrained models like BERT, fine-tuned on a classification dataset, now achieve top performance.

### 36. Explain the concept of Language Modeling as a Fundamental NLP task.
**Answer:**  
Language Modeling predicts the next word (or character) in a sequence, capturing syntax and semantics. It underpins many NLP tasks: a good language model can assist in text generation, machine translation, and provide embeddings for words. Pretrained language models form the basis of many advanced NLP systems.

### 37. What is a Character-Level Model, and when is it useful?
**Answer:**  
Character-level models process text as characters rather than words or subwords. They handle languages without clear word boundaries, avoid OOV issues, and adapt to misspellings or rare words. However, they are slower and need more data to learn meaningful patterns. Character-level approaches are useful in morphologically rich languages or noisy text.

### 38. How does a Seq2Seq model handle Machine Translation?
**Answer:**  
In machine translation, a seq2seq model encodes the source sentence into a context vector and decodes it into the target language. With attention, the decoder can focus on different source words at each target word generation step. This approach has largely replaced phrase-based statistical translation, achieving fluency and coherence.

### 39. What is Text Summarization, and which neural approaches exist?
**Answer:**  
Text Summarization condenses longer texts into shorter versions capturing key points. Neural approaches often involve seq2seq models:
- **Abstractive Summarization:** Generate new sentences capturing main ideas (like neural translation).
- **Extractive Summarization:** Select relevant sentences from the original text.  
Transformers and pretrained models fine-tuned on summarization tasks produce coherent, high-quality summaries.

### 40. Explain the concept of Word Sense Disambiguation (WSD).
**Answer:**  
WSD identifies which sense of a word is intended in a given context when the word has multiple meanings. Approaches range from dictionary-based methods to supervised classification using contextual embeddings. Modern methods often leverage pretrained language models that encode rich context, making sense prediction more accurate.

### 41. How do POS Tagging and Parsing benefit downstream NLP tasks?
**Answer:**  
POS tagging identifies grammatical roles of words, aiding syntactic understanding. Parsing (dependency or constituency) reveals sentence structure. This structural knowledge helps tasks like information extraction, question answering, or entity recognition by providing clues about relationships between words and phrases.

### 42. What is Coreference Resolution?
**Answer:**  
Coreference resolution identifies when different mentions (e.g., “John,” “he,” “the man”) refer to the same entity. It’s crucial for understanding context and maintaining coherence in tasks like summarization, QA, and dialog. Neural methods often use contextual embeddings and attention to align mentions with entity representations.

### 43. Compare Rule-based and Statistical/Neural Methods in NLP.
**Answer:**  
- **Rule-based:** Depend on hand-crafted linguistic rules. Interpretable but brittle and hard to scale to many languages or domains.
- **Statistical/Neural:** Learn patterns from data. More robust, scale to large corpora, often outperform rules, but less interpretable and require labeled data and computational resources.

### 44. What are Language Agnostic approaches in NLP?
**Answer:**  
Language-agnostic approaches rely on universal principles, character-based models, or multilingual embeddings that don’t assume a particular language’s structure. These help handle low-resource languages or tasks requiring cross-lingual transfer without extensive language-specific engineering.

### 45. Explain the concept of a BiLSTM in NLP.
**Answer:**  
A BiLSTM is a bidirectional LSTM that processes the input from left-to-right and right-to-left. Combining both directions captures context from both preceding and following words. This is crucial for understanding ambiguous words that depend on context. BiLSTMs are common in POS tagging, NER, and other sequence labeling tasks.

### 46. How do neural embeddings capture semantic similarity between words?
**Answer:**  
Embeddings map words into a continuous vector space where semantic similarity correlates with vector proximity. Similar words appear in similar contexts, so training embedding models arranges synonyms close together. For instance, “king” and “queen” are closer to each other than to unrelated words like “car,” reflecting semantic relationships.

### 47. What is Fine-Tuning vs. Feature Extraction approach using pretrained models?
**Answer:**  
- **Fine-Tuning:** Update all or most layers of a pretrained model on a new task, adapting parameters to the specific task.
- **Feature Extraction:** Freeze the pretrained model’s weights and use it as a fixed feature extractor. A simpler classifier on top uses those features.  
Fine-tuning often yields better performance if you have enough data, while feature extraction is faster and simpler.

### 48. Explain Zero-Shot Classification in NLP.
**Answer:**  
Zero-shot classification predicts labels not seen during training by leveraging semantic information (e.g., descriptions of classes). Pretrained language models can understand and match new labels’ descriptions to input text, classifying without task-specific examples. This approach generalizes beyond labeled training categories.

### 49. What is the role of Convolutional Neural Networks in NLP?
**Answer:**  
Before RNNs and Transformers dominated, CNNs processed text (like character-level embeddings or short text classification) by extracting local n-gram features. CNNs are still useful for tasks where local patterns matter (e.g., sentence-level classification). They are faster and simpler than RNNs but handle long dependencies less effectively.

### 50. How do Attentional Models improve Document Classification?
**Answer:**  
Attentional models weigh different parts of a document differently when making a classification. This focuses the model on the most relevant words or sentences. It improves interpretability and performance, allowing the model to “explain” which parts of text influenced the final classification decision.

### 51. What is Sentence Embedding and how does it differ from Word Embedding?
**Answer:**  
Sentence embeddings encode entire sentences into fixed-length vectors, capturing overall meaning beyond individual word semantics. While word embeddings represent single words, sentence embeddings use context and word interactions to represent the entire sentence’s semantics, enabling tasks like semantic similarity or sentence-level classification.

### 52. How does Universal Sentence Encoder differ from Word2Vec?
**Answer:**  
- **Word2Vec:** Produces embeddings for individual words.
- **Universal Sentence Encoder (USE):** Creates embeddings for entire sentences. Trained on large corpora and various tasks, USE can measure sentence-level semantic similarity out-of-the-box. This makes it more suitable than Word2Vec for sentence-level tasks like semantic search or QA.

### 53. Explain the concept of Contextual Word Embeddings (e.g., ELMo).
**Answer:**  
ELMo (Embeddings from Language Models) provides context-dependent embeddings. A word’s vector depends on its sentence context, so polysemous words get different embeddings depending on usage. This contrasts with static embeddings like Word2Vec, where each word has one vector regardless of context. Contextual embeddings enhance performance in tasks that rely on nuanced word meanings.

### 54. Compare ELMo, BERT, and GPT embeddings.
**Answer:**  
- **ELMo:** Uses bidirectional LSTM language models, producing contextual embeddings for each word.
- **BERT:** Transformer-based, masked language model producing deeply contextualized embeddings. Bidirectional context and can be fine-tuned for downstream tasks.
- **GPT:** Unidirectional transformer LM focusing on next-word prediction. Good at generation and language understanding but less symmetric than BERT for certain tasks.

### 55. What is Sentence-level Pretraining and how is it exemplified by models like Sentence-BERT?
**Answer:**  
Sentence-level pretraining focuses on generating embeddings for entire sentences that reflect semantic similarity. Sentence-BERT, for example, modifies BERT’s architecture and training to produce embeddings that can be compared using cosine similarity. This benefits tasks like semantic search, duplicate question detection, or textual entailment.

### 56. How is NER approached with Neural Networks?
**Answer:**  
Commonly, a BiLSTM processes token embeddings (possibly combined with character-level features), and a CRF layer predicts the optimal label sequence. With transformers, a fine-tuned BERT model directly outputs token-level label probabilities. Both approaches rely on contextual embeddings that capture richer linguistic nuances than feature-engineered methods.

### 57. What is a Multi-Task Learning approach in NLP?
**Answer:**  
Multi-Task Learning trains a model on multiple related NLP tasks (e.g., POS tagging, NER, sentence classification) simultaneously. The model’s shared layers learn general language representations, while task-specific heads produce outputs. This often improves overall performance and data efficiency, as the model leverages complementary information across tasks.

### 58. Explain Conditional Text Generation tasks (like conditional language modeling).
**Answer:**  
Conditional text generation involves generating text based on given context or conditions, such as prompts, topics, or input sequences. For example, machine translation is conditional on a source sentence. Summarization is conditional on an input document. The model’s output depends on the provided conditioning information.

### 59. What are the challenges of Dialogue Systems (Chatbots) in NLP?
**Answer:**  
Dialogue systems must:
- Handle context across multiple turns.
- Manage personality, style, and factual consistency.
- Understand and generate coherent, contextually relevant responses.
- Possibly integrate external knowledge for accurate answers.
Balancing these challenges requires robust language models, dialogue state tracking, and sometimes knowledge bases.

### 60. Explain the difference between Closed-Book and Open-Book QA.
**Answer:**  
- **Closed-Book QA:** The model answers questions using only its internal knowledge learned during training. It doesn’t have access to external documents at inference.
- **Open-Book QA:** The system retrieves relevant documents (from a knowledge base or search engine) and reads them to find the answer.
Open-book QA emphasizes retrieval and reading comprehension, while closed-book QA relies heavily on memorized knowledge.

### 61. What is a Knowledge Graph and how is it integrated with NLP?
**Answer:**  
A Knowledge Graph (KG) represents entities and their relationships as a graph. NLP can leverage KGs to improve entity disambiguation, QA, and recommendation by grounding language understanding in factual knowledge. Integrating embeddings from KGs and text enhances models with structured, explicit knowledge.

### 62. Explain the concept of Word Sense Disambiguation and Modern Approaches.
**Answer:**  
WSD determines which sense of an ambiguous word is meant. Modern approaches leverage contextual embeddings (like from BERT) to represent each occurrence of the word. By clustering or comparing these embeddings against sense definitions or labeled examples, models pick the correct sense. This outperforms older dictionary or rule-based methods.

### 63. How does QA differ from Information Retrieval (IR)?
**Answer:**  
- **IR:** Finds relevant documents or passages that may contain the answer.
- **QA:** Extracts or generates the specific answer from provided text or from its learned representations.  
IR returns documents; QA returns direct answers. Many QA systems combine IR (to retrieve context) with reading comprehension models that extract precise answers.

### 64. What is the Transformer Encoder vs. Decoder difference in architectures like BERT and GPT?
**Answer:**  
- **Encoder:** Processes input sequences and builds contextual representations. BERT uses only the encoder stack, focusing on understanding input text.
- **Decoder:** Generates output step-by-step, attending to encoder outputs and previously generated tokens. GPT uses only the decoder stack, focusing on generative tasks.  
Full seq2seq Transformers (e.g., for translation) combine both encoder and decoder.

### 65. Explain Beam Search vs. Greedy Search in Machine Translation.
**Answer:**  
Greedy search picks the highest probability word at each step, potentially missing the optimal global sequence. Beam search keeps multiple candidates (the beam) at each step, exploring more possibilities to find a higher quality translation. Beam search trades off computational cost for improved output quality.

### 66. How do pretrained language models like BERT improve low-resource tasks?
**Answer:**  
Pretrained models capture general linguistic knowledge, reducing the data needed for fine-tuning. For low-resource tasks or languages, fine-tuning a pretrained model yields better performance than training from scratch. The model already “knows” a lot about language structure and semantics, compensating for limited in-domain training data.

### 67. Explain the concept of a Masked Language Modeling objective.
**Answer:**  
Masked LM replaces some tokens in the input with a mask token and trains the model to predict the masked words. This teaches the model to use bidirectional context to guess missing words, learning powerful contextual embeddings. BERT’s success stems largely from the MLM objective.

### 68. How does Sentence-level Pretraining (e.g., STS tasks) enhance embeddings?
**Answer:**  
Sentence-level pretraining trains models on tasks like sentence similarity or next sentence prediction. This encourages the model to produce embeddings that capture entire sentence meanings rather than just local word contexts. The resulting sentence embeddings are more directly applicable to tasks like semantic search and textual entailment.

### 69. What is a Code-Switched text, and why is it challenging?
**Answer:**  
Code-switching involves mixing two or more languages in a single utterance. Models must handle multiple vocabularies, grammar rules, and language boundaries simultaneously. This complexity makes tokenization, embedding, and language modeling harder, often requiring language identification and specialized multilingual embeddings.

### 70. How does language model pretraining differ for multilingual models like mBERT?
**Answer:**  
Multilingual BERT (mBERT) is pretrained on text from multiple languages simultaneously, learning a shared multilingual vocabulary and embeddings. By absorbing patterns from diverse languages, it can transfer knowledge across languages, enabling zero-shot or few-shot performance in low-resource languages.

### 71. What is Machine Translation and what are current SOTA approaches?
**Answer:**  
Machine Translation converts text from one language to another. Current SOTA approaches use Transformer-based seq2seq models with attention and large-scale pretraining. They often rely on massive parallel corpora, and multilingual systems can translate multiple language pairs with a single model (e.g., M2M-100).

### 72. Explain Extractive vs. Abstractive Summarization.
**Answer:**  
- **Extractive:** Selects important sentences or phrases from the original text. Straightforward but limited by source phrasing.
- **Abstractive:** Generates summaries that may include paraphrasing and new wording. More flexible, can produce more coherent and concise summaries but is more challenging due to language generation complexity.

### 73. What is Text Classification and why are Transformers effective for it?
**Answer:**  
Text Classification assigns labels (topics, sentiment, category) to documents. Transformers, pretrained on massive corpora, provide contextual embeddings that capture nuanced meanings. Fine-tuning a transformer on a classification dataset yields state-of-the-art performance, often surpassing previous RNN-based or feature-based methods.

### 74. How can Entity Linking benefit from NLP techniques?
**Answer:**  
Entity Linking maps entity mentions in text to canonical entities in a knowledge base. NLP helps by:
- Identifying mentions via NER.
- Using context from embeddings to disambiguate entities.
- Matching entities with similar names or attributes.  
Advanced language models understand context better, improving entity linking accuracy.

### 75. Explain the concept of Textual Entailment.
**Answer:**  
Textual Entailment determines if a premise logically implies a hypothesis. If the hypothesis must be true given the premise, we have entailment; if not, contradiction or neutral. Modern transformers fine-tuned on NLI (Natural Language Inference) datasets solve textual entailment, aiding QA, inference, and reasoning tasks.

### 76. How do Conversational Agents handle context?
**Answer:**  
Conversational agents use context modeling techniques like RNNs, Transformers, or attention over conversation history. They maintain state tracking variables (for slot-filling dialogues) or rely on memory networks to recall past turns. Large language models store contextual cues internally, allowing coherent multi-turn dialogues.

### 77. What are Polyglot embeddings?
**Answer:**  
Polyglot embeddings are multilingual word embeddings trained on large multilingual corpora. They map words from different languages into a shared embedding space, enabling cross-lingual transfer, bilingual dictionary induction, or zero-shot multilingual tasks.

### 78. Explain the concept of Domain Adaptation in NLP.
**Answer:**  
Domain Adaptation tailors a general model trained on broad data (e.g., news text) to perform better in a specific domain (e.g., medical text). It may involve fine-tuning on domain-specific corpora, adjusting embeddings, or using domain adaptation techniques like adversarial training. This improves model accuracy and relevance in specialized contexts.

### 79. How can you handle sarcasm or irony in sentiment analysis?
**Answer:**  
Sarcasm often contradicts literal interpretation of words. Handling it requires:
- Contextual cues beyond words (hashtags, emojis, punctuation).
- Domain knowledge or multimodal signals (tone of voice).
- Pretrained language models that understand subtle lexical or syntactic patterns indicative of sarcasm.
Fine-tuning on sarcasm-labeled data and using contextual embeddings improves detection.

### 80. What is a Multi-Head Attention mechanism in Transformers?
**Answer:**  
Multi-Head Attention uses multiple parallel attention heads. Each head focuses on different parts of the input, capturing various types of relationships (e.g., syntactic vs. semantic). Combining them yields richer representations. This allows Transformers to learn multiple aspects of language dependencies simultaneously.

### 81. Explain the concept of Positional Encoding in Transformers.
**Answer:**  
Positional encodings inject sequence order information into word embeddings since Transformers lack recurrence. Typically using sine and cosine functions at different frequencies, positional encodings let the model differentiate between “dog chased cat” and “cat chased dog” by providing token position awareness.

### 82. How does Summarization evaluation differ from classification evaluation?
**Answer:**  
Summarization often uses ROUGE scores comparing n-grams of generated summaries to references. Classification uses accuracy or F1-scores for discrete labels. Summarization quality is more subjective and harder to measure, often requiring lexical overlap (ROUGE) or semantic similarity (BERTScore) rather than simple correctness.

### 83. Explain BPE-based subword tokenization in detail.
**Answer:**  
BPE starts with a character-level vocabulary and iteratively merges the most frequent character pairs into subwords. Over multiple merges, it builds a vocabulary balancing granularity and coverage. This lets models represent rare words as sequences of known subwords, reducing OOV and improving handling of rich morphological languages.

### 84. What is BERTScore, and how is it used for text evaluation?
**Answer:**  
BERTScore computes similarity between machine-generated text and a reference by comparing contextual embeddings from a pre-trained model. Instead of exact word matches (like ROUGE), BERTScore measures semantic similarity. It’s more robust to paraphrases or lexical variations, often correlating better with human judgments.

### 85. Explain the concept of a Knowledge-Enhanced Language Model.
**Answer:**  
These models integrate structured knowledge (from knowledge bases or triples) into language model architectures. They might incorporate entity embeddings, graph attention, or use knowledge retrieval modules to produce factually accurate and context-rich answers. This improves factual consistency in tasks like QA.

### 86. How does Attention differ from simple weighted averaging of context?
**Answer:**  
Attention computes a weighted combination of values (contextual representations) using learned query-key-value structures. It dynamically focuses on relevant parts of the input at each step, guided by similarity (dot products) between queries and keys. This selective mechanism outperforms static averaging, capturing nuanced context-sensitive relationships.

### 87. What are the challenges of Low-Resource Languages in NLP?
**Answer:**  
Low-resource languages lack large corpora or annotated datasets. This makes training high-performing models challenging. Techniques include transfer learning from high-resource languages, multilingual pretraining, or leveraging parallel corpora. Active learning, data augmentation, and unsupervised methods also help close the resource gap.

### 88. How do you measure Embedding Quality?
**Answer:**  
Intrinsic evaluations:
- Word similarity tasks: Check if similar words have close vectors.
- Analogy tasks: Evaluate if embeddings capture relationships (king - man + woman = queen).
Extrinsic evaluations:
- Use embeddings in downstream tasks (classification, NER) to see performance changes.
Quality is judged by both intrinsic correlation with human judgments and extrinsic improvements in NLP tasks.

### 89. Compare Extractive vs. Neural End-to-End (Abstractive) QA.
**Answer:**  
- **Extractive QA:** Identifies spans from a provided passage. The answer is always a substring. Easy to evaluate, but limited to original text.
- **Abstractive QA:** Generates answers not necessarily present verbatim in the text. More flexible and human-like, but harder and more prone to factual errors. Transformers with generation capabilities handle abstractive QA tasks.

### 90. What is Cross-Lingual Transfer in NLP?
**Answer:**  
Cross-lingual transfer uses resources (e.g., pretrained models, annotated data) from one language to improve performance in another language. Techniques include training multilingual models, translating training data, or leveraging universal subword vocabularies. This helps address languages with minimal annotated data.

### 91. Explain the concept of Document-level Context in NLP tasks.
**Answer:**  
Many NLP tasks consider sentence-level inputs. Document-level context uses entire documents to interpret sentences more accurately, resolving ambiguities in pronouns, references, or topic shifts. Models must handle longer inputs and track coherence across multiple sentences, often using hierarchical models or attention over multiple sentences.

### 92. What is BPE-Dropout?
**Answer:**  
BPE-Dropout introduces randomness during subword segmentation. At training time, merges are probabilistically undone, producing different subword segmentations of the same input. This enhances robustness, regularizing the model by exposing it to varied decompositions and reducing over-reliance on a single tokenization scheme.

### 93. How do Neural Spell Checkers or Grammatical Error Correction models work?
**Answer:**  
These models often use sequence-to-sequence frameworks. Given an input sentence with errors, the model generates a corrected version. By training on pairs of incorrect and corrected sentences, models learn to fix spelling mistakes and grammatical errors. Attention-based transformers perform particularly well, capturing contextual clues to correct subtle errors.

### 94. Explain Nucleus Sampling vs. Greedy and Beam Search in text generation.
**Answer:**  
Nucleus Sampling (top-p sampling) chooses from the smallest set of words whose cumulative probability exceeds p. Unlike greedy or beam search (which pick high-probability words), nucleus sampling introduces controlled randomness for more diverse, less deterministic text generation. It balances quality and creativity in generated outputs.

### 95. What is a Slot-Filling task in Dialogue Systems?
**Answer:**  
Slot-filling identifies key pieces of information (slots) from user utterances, like a destination city or travel date in a booking scenario. Models often use NER-like approaches to label tokens with slot types. Accurate slot-filling is critical for dialogue managers to understand user requests and provide correct responses or actions.

### 96. How do Hybrid Models combining Rules and Neural Methods help in NLP?
**Answer:**  
Hybrid approaches use rules to handle straightforward patterns or ensure compliance (like date formats), while neural models tackle ambiguous or context-heavy parts. This synergy improves reliability, interpretability, and can reduce errors where neural models struggle without constraints, achieving better overall system performance.

### 97. What is a Hallucination in text generation models?
**Answer:**  
Hallucination occurs when a generation model produces content that is factually incorrect or unrelated to the input. Large language models sometimes create plausible but false statements. Mitigating hallucination involves grounding models in knowledge bases, using fact-checking modules, or applying constraints during decoding.

### 98. How do you evaluate conversational agents?
**Answer:**  
Conversational agents are evaluated using:
- Automatic metrics: BLEU, METEOR, or perplexity for response quality.
- Human evaluations: Judging coherence, relevance, and fluency.
- Task success rate: For goal-oriented dialogs, measuring how often the agent satisfies user requests.
No single metric perfectly captures dialogue quality, often requiring multiple measures.

### 99. What is a Knowledge-Intensive NLP Task?
**Answer:**  
Knowledge-intensive tasks require external factual or domain knowledge beyond what’s contained in training text. Examples: QA about rare facts, domain-specific technical questions. Models often integrate retrieval mechanisms or knowledge graphs to answer queries that cannot be solved by language patterns alone.

### 100. Summarize current trends in NLP.
**Answer:**  
NLP increasingly relies on large pretrained models (like BERT, GPT), fine-tuned for specific tasks. Methods incorporate better tokenization (subwords), handle longer contexts (Transformers), integrate external knowledge (RAG models), and support zero-shot or few-shot learning. Efficiency techniques (distillation, quantization) address deployment constraints. The field continues evolving toward more robust, general, and contextually aware systems.

---

These 100 questions and answers cover essential NLP concepts, from basic preprocessing and classical representations (TF-IDF, N-grams) to advanced neural architectures (Transformers, pretrained language models) and key applications (NER, QA, Summarization), providing a comprehensive foundation for NLP interviews.
