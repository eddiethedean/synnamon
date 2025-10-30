from synnamon.index import has, list_words


def test_list_words_prefix_and_limit():
    words = list_words(prefix="ju", limit=10)
    assert isinstance(words, list)
    assert all(isinstance(w, str) for w in words)


def test_has_word_jump():
    # depends on bundled data containing 'jump'
    assert isinstance(has("jump"), bool)
