def word_count(sentence):
    words = sentence.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


sentence = "apple banana apple orange banana apple"
print(word_count(sentence))
