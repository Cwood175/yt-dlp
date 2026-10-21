#!/usr/bin/env python3

# Execute with
# $ python -m yt_dlp

import sys

if __package__ is None and not getattr(sys, "frozen", False):
    # direct call of __main__.py
    import os.path

    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

try:
    import yt_dlp
except ModuleNotFoundError as e:
    # If an optional extractor submodule is missing during package initialization,
    # warn and continue; re-raise for other missing modules.
    if getattr(e, "name", "").startswith("yt_dlp.extractor"):
        import warnings

        warnings.warn(
            f"Optional extractor module {e.name!s} not found; continuing without it",
            ImportWarning,
        )
    else:
        raise


if __name__ == "__main__":
    yt_dlp.main()
