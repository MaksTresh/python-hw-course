from collections import Counter


if __name__ == '__main__':
    words = input('> ').lower().split()
    words_count = Counter(words)
    max_word_length = max(words_count.values())
    for word, length in words_count.items():
        if length == max_word_length:
            print(f'{length} - {word}')
