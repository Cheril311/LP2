import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')

# Step 1: Tokenization
text = "I will walk 500 miles and I would walk 500 more, just to be the man who walks a thousand miles to fall down at your door!"
tokens = nltk.word_tokenize(text)
print("Tokens:", tokens)

# Step 2: Count Word Frequency
word_freq = Counter(tokens)
print("Word Frequency:", word_freq)

nltk.download('stopwords')

# Step 3: Remove Stop Words
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.casefold() not in stop_words]
print("Filtered Tokens:", filtered_tokens)

#nltk.download('averaged_perceptron_tagger')

# Step 4: POS Tagging
pos_tags = nltk.pos_tag(filtered_tokens)
print("POS Tagging:", pos_tags)
