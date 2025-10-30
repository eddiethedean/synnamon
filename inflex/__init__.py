class Noun:
    def __init__(self, word: str):
        self._word = word or ""

    def is_plural(self) -> bool:
        w = self._word.lower()
        if not w:
            return False
        if w.endswith("ss"):
            return False
        return w.endswith("s")

    def is_singular(self) -> bool:
        return not self.is_plural()

    def singular(self) -> str:
        w = self._word
        if w.lower().endswith("ies") and len(w) > 3:
            return w[:-3] + "y"
        if w.lower().endswith("s") and not w.lower().endswith("ss"):
            return w[:-1]
        return w

    def plural(self) -> str:
        w = self._word
        if w.lower().endswith("y") and len(w) > 1:
            return w[:-1] + "ies"
        if w.lower().endswith("s"):
            return w
        return w + "s"
