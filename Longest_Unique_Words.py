def get_n_longest_unique_words(words, n):
    # Write your code here.
    unique_words = []
    for word in words:
        if words.count(word) == 1:
            unique_words.append(word)

    longest_unique_words = sorted(unique_words, key=len, reverse=True)

    return longest_unique_words[:n]