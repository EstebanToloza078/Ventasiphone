import os
import sys

# Local entrypoint (kept at root per project convention).
# Avoid name conflict with the `app/` package when this file is named app.py.
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

if __name__ == "__main__":
    # When run as a script, prevent importing this module as `app`.
    sys.modules.pop("app", None)

from app import app  # noqa: E402

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)

