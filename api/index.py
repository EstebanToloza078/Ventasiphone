import os
import sys

# Ensure project root is on sys.path so the "app" package (directory) can be imported.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Avoid shadowing: if "app" was resolved to root app.py (module), drop it so the package loads.
_mod = sys.modules.get("app")
if _mod is not None:
    _file = getattr(_mod, "__file__", "") or ""
    if os.path.abspath(_file) == os.path.abspath(os.path.join(ROOT, "app.py")):
        sys.modules.pop("app", None)

from app import app  # noqa: E402

# Vercel Python runtime looks for `app` or `handler` in the entrypoint module.
__all__ = ["app"]

