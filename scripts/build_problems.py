"""
One-time build script: download LeetCodeDataset from HuggingFace,
split test cases, and write per-problem JSON files to problems/.
"""

import json
import re
from pathlib import Path

PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "problems"

# Common imports needed by LeetCode starter code (class Solution with type hints)
PREAMBLE = """\
from typing import *
from collections import *
from functools import *
from itertools import *
from heapq import *
from bisect import *
from math import *
import math, collections, functools, itertools, bisect, heapq, string, re
"""


def extract_test_cases(check_fn: str) -> list[str]:
    """Split a check() function body into individual assert statements.

    Handles multi-line asserts by joining continuation lines.
    """
    cases = []
    current = None

    for line in check_fn.splitlines():
        stripped = line.strip()
        if stripped.startswith("assert"):
            if current is not None:
                cases.append(current)
            current = stripped
        elif current is not None and stripped and not stripped.startswith("def "):
            # Continuation of previous assert
            current += " " + stripped
        elif stripped.startswith("def ") and current is not None:
            cases.append(current)
            current = None

    if current is not None:
        cases.append(current)

    return cases


def slugify(title: str) -> str:
    """Convert problem title to a filename-safe slug."""
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def build():
    try:
        from datasets import load_dataset
    except ImportError:
        print("Install build dependencies: uv pip install datasets")
        raise SystemExit(1)

    print("Downloading LeetCodeDataset from HuggingFace...")
    ds = load_dataset("newfacade/LeetCodeDataset", split="train")

    PROBLEMS_DIR.mkdir(parents=True, exist_ok=True)
    index = []
    written = 0
    skipped = 0
    slug_counts: dict[str, int] = {}

    for row in ds:
        entry_point = row.get("entry_point", "")
        check_fn = row.get("test", "")
        task_id = row.get("task_id", "")
        title = task_id or f"problem-{written}"
        difficulty = row.get("difficulty", "Medium")
        tags = row.get("tags", [])
        description = row.get("problem_description", "")
        starter_code = row.get("starter_code", "")

        if not entry_point or not check_fn:
            skipped += 1
            continue

        test_cases = extract_test_cases(check_fn)
        if len(test_cases) < 2:
            skipped += 1
            continue

        slug = slugify(title)
        if not slug:
            slug = f"problem-{written}"

        # Handle duplicate slugs
        if slug in slug_counts:
            slug_counts[slug] += 1
            slug = f"{slug}-{slug_counts[slug]}"
        else:
            slug_counts[slug] = 0

        # Ensure starter_code has a valid body (add pass if it ends with just a signature)
        if starter_code and starter_code.rstrip().endswith(':'):
            # Function/class definition without body, add pass statement
            starter_code = starter_code.rstrip() + '\n        pass'

        # Build the problem JSON
        problem_data = {
            "id": slug,
            "title": title.replace("-", " ").title(),
            "difficulty": difficulty,
            "tags": tags if isinstance(tags, list) else [],
            "description": description,
            "entry_point": entry_point,
            "starter_code": starter_code,
            "preamble": PREAMBLE,
            "check_function": check_fn,
            "test_cases": test_cases,
        }

        problem_path = PROBLEMS_DIR / f"{slug}.json"
        problem_path.write_text(json.dumps(problem_data, indent=2))

        index.append(
            {
                "id": slug,
                "title": problem_data["title"],
                "difficulty": difficulty,
                "tags": problem_data["tags"],
                "test_count": len(test_cases),
            }
        )
        written += 1

    # Write index
    index_path = PROBLEMS_DIR / "index.json"
    index_path.write_text(json.dumps(index, indent=2))

    print(f"Wrote {written} problems to {PROBLEMS_DIR}")
    print(f"Skipped {skipped} problems (missing data or <2 test cases)")
    print(f"Index: {index_path}")


if __name__ == "__main__":
    build()
