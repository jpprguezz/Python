def run(input_path: str, lower_bound: int) -> dict:
    f = open(input_path, 'r')
    freq = {}
    for line in f:
        line_words = line.lower().split()
        for word in line_words:
            word_count = line_words.count(word)
            if word_count >= lower_bound:
                freq[word] = word_count

    return freq


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
