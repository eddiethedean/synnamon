import shelve
import os
import pathlib

from inflex import Noun

path = pathlib.Path(__file__).parent.resolve()


def get_syns(word: str) -> dict:
    """Get synonyms for a word from the thesaurus."""
    word = word.lower()
    with shelve.open(os.path.join(path, 'data/en_thesaurus')) as thesaurus:
        if word not in thesaurus:
            # Check if word is plural and if so, get synonyms for singular form
            if Noun(word).is_plural():
                word = Noun(word).singular()
                if word in thesaurus:
                    results = thesaurus[word]
                    if 'noun' in thesaurus[word]:
                        # Convert noun synonyms to plural forms
                        results['noun'] = [Noun(s).plural() for s in thesaurus[word]['noun'] if Noun(s).is_singular()]
                        return results
        return thesaurus.get(word, {})