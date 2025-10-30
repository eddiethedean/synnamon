import shelve
import os
import pathlib
from typing import Dict, Iterable, List, Optional, Sequence, cast
from functools import lru_cache

from inflex import Noun


@lru_cache(maxsize=4096)
def get_record(word: str) -> Dict[str, List[str]]:
    """Return the raw thesaurus record for a word or an empty dict if missing.

    The returned structure maps part-of-speech keys (e.g. "noun", "verb") to
    lists of synonym strings.
    """
    path = pathlib.Path(__file__).parent.resolve()
    with shelve.open(os.path.join(path, "data/en_thesaurus")) as thesaurus:
        if word not in thesaurus:
            return {}
        value = cast(Dict[str, List[str]], thesaurus[word])
        # Return a shallow copy to avoid external mutation and cache pollution
        return {k: list(v) for k, v in value.items()}


def _apply_pos_filter_limit_sort(
    record: Dict[str, List[str]],
    parts_of_speech: Optional[Sequence[str]] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = "alpha",
) -> Dict[str, List[str]]:
    result: Dict[str, List[str]] = {}
    pos_keys: Iterable[str] = (
        parts_of_speech if parts_of_speech is not None else record.keys()
    )
    for pos in pos_keys:
        if pos in record:
            values = list(record[pos])
            if sort == "alpha":
                values.sort(key=lambda s: s.lower())
            if limit is not None and limit >= 0:
                values = values[:limit]
            result[pos] = values
    return result


def get_syns(
    word: str,
    *,
    parts_of_speech: Optional[Sequence[str]] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = "alpha",
    pluralize_nouns: bool = True,
    fallback_to_suggestions: bool = False,
    normalize_verbs: bool = False,
) -> Dict[str, List[str]]:
    """Get synonyms for a word from the built-in thesaurus.

    Behavior:
    - Input is normalized with strip+lowercase.
    - If the exact word is not found and the word is plural, look up the
      singular form and pluralize only the noun synonyms in the result (if
      pluralize_nouns=True).
    - Optionally filter, sort, and limit results per part of speech.
    - If fallback_to_suggestions=True and no record is found, try the first
      suggestion (when fuzzy module is available).
    """
    normalized = word.strip().lower()
    if normalized == "":
        return {}

    record = get_record(normalized)
    if record == {} and Noun(normalized).is_plural() and pluralize_nouns:
        singular = Noun(normalized).singular()
        singular_record = get_record(singular)
        if singular_record and "noun" in singular_record:
            # Create a new dict without mutating the shelve-backed record
            new_record: Dict[str, List[str]] = {
                k: list(v) for k, v in singular_record.items()
            }
            new_record["noun"] = [
                Noun(s).plural() if Noun(s).is_singular() else s
                for s in singular_record["noun"]
            ]
            return _apply_pos_filter_limit_sort(
                new_record, parts_of_speech, limit, sort
            )
        return _apply_pos_filter_limit_sort(
            singular_record, parts_of_speech, limit, sort
        )

    # Optional simple verb normalization heuristics
    if record == {} and normalize_verbs:
        candidates = []
        if normalized.endswith("ing") and len(normalized) > 4:
            candidates.append(normalized[:-3])
        if normalized.endswith("ed") and len(normalized) > 3:
            candidates.append(normalized[:-2])
        if normalized.endswith("s") and len(normalized) > 3:
            candidates.append(normalized[:-1])
        for cand in candidates:
            cand_record = get_record(cand)
            if cand_record:
                return _apply_pos_filter_limit_sort(
                    cand_record, parts_of_speech, limit, sort
                )

    if record == {} and fallback_to_suggestions:
        try:
            from .fuzzy import suggest  # type: ignore

            suggestions = suggest(normalized, max_suggestions=1)
            if suggestions:
                record = get_record(suggestions[0])
        except Exception:
            pass

    return _apply_pos_filter_limit_sort(record, parts_of_speech, limit, sort)


def get_syns_many(
    words: Sequence[str],
    **kwargs: object,
) -> Dict[str, Dict[str, List[str]]]:
    results: Dict[str, Dict[str, List[str]]] = {}
    for w in words:
        if isinstance(w, str):
            results[w] = get_syns(w, **kwargs)  # type: ignore[arg-type]
    return results
