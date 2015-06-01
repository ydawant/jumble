#!/usr/local/bin/python

def create_word_dict(word_file):
    with open(word_file, "r") as lines:
        word_dict = {}
        for line in lines:
            line = line.rstrip("\n")
            #pruned our single letters - felt it cluttered results, if needed, just remove this if statement.
            if len(line) > 1:
                #maps sorted letter values to word Ex. word_dict['dgo'] = ['dog', 'god', 'God']
                sorted_line = ''.join(sorted(line.lower()))
                word_dict.setdefault(sorted_line, []).append(line)
    return word_dict

def get_words(words_txtfile):
    letters = raw_input("Input letters: ")
    word_dict = create_word_dict(words_txtfile)
    total_words = []
    #start at 2, because we don't need combos of single letters.
    for i in range(2, len(letters)+1):
        combos = comb(i, letters)
        for combo in combos:
            words = word_dict.get(''.join(sorted(combo)).lower())
            if words != None:
                total_words.append(words)

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
    print get_words("words.txt")