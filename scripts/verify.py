"""Validate LeetRace problems against HuggingFace reference solutions.

Classifies each problem as:
  - verified:   reference solution passes ALL test cases
  - partial:    reference solution passes SOME but not all
  - untestable: all test cases assert == None (in-place mutation problems)
  - unmatched:  no reference solution found in HuggingFace dataset
  - error:      reference solution crashed or timed out

Updates problems/index.json with a "verified" boolean field and writes
a detailed report to problems/validation_report.json.

Usage:
    python scripts/validate_problems.py
    python scripts/validate_problems.py --workers 4
"""

import argparse
import json
import re
import sys
import time
from multiprocessing import Pool
from pathlib import Path

# Add project root to path so we can import server modules
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.generate import slugify  # noqa: E402
from server.sandbox import _run_sync  # noqa: E402

PROBLEMS_DIR = PROJECT_ROOT / "problems"


def is_all_none(test_cases: list[str]) -> bool:
    """Check if ALL test cases assert == None (in-place mutation problems)."""
    if not test_cases:
        return False
    for tc in test_cases:
        # Match patterns like: assert candidate(...) == None
        if not re.search(r"==\s*None\s*$", tc.strip()):
            return False
    return True


def detect_any_order(description: str) -> bool:
    """Heuristic from ws.py:307 — check for 'any order' in description."""
    return "any order" in description.lower()


def validate_one(args: tuple) -> dict:
    """Validate a single problem against its reference solution.

    Args is a tuple of (problem_id, solution_code, any_order) to support
    multiprocessing.Pool.map().

    Returns a dict with validation results.
    """
    problem_id, solution_code, any_order = args

    problem_path = PROBLEMS_DIR / f"{problem_id}.json"
    if not problem_path.exists():
        return {
            "id": problem_id,
            "category": "error",
            "error": "Problem file not found",
        }

    problem = json.loads(problem_path.read_text())
    test_cases = problem.get("test_cases", [])
    entry_point = problem.get("entry_point", "")
    preamble = problem.get("preamble", "")

    if not test_cases:
        return {"id": problem_id, "category": "error", "error": "No test cases"}

    # Static check: all-None test cases
    if is_all_none(test_cases):
        return {
            "id": problem_id,
            "category": "untestable",
            "passed": 0,
            "total": len(test_cases),
            "pass_rate": 0.0,
            "error": "All test cases assert == None",
        }

    # Run reference solution through sandbox
    result = _run_sync(
        code=solution_code,
        entry_point=entry_point,
        test_cases=test_cases,
        preamble=preamble,
        any_order=any_order,
    )

    passed = result.get("passed", 0)
    total = result.get("total", len(test_cases))
    pass_rate = passed / total if total > 0 else 0.0
    error = result.get("error")

    if passed == total and total > 0:
        category = "verified"
    elif passed > 0:
        category = "partial"
    else:
        category = "error"

    return {
        "id": problem_id,
        "category": category,
        "passed": passed,
        "total": total,
        "pass_rate": round(pass_rate, 4),
        "error": error,
    }


def main():
    parser = argparse.ArgumentParser(description="Validate LeetRace problems")
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Number of parallel workers (default: 8)",
    )
    args = parser.parse_args()

    # Load problem index
    index_path = PROBLEMS_DIR / "index.json"
    if not index_path.exists():
        print("Error: problems/index.json not found. Run build_problems.py first.")
        sys.exit(1)

    index = json.loads(index_path.read_text())
    print(f"Loaded {len(index)} problems from index")

    # Download HuggingFace dataset
    try:
        from datasets import load_dataset
    except ImportError:
        print("Install build dependencies: uv pip install datasets")
        sys.exit(1)

    print("Downloading LeetCodeDataset from HuggingFace...")
    ds = load_dataset("newfacade/LeetCodeDataset", split="train")

    # Build map: slug -> reference solution
    ref_solutions: dict[str, str] = {}
    for row in ds:
        task_id = row.get("task_id", "")
        completion = row.get("completion", "")
        if task_id and completion:
            slug = slugify(task_id)
            if slug:
                ref_solutions[slug] = completion

    print(f"Found {len(ref_solutions)} reference solutions in HuggingFace dataset")

    # Load problem descriptions for any_order detection
    problem_descriptions: dict[str, str] = {}
    for entry in index:
        pid = entry["id"]
        prob_path = PROBLEMS_DIR / f"{pid}.json"
        if prob_path.exists():
            prob_data = json.loads(prob_path.read_text())
            problem_descriptions[pid] = prob_data.get("description", "")

    # Static analysis pass: find all-None problems first
    print("\n--- Static Analysis Pass ---")
    untestable_ids = set()
    for entry in index:
        pid = entry["id"]
        prob_path = PROBLEMS_DIR / f"{pid}.json"
        if not prob_path.exists():
            continue
        prob_data = json.loads(prob_path.read_text())
        if is_all_none(prob_data.get("test_cases", [])):
            untestable_ids.add(pid)
    print(
        f"Found {len(untestable_ids)} untestable problems (all test cases assert == None)"
    )

    # Build validation work items
    work_items = []
    unmatched_ids = []
    results = []

    for entry in index:
        pid = entry["id"]

        if pid in untestable_ids:
            # Already classified via static analysis
            prob_path = PROBLEMS_DIR / f"{pid}.json"
            prob_data = json.loads(prob_path.read_text())
            tc_count = len(prob_data.get("test_cases", []))
            results.append(
                {
                    "id": pid,
                    "category": "untestable",
                    "passed": 0,
                    "total": tc_count,
                    "pass_rate": 0.0,
                    "error": "All test cases assert == None",
                }
            )
            continue

        if pid not in ref_solutions:
            unmatched_ids.append(pid)
            results.append(
                {
                    "id": pid,
                    "category": "unmatched",
                    "passed": 0,
                    "total": 0,
                    "pass_rate": 0.0,
                    "error": "No reference solution in HuggingFace dataset",
                }
            )
            continue

        any_order = detect_any_order(problem_descriptions.get(pid, ""))
        work_items.append((pid, ref_solutions[pid], any_order))

    print(f"Unmatched problems (no reference solution): {len(unmatched_ids)}")
    print(f"Problems to validate: {len(work_items)}")

    # Run validation in parallel
    print(
        f"\n--- Validating {len(work_items)} problems with {args.workers} workers ---"
    )
    start_time = time.time()

    with Pool(processes=args.workers) as pool:
        validated = []
        total_items = len(work_items)
        for i, result in enumerate(pool.imap_unordered(validate_one, work_items), 1):
            validated.append(result)
            if i % 50 == 0 or i == total_items:
                pct = i * 100 // total_items
                cats = {}
                for r in validated:
                    cats[r["category"]] = cats.get(r["category"], 0) + 1
                status = " | ".join(f"{k}: {v}" for k, v in sorted(cats.items()))
                print(f"  [{i}/{total_items}] {pct}% — {status}")

    results.extend(validated)
    elapsed = time.time() - start_time
    print(f"Validation completed in {elapsed:.1f}s")

    # Build results by category
    categories: dict[str, list] = {
        "verified": [],
        "partial": [],
        "untestable": [],
        "unmatched": [],
        "error": [],
    }
    for r in results:
        cat = r["category"]
        categories[cat].append(r)

    # Print summary
    print("\n--- Results ---")
    for cat in ["verified", "partial", "untestable", "unmatched", "error"]:
        print(f"  {cat}: {len(categories[cat])}")
    print(f"  total: {len(results)}")

    # Update index.json with verified field
    id_to_category = {r["id"]: r["category"] for r in results}
    for entry in index:
        entry["verified"] = id_to_category.get(entry["id"]) == "verified"

    index_path.write_text(json.dumps(index, indent=2) + "\n")
    verified_count = sum(1 for e in index if e.get("verified"))
    print(
        f"\nUpdated {index_path} — {verified_count} verified, {len(index) - verified_count} unverified"
    )

    # Write detailed report
    report = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "summary": {cat: len(entries) for cat, entries in categories.items()},
        "total": len(results),
        "untestable_problems": [r["id"] for r in categories["untestable"]],
        "problems": sorted(results, key=lambda r: r["id"]),
    }
    report_path = PROBLEMS_DIR / "validation_report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Wrote detailed report to {report_path}")


if __name__ == "__main__":
    main()
