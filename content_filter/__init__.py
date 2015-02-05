import inspect
import os
import string

separators = ['.', ',', ';', '\n']
word_list = []
filename = '5000_processed_usable_english_words'

def get_word_list():
    """caches the list for later use... at the module level... like some
    weird singleton pattern
    """
    global word_list
    if not word_list:
        path = os.path.join(os.path.dirname(
                inspect.getfile(inspect.currentframe())
                ), filename)
        
        f = open(path)
        word_list = [word[:-1] for word in f.readlines()[1:] if not word.startswith('#')]

    return word_list

def text_tokenizer(text):
    """Given a text, splits it into manageable pieces.
    """
    return text.split(separators[0])


def get_interesting_factor(phrase):
    """Given a small text piece, determine its absolute interesting factor.

    Absolute contrasts with relative.

    This is one of the money functions... the score given by it will make
    phrases more or less interesting, compared to the others
    """
    factor = 0.0
    word_list = get_word_list()
    phrase_words = phrase.split(' ')

    #import ipdb; ipdb.set_trace()
    for word in phrase_words:
        if word in word_list:
            factor += (len(word_list) - word_list.index(word))
    
    factor /= len(phrase_words)

    # this is really crude. Should really find out a way to make
    # numbers seem more interesting
    factor -= len([ch for ch in phrase if ch.isdigit()])

    return factor
