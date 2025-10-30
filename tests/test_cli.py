import json
from synnamon.cli import main


def run_cli(argv):
    # capture output by temporarily redirecting print via capsys in pytest; here we call main
    return main(argv)


def test_cli_lookup_json(capsys):
    code = run_cli(["lookup", "jump", "--pos", "verb", "--limit", "2", "--json"])
    captured = capsys.readouterr().out
    assert code == 0
    data = json.loads(captured)
    assert list(data.keys()) == ["verb"]
    assert len(data["verb"]) <= 2


def test_cli_suggest_basic(capsys):
    code = run_cli(["suggest", "jupm", "--max", "3", "--json"])
    captured = capsys.readouterr().out
    assert code == 0
    items = json.loads(captured)
    assert isinstance(items, list)


def test_cli_list_prefix(capsys):
    code = run_cli(["list", "--prefix", "ju", "--limit", "5", "--json"])
    captured = capsys.readouterr().out
    assert code == 0
    items = json.loads(captured)
    assert isinstance(items, list)
