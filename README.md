A simple Python package that looks up synonyms for words.

![Synnamon Logo](https://raw.githubusercontent.com/eddiethedean/synnamon/main/docs/synnamon.png)
-----------------

# Synnamon: Offline synonyms for English words (Python 3.8+)
[![PyPI Latest Release](https://img.shields.io/pypi/v/synnamon.svg)](https://pypi.org/project/synnamon/)
![Tests](https://github.com/eddiethedean/synnamon/actions/workflows/tests.yml/badge.svg)

## What is it?

**Synnamon** is a simple Python package that looks up synonyms using a built in thesaurus shelve file instead of reaching out to web resources (PyDictionary) or using large English lexical databases (nltk WordNet).

## Where to get it
Source code: https://github.com/eddiethedean/synnamon

```sh
# PyPI
pip install synnamon
```

## Requirements
- Python 3.8+
- Dependency: `inflex` (used to convert plural word lookups to singular and then convert singular synonym results to plural)


## Usage
```python
import synnamon

syns = synnamon.get_syns('jump')
print(syns.get('verb', [])[:5])
```

### Behavior
- Input is normalized to lowercase and trimmed.
- If the plural form is not found, `get_syns` will try the singular form and pluralize only the noun synonyms.
- Returns `{}` for unknown words or empty/whitespace input.

## API
```python
from synnamon import get_syns

def get_syns(word: str) -> dict:
    """Get synonyms for a word from the built-in thesaurus."""
```

## Development
Run tests with pytest:
```sh
pytest -q
```

Test configuration lives in `pyproject.toml` and collects coverage for `synnnamon`.