import json
from copy import deepcopy
from inflex import Noun

# Load thesaurus from JSON file
with open('../data/en_thesaurus_dict.json', 'r') as f:
    thesaurus = json.load(f)


def get_syns(word: str) -> dict:
    """Get synonyms for a word from the thesaurus."""
    word = word.lower()
    if word not in thesaurus:
        # Check if word is plural and if so, get synonyms for singular form
        if Noun(word).is_plural():
            word = Noun(word).singular()
            if word in thesaurus:
                results = deepcopy(thesaurus[word])
                if 'noun' in thesaurus[word]:
                    # Convert noun synonyms to plural forms
                    results['noun'] = [Noun(s).plural() for s in thesaurus[word]['noun'] if Noun(s).is_singular()]
                    return results
    return thesaurus.get(word, {})