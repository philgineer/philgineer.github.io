from collections import defaultdict, Counter

def get_pair_stat(vocab):
    stats = defaultdict(int)
    vocab_counted = Counter(vocab)
    for word, freq in vocab_counted.items():
        symbols = list(word)
        for i in range(len(symbols)-1):
            stats[symbols[i], symbols[i+1]] += freq
    return stats


vocab = ["hello", "world"]
print(get_pair_stat(vocab))

h el l o