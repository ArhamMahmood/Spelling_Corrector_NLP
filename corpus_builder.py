def build_corpus(input_file, output_file='data/data.txt'):
    import re
    from collections import Counter
    with open(input_file, 'r') as infile:
        text = infile.read().lower()
        words = re.findall(r"[a-zA-Z]+", text)
    counter = Counter(words)
    with open(output_file, 'w') as outfile:
        for word, freq in counter.items():
            outfile.write((word + ' ') * freq)
    print(f"[INFO] Corpus built and saved to {output_file}.")

# Example usage
# build_corpus('data/my_raw_texts.txt')