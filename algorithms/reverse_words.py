def reverse_words_in_list(words_list):


    reverse_words = []
    words = []
    for letters in words_list:

        if letters == '':
            reverse_words += [''.join(words)]
            words = []
            continue
        words += letters

    reverse_words += [''.join(words)]

    reverse_words1 = []

    for i in range(len(reverse_words)-1, -1, -1):
        reverse_words1 += [reverse_words[-i]]

    return reverse_words1

print(reverse_words_in_list(['a','b','','z']))