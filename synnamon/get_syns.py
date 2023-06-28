import json

with open('../data/en_thesaurus_dict.json', 'r') as f:
    thesaurus = json.load(f)


def get_syns(word: str) -> dict:
    word = word.lower()
    if word[-1] == 's':
        word = word[:-1]
    return thesaurus.get(word, {})