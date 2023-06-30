A simple Python package that looks up synonyms for words.

![Synnamon Logo](https://raw.githubusercontent.com/eddiethedean/synnamon/main/docs/synnamon.png)
-----------------

# Synnamon: Easy to use function for word synonym lookups
[![PyPI Latest Release](https://img.shields.io/pypi/v/synnamon.svg)](https://pypi.org/project/synnamon/)
![Tests](https://github.com/eddiethedean/synnamon/actions/workflows/tests.yml/badge.svg)

## What is it?

**Synnamon** is a simple Python package that looks up synonyms using a built in thesaurus json file instead of reaching out to web resources (PyDictionary) or using large English lexical databases (nltk WordNet).

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/eddiethedean/synnamon

```sh
# PyPI
pip install synnamon
```

## Dependencies
- inflex: used to convert plural word lookups to singular and then convert singular synonym results to plural


## Example
```sh
>>> import synnamon

>>> synnamon.get_syns('jump')
{'noun': ['leap', 'parachuting', 'jumping', 'saltation', 'startle', 'start'],
 'verb': ['leap',
  'spring',
  'stand out',
  'alternate',
  'startle',
  'climb up',
  'chute',
  'jump-start',
  'jump out',
  'skip over',
  'stick out',
  'jump off',
  'jumpstart',
  'pass over',
  'derail',
  'start',
  'rise',
  'bound',
  'parachute',
  'jump on',
  'leap out',
  'skip']}
```