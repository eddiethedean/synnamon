import argparse
import json
import sys
from typing import List, Optional, Protocol, cast

from .get_syns import get_syns
from .fuzzy import suggest
from .index import list_words


def _parse_pos(value: Optional[str]) -> Optional[List[str]]:
    if not value:
        return None
    return [p.strip() for p in value.split(",") if p.strip()]


def cmd_lookup(args: argparse.Namespace) -> int:
    pos = _parse_pos(args.pos)
    res = get_syns(
        args.word,
        parts_of_speech=pos,
        limit=args.limit,
        sort="alpha",
        pluralize_nouns=not args.no_pluralize,
        fallback_to_suggestions=args.fallback,
    )
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        for k, v in res.items():
            print(f"{k}:")
            for s in v:
                print(f"  - {s}")
    return 0


def cmd_suggest(args: argparse.Namespace) -> int:
    items = suggest(args.word, max_suggestions=args.max, cutoff=args.cutoff)
    if args.json:
        print(json.dumps(items, ensure_ascii=False))
    else:
        for s in items:
            print(s)
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    words = list_words(prefix=args.prefix, limit=args.limit)
    if args.json:
        print(json.dumps(words, ensure_ascii=False))
    else:
        for w in words:
            print(w)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="synnnamon")
    sub = p.add_subparsers(dest="cmd", required=True)

    look = sub.add_parser("lookup", help="Lookup synonyms for a word")
    look.add_argument("word")
    look.add_argument("--pos", help="Comma-separated PoS filter, e.g. noun,verb")
    look.add_argument("--limit", type=int, default=None)
    look.add_argument("--json", action="store_true")
    look.add_argument(
        "--fallback", action="store_true", help="Use fuzzy suggestion if not found"
    )
    look.add_argument(
        "--no-pluralize", action="store_true", help="Disable pluralization for nouns"
    )
    look.set_defaults(func=cmd_lookup)

    sug = sub.add_parser("suggest", help="Suggest closest words to input")
    sug.add_argument("word")
    sug.add_argument("--max", type=int, default=5)
    sug.add_argument("--cutoff", type=int, default=80)
    sug.add_argument("--json", action="store_true")
    sug.set_defaults(func=cmd_suggest)

    lst = sub.add_parser("list", help="List words, optionally by prefix")
    lst.add_argument("--prefix", default=None)
    lst.add_argument("--limit", type=int, default=None)
    lst.add_argument("--json", action="store_true")
    lst.set_defaults(func=cmd_list)

    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    class CommandFunc(Protocol):
        def __call__(self, args: argparse.Namespace) -> int: ...

    func = cast(CommandFunc, args.func)
    return func(args)


if __name__ == "__main__":
    sys.exit(main())
