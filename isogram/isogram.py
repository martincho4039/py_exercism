def is_isogram(string):
    is_the_word_isogram = True
    for i in range(len(string)):
        if ord(string[i]) == 32 or ord(string[i]) == 45:
            continue
        elif string.casefold().count(string.casefold()[i]) > 1:
            is_the_word_isogram = False
            break
    return(is_the_word_isogram)
