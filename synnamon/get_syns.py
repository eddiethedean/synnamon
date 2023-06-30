from .data.thesaurus import thesaurus

from inflex import Noun


def get_record(word: str) -> dict:
    if word in thesaurus:
        return thesaurus[word]
    else:
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