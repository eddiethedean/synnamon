import shelve
import os
import pathlib

from inflex import Noun

path = pathlib.Path(__file__).parent.resolve()


def get_record(word: str) -> dict:
    with shelve.open(os.path.join(path, 'data/en_thesaurus0')) as thesaurus0:
        if word in thesaurus0:
            return thesaurus0[word]
    with shelve.open(os.path.join(path, 'data/en_thesaurus1')) as thesaurus1:
        if word in thesaurus1:
            return thesaurus1[word]
    return {}


def get_syns(word: str) -> dict:
    """Get synonyms for a word from the thesaurus."""
    word = word.lower()
    record = get_record(word)
    if record == {}:
        # Check if word is plural and if so, get synonyms for singular form
        if Noun(word).is_plural():
            word = Noun(word).singular()
            record = get_record(word)
            if record != {}:
                if 'noun' in record:
                    # Convert noun synonyms to plural forms
                    record['noun'] = [Noun(s).plural() for s in record['noun'] if Noun(s).is_singular()]
                    return record
    return record