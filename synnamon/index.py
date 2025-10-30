import os
import pathlib
import shelve
from functools import lru_cache
from typing import Iterable, List, Optional


def _get_db_path() -> str:
    path = pathlib.Path(__file__).parent.resolve()
    return os.path.join(path, "data/en_thesaurus")


@lru_cache(maxsize=1)
def list_words(prefix: Optional[str] = None, limit: Optional[int] = None) -> List[str]:
    db_path = _get_db_path()
    with shelve.open(db_path) as thesaurus:
        keys: Iterable[str] = thesaurus.keys()  # type: ignore[assignment]
        words = list(keys)
    if prefix:
        p = prefix.lower()
        words = [w for w in words if w.lower().startswith(p)]
    words.sort()
    if limit is not None and limit >= 0:
        words = words[:limit]
    return words


def has(word: str) -> bool:
    db_path = _get_db_path()
    with shelve.open(db_path) as thesaurus:
        return word in thesaurus
