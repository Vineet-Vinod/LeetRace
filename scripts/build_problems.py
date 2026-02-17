"""
One-time build script: download LeetCodeDataset from HuggingFace,
split test cases, and write per-problem JSON files to problems/.
"""

import json
import re
import textwrap
from pathlib import Path

PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "problems"


def extract_test_cases(check_fn: str, entry_point: str) -> list[str]:
    """Split a check() function body into individual assert statements."""
    cases = []
    for line in check_fn.splitlines():
        stripped = line.strip()
        if stripped.startswith("assert"):
            cases.append(stripped)
    return cases


def slugify(title: str) -> str:
    """Convert problem title to a filename-safe slug."""
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def parse_starter_code(prompt: str, entry_point: str) -> str:
    """Extract a minimal starter code template from the prompt."""
    return f"def {entry_point}():\n    pass\n"


def build():
    try:
        from datasets import load_dataset
    except ImportError:
        print("Install build dependencies: pip install 'leetrace[build]'")
        raise SystemExit(1)

    print("Downloading LeetCodeDataset from HuggingFace...")
    ds = load_dataset("newfacade/LeetCodeDataset", split="train")

    PROBLEMS_DIR.mkdir(parents=True, exist_ok=True)
    index = []
    written = 0

    for row in ds:
        entry_point = row.get("entry_point", "")
        check_fn = row.get("test", "")
        prompt = row.get("prompt", "")
        title = row.get("title", "") or row.get("task_id", f"problem-{written}")
        difficulty = row.get("difficulty", "Medium")
        tags = row.get("tags", [])

        if not entry_point or not check_fn:
            continue

        test_cases = extract_test_cases(check_fn, entry_point)
        if len(test_cases) < 2:
            continue

        slug = slugify(title)
        if not slug:
            slug = f"problem-{written}"

        # Build the problem JSON
        problem_data = {
            "id": slug,
            "title": title,
            "difficulty": difficulty,
            "tags": tags if isinstance(tags, list) else [],
            "description": prompt,
            "entry_point": entry_point,
            "starter_code": f"def {entry_point}():\n    pass\n",
            "check_function": check_fn,
            "test_cases": test_cases,
        }

        problem_path = PROBLEMS_DIR / f"{slug}.json"
        problem_path.write_text(json.dumps(problem_data, indent=2))

        index.append({
            "id": slug,
            "title": title,
            "difficulty": difficulty,
            "tags": problem_data["tags"],
            "test_count": len(test_cases),
        })
        written += 1

    # Write index
    index_path = PROBLEMS_DIR / "index.json"
    index_path.write_text(json.dumps(index, indent=2))

    print(f"Wrote {written} problems to {PROBLEMS_DIR}")
    print(f"Index: {index_path}")


if __name__ == "__main__":
    build()
