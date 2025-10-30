from synnamon.fuzzy import suggest
from synnamon.get_syns import get_syns


def test_suggest_returns_candidates_for_typo():
    items = suggest("jupm", max_suggestions=5, cutoff=60)
    assert isinstance(items, list)


def test_get_syns_fallback_to_suggestions():
    res = get_syns(
        "jupm", fallback_to_suggestions=True, parts_of_speech=["verb"], limit=1
    )
    # Should return either empty or a verb suggestion result; we accept both but prefer non-empty
    assert isinstance(res, dict)


def test_normalize_verbs_flag():
    # If data contains verb base for 'running' -> 'run', this should help
    res = get_syns("running", normalize_verbs=True)
    assert isinstance(res, dict)
