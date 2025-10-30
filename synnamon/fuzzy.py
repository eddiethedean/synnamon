from typing import List

try:
    from rapidfuzz import process as rf_process  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    rf_process = None  # type: ignore

from .index import list_words


def suggest(word: str, *, max_suggestions: int = 5, cutoff: int = 80) -> List[str]:
    candidates = list_words()
    if not candidates:
        return []
    w = word.strip().lower()
    if rf_process is not None:
        # rapidfuzz scores are 0..100; process.extract returns list of (match, score, idx)
        matches = rf_process.extract(
            w, candidates, score_cutoff=cutoff, limit=max_suggestions
        )
        return [m[0] for m in matches]

    # Fallback to difflib
    import difflib

    # difflib uses 0..1 similarity; convert cutoff to approximate ratio
    ratio_cutoff = cutoff / 100.0
    # get_close_matches returns up to n close matches above cutoff
    return difflib.get_close_matches(
        w, candidates, n=max_suggestions, cutoff=ratio_cutoff
    )
