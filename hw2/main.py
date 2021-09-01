if __name__ == '__main__':
    words = input('> ').split()
    unique_words = set()

    for word in words:
        if word in unique_words:
            continue
        unique_words.add(word)
        print(word, end=' ')
