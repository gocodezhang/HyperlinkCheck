from nltk import word_tokenize, pos_tag
import logging

logger = logging.getLogger('nltk')


def pos_phrase(s: str):
    logging.info('pos_phrase(): %s', s)
    tags = pos_tag(word_tokenize(s))

    # add noun or verb if only one tag
    if (len(tags) == 1):
        return [tag[0] for tag in tags if tag[1].startswith('NN') or tag[1].startswith('VB')]

    prev_is_noun = False
    nouns = []
    for tag in tags:
        if (tag[1].startswith('NN') and len(tag[0]) > 1):
            if (prev_is_noun):
                # add curr noun into prev when prev word is also a noun
                nouns[-1] = nouns[-1] + ' ' + tag[0]
            else:
                # add a new noun
                nouns.append(tag[0])
            prev_is_noun = True
        else:
            prev_is_noun = False

    return nouns
