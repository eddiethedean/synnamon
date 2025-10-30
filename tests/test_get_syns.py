import pytest
from synnamon import get_syns


def test_get_syns_found_contains_expected_keys_and_examples():
    result = get_syns("jump")
    assert "noun" in result or "verb" in result
    # Spot-check a few expected synonyms without relying on full ordering
    verb_syns = set(result.get("verb", []))
    assert {"leap", "jump out", "skip"}.issubset(verb_syns)


@pytest.mark.parametrize("word", ["notaword", "c++"])
def test_get_syns_unknown_or_special_returns_empty(word: str):
    assert get_syns(word) == {}


def test_get_syns_plural_path_pluralizes_noun_syns():
    # For a plural not directly present, we expect noun results
    result = get_syns("dragons")
    assert "noun" in result
    # Ensure some known pluralized forms are present (case preserved as in data)
    noun_syns = set(result["noun"])
    expected_some = {"flying lizards", "firedrakes", "flying dragons"}
    assert expected_some.issubset(noun_syns)


@pytest.mark.parametrize("word", ["", "   "])
def test_get_syns_empty_or_whitespace_returns_empty(word: str):
    assert get_syns(word) == {}


def test_get_syns_multiple_pos_present_for_run():
    result = get_syns("run")
    assert "noun" in result and "verb" in result


def test_get_syns_case_insensitive_happy_contains_adj_synonyms():
    result = get_syns("HaPpY")
    assert "adj" in result
    adj_syns = set(result["adj"])
    assert {"glad", "joyful", "cheerful"}.issubset(adj_syns)
