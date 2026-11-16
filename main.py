"""Cake-osaurus — ai-excited-01 entry for make.fun.

Grader contract:
    The grader runs this program with no MAKEFUN_OUTPUT_DIR environment
    variable set and with the repository mounted read-only. This program
    must therefore default its output directory to the absolute path
    "/output" and copy the bundled image there as "entry.png".

    When MAKEFUN_OUTPUT_DIR is set (e.g. for local testing), that
    directory is used instead of "/output".

Behaviour:
    Copies the bundled ``entry.png`` (located in the same directory as
    this ``main.py``) to ``<output_dir>/entry.png`` in 64 KiB chunks,
    creating the output directory if needed. Uses only the Python
    standard library.
"""

import os
import shutil
import sys

CHUNK_SIZE = 64 * 1024  # 64 KiB


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            chunk = fin.read(CHUNK_SIZE)
            if not chunk:
                break
            fout.write(chunk)
        # Flush and fsync before close so the grader never reads a
        # partially-written file if the process exits immediately after.
        fout.flush()
        os.fsync(fout.fileno())
    return 0


if __name__ == "__main__":
    sys.exit(main())
