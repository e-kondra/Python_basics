from random import shuffle

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, no_repeat=False):
    """
    Return a list of n jokes, building from 3 lists of different words
    without repeats of word(no_repeat = True) or with repeats (no_repeat defaults False)
    """
    jokes_list = []
    if no_repeat:
        n = len(nouns)
    for counter in range(0, n, len(nouns)):
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for noun, adv, adj in zip(nouns, adverbs, adjectives):
            if counter < n:
                jokes_list.append(f'{noun} {adv} {adj}')
                counter += 1
    return jokes_list


print(get_jokes(8))
print(get_jokes(no_repeat=True, n=18))
