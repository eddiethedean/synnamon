from types import FunctionType

import synnamon


def test_package_exports_get_syns():
    # Ensure the package-level import in __init__.py exposes get_syns
    assert hasattr(synnamon, "get_syns")
    assert isinstance(synnamon.get_syns, FunctionType)

    # Sanity check: calling it returns a dict
    result = synnamon.get_syns("jump")
    assert isinstance(result, dict)
