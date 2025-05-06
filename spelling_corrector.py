import re
from collections import Counter

class SpellingCorrector:
    def __init__(self, corpus_file='data/big.txt'):
        self.WORDS = Counter(self.words(open(corpus_file).read()))
        self.N = sum(self.WORDS.values())
        print(f"[INFO] Loaded corpus with {len(self.WORDS)} unique words.")

    def words(self, text):
        return re.findall(r"[a-zA-Z]+", text.lower())

    def P(self, word):
        V = len(self.WORDS)
        return (self.WORDS[word] + 1) / (self.N + V)  # Laplace smoothing

    def correction(self, word):
        candidates_list = self.candidates(word)
        return max(candidates_list, key=lambda w: (self.P(w), -self.levenshtein_distance(word, w)))

    def candidates(self, word):
        return (self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word])

    def known(self, words_set):
        return set(w for w in words_set if w in self.WORDS)

    def edits1(self, word):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word):
        return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

    def levenshtein_distance(self, s1, s2):
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)
        if len(s2) == 0:
            return len(s1)
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

    def correct_text(self, text):
        tokens = self.words(text)
        corrected_tokens = [self.correction(token) for token in tokens]
        return ' '.join(corrected_tokens)