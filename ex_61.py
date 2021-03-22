index = 0
inverse = -1

test = input('Enter word: ')

while index < len(test):

    letter = test[inverse]
    print(letter)
    index = index + 1
    inverse = inverse - 1
