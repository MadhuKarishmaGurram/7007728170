from collections import Counter
import re

# ---------- BPE helper functions ----------

def symbols(word):
    """Return characters plus the end-of-word marker."""
    return list(word) + ["_"]

def pair_counts(vocab):
    """Count adjacent symbol pairs, weighted by word frequency."""
    counts = Counter()
    for seq, freq in vocab.items():
        for i in range(len(seq) - 1):
            counts[(seq[i], seq[i + 1])] += freq
    return counts

def merge_pair(seq, pair):
    """Merge every occurrence of one adjacent pair."""
    out = []
    i = 0
    while i < len(seq):
        if i + 1 < len(seq) and (seq[i], seq[i + 1]) == pair:
            out.append(seq[i] + seq[i + 1])
            i += 2
        else:
            out.append(seq[i])
            i += 1
    return out

def learn_bpe(words, num_merges):
    """Learn the most frequent adjacent pair at each BPE step."""
    vocab = Counter(tuple(symbols(w)) for w in words)
    merges = []
    print("Initial vocabulary size:", len(set(x for s in vocab for x in s)))

    for step in range(1, num_merges + 1):
        counts = pair_counts(vocab)
        if not counts:
            break
        pair, count = counts.most_common(1)[0]
        merges.append(pair)

        new_vocab = Counter()
        for seq, freq in vocab.items():
            new_vocab[tuple(merge_pair(list(seq), pair))] += freq
        vocab = new_vocab

        token_set = set(x for s in vocab for x in s)
        print(f"Step {step:02d}: top pair={pair}, count={count}, vocabulary size={len(token_set)}")

    return merges, vocab

def segment(word, merges):
    """Apply learned BPE merges to a new word."""
    seq = symbols(word)
    for pair in merges:
        seq = merge_pair(seq, pair)
    return seq

# ---------- Q2.2: Required toy corpus ----------

toy_corpus = """
low low low low lowest lowest
newer newer newer newer newer newer
wider wider wider new new
"""
toy_words = toy_corpus.split()

print("\n===== Q2.2 MINI-BPE =====")
merges, final_vocab = learn_bpe(toy_words, 20)

print("\nSegmentations:")
for word in ["new", "newer", "lowest", "widest", "newestest"]:
    print(f"{word} -> {segment(word, merges)}")

# ---------- Q2.3: English paragraph ----------

paragraph = """
Natural language processing helps computers understand human language.
Tokenization separates words punctuation and contractions.
Students learn from examples and compare patterns across sentences.
Thoughtful preprocessing improves reliable models for practical language tasks.
Reusable subwords help learners analyze uncommon words and inflected forms.
"""

words = re.findall(r"[a-z]+", paragraph.lower())

print("\n===== Q2.3 BPE ON ENGLISH PARAGRAPH =====")
p_merges, p_vocab = learn_bpe(words, 30)

print("\nFive selected merges:")
for i, pair in enumerate(p_merges[:5], 1):
    print(f"{i}. {pair}")

tokens = set(x for seq in p_vocab for x in seq)
longest = sorted(tokens, key=lambda x: (-len(x), x))[:5]

print("\nFive longest resulting subword tokens:")
for token in longest:
    print(token)

print("\nFive segmentations:")
for word in ["language", "tokenization", "uncommon", "inflected", "learners"]:
    print(f"{word} -> {segment(word, p_merges)}")
