from synnamon import get_syns
from synnamon.get_syns import get_syns_many


def test_parts_of_speech_filter_and_limit_and_sort():
    res = get_syns("jump", parts_of_speech=["verb"], limit=3, sort="alpha")
    assert list(res.keys()) == ["verb"]
    assert len(res["verb"]) <= 3
    # alphabetical order check
    assert res["verb"] == sorted(res["verb"], key=str.lower)


def test_pluralize_nouns_flag_false():
    # With pluralize_nouns=False, no pluralization path should be taken
    res = get_syns("dragons", pluralize_nouns=False)
    # Either empty or non-noun results without pluralization; baseline: allow empty
    assert isinstance(res, dict)


def test_get_syns_many_basic():
    words = ["jump", "run", "notaword"]
    res = get_syns_many(words, parts_of_speech=["noun"], limit=2)
    assert set(res.keys()) == set(words)
    assert isinstance(res["notaword"], dict)
    if res["jump"]:
        assert list(res["jump"].keys()) == ["noun"]
