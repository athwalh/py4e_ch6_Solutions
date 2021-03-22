def count(w,l):
    value = 0
    for letter in w:
        if letter == l:
            value = value + 1

    print('Letter count: ', value)

word = input('Please enter a word: ')
letter = input('Please enter a letter: ')

count(word,letter)
