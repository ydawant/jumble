#!/usr/local/bin/python

def create_word_dict(word_file):
    with open(word_file, "r") as lines:
        word_dict = {}
        #strips out new lines and filters out single letter words, didn't think they were necessary.
        lines = filter(lambda line: len(line) > 1, map(lambda line: line.rstrip("\n"), lines))
        word_dict = {}
        for line in lines:
            #maps sorted letter values to word Ex. word_dict['dgo'] = ['dog', 'god', 'God']
            sorted_line = ''.join(sorted(line.lower()))
            word_dict.setdefault(sorted_line, []).append(line)
    return word_dict

def get_words(word_dict):
    letters = raw_input("Input letters: ")
    total_words = []
    #start at 2, because we don't need combos of single letters.
    for i in range(2, len(letters)+1):
        combos = comb(i, letters)
        #slightly busy, but this simply adds the word to our total_words if there is a value.
        map(lambda word: total_words.append(word),
            filter(lambda words: words is not None, [word_dict.get(''.join(sorted(combo)).lower()) for combo in combos]))

    #flattens our answer list.
    return [word for sublist in total_words for word in sublist]

#http://rosettacode.org/wiki/Combinations#Python
#grabbed the combinations code off of Rosetta Code, can explain how it works if needed.
def comb(m, lst):
    if m == 0:
        return [[]]

    return [[x] + suffix for i, x in enumerate(lst)
            for suffix in comb(m - 1, lst[i + 1:])]

if __name__ == '__main__':
    #create the dict before we ask for input, makes getting results faster.
    word_dict = create_word_dict("words.txt")
    print get_words(word_dict)