def abbr(phrase):
    words_of_phrase = phrase.split()
    abbr = ""
    for currentWord in words_of_phrase:
        if currentWord and currentWord[0].isalpha():
            abbr += currentWord[0].upper()

    return abbr

phrase = "otgijbmdifh fiudfv peu"
print(abbr(phrase))
