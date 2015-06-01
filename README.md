This is my solution to a word jumble.

How it works:

The first step is we ask for an input from the user, which is just the letters they choose to run this program with.

The second step is creating a dictionary that maps the sorted letters in a word to the unsorted letters. The reason
to do this is so that we can do combinations as opposed to permutations through the given letters, saving us time. A
certain key can of course have many values, but we will only need to see the one combination as we know that it is
sorted alphabetically. I pruned out all the single letters, as I felt that cluttered the results. The word list is just
the word list that is provided with OSX (/usr/share/dict/words)

The third step is generating all the possible combinations, running through them, and seeing if those keys exist in
our dictionary. If they do, we append the results to our results array, and at the end, we flatten our array, as our
values are all lists. We then take the unique answers, as words with double letters can create the same results mutiple times as combinations are based off of position and not value.

To run the tests, just run the executable tests.py file from the command line.
