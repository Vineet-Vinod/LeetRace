# Corpus repair instructions

Work only in your assigned `problem-fix` worktree on branch `problem-fix`.
Many workers share this worktree. Do not switch branches, commit, stage files, or touch
another worker's assigned problems. Do not edit `problems/index.json` or shared code.

Read your assignment in `corpus/batches/<batch>.json`. Complete EVERY assigned problem.
Work in small groups and keep a durable progress report in `corpus/reports/<batch>.json`.
Do not stop after a sample or mark a problem repaired without running its solution.

For each problem:

1. Read its full statement, constraints, signature, and examples. Existing assertions
   and expected outputs are untrusted. Infer the actual contract and correct them.
2. Make the output unique. For unordered lists specify ascending or lexicographic
   order, including inner lists when appropriate. For ties choose a precise natural
   rule, such as the lexicographically smallest valid answer. Update ALL conflicting
   prose and examples. Do not normalize or sort the submitted answer in assertions.
   If a deterministic contract cannot reasonably preserve the task, delete that
   assigned problem file and document why. Difficulty or time pressure is not a
   reason to delete a problem.
3. Format the description as Markdown with paragraphs, `## Examples`, fenced
   example input/output blocks, `## Constraints`, and bullet constraints. Repair
   flattened powers like `104` to `10^4` only where the intended exponent is clear.
   Preserve bounds and mathematical meaning. Keep titles, IDs, tags and difficulty.
4. Write a correct standalone golden solution to `corpus/solutions/<id>.py` using
   the existing entry point and starter signature. The solution is executed with
   the problem preamble and sandbox TreeNode/ListNode helpers. Match any canonical
   output rule. Use straightforward algorithms. Add a small independent oracle or
   exhaustive cross-check for tricky logic whenever practical. Avoid `Any`.
5. Write `corpus/generators/<id>.py` with
   `def generate(seed: int = 0) -> list[str]:`. Return unique Python CALL EXPRESSIONS
   invoking `candidate`, e.g. `candidate(nums=[1, 2], target=3)`.
   These are inputs only, not assertions and not expected values. Calls may use
   `tree_node` and `list_node`. Use a local `random.Random(seed)` and explicit
   problem-specific constraints. Generator code must document or assert validity,
   including semantic conditions like connected graphs, sorted arrays, unique
   answers, valid BSTs, counts, non-overlapping intervals, and promised solutions.
   Generate 500-999 DISTINCT inputs, targeting 600. Include boundaries, adversarial
   patterns, examples, and varied random inputs. Keep total suite runtime below
   the sandbox's 5-second CPU / 10-second wall limits. Use a few large boundary
   inputs and many modest ones. If the entire legal domain has fewer than 500
   inputs, enumerate it fully and document the domain size and proof in the report.
   Never shrink stated constraints just to claim exhaustive coverage. Do not pad
   with repetitions, permutations of irrelevant kwargs, or copied legacy tests.
   Audit every numeric range against the original statement, including zero vs
   one minima. Assert the constraints during generation. Pure uniform random
   inputs often produce nearly all false or zero outputs: construct positive,
   negative, and adversarial families intentionally. Include actual maximum
   length/value boundary cases when the golden algorithm can handle them. A
   passing solution does not prove generated inputs satisfy the constraints.
   Inspect expected-output distributions before finishing. A constant answer
   must not pass the suite unless mathematics forces it over the entire legal
   domain; document the proof for such exceptions. A few positive cases among
   hundreds of negatives are insufficient: use substantial constructive families.
   Re-read the ORIGINAL statement with `git show HEAD:problems/<id>.json` before
   finalizing, so rewritten prose cannot accidentally narrow or alter constraints.
6. Use the shared helper after it exists:
   `uv run python -m scripts.corpus build <id>`.
   It runs the golden solution on generated inputs, writes exact expected
   outputs into `test_cases` and synchronizes `check_function`, then verifies
   the entire suite through the actual sandbox with strict ordering.
   Read any failures and fix them. You may implement custom assertions only for
   mutation/design interfaces unsupported by the helper, but preserve exact
   deterministic expected outputs and keep the generator reproducible. Notify
   the master about any required helper/runner change before relying on it.
   Mutation inputs ARE supported by call wrappers. For a returned length and
   modified prefix use `(lambda nums: (lambda k: (k, nums[:k]))(candidate(nums)))([...])`.
   For a void mutation return the modified argument after calling the candidate.
   For tree mutation compare both returned tree and input, e.g.
   `(lambda root: (repr(candidate(root)), repr(root)))(tree_node([...]))`.
   The helper computes exact expected tuples, so wrappers remain reproducible.
   Large literal inputs and expected lists are stored as losslessly compressed
   JSON and decoded by the runner without weakening equality.
7. Update your report with id, status (`repaired` or `deleted`), test_count,
   canonicalization, constraint reasoning, validation result, and any finite
   domain exception. Include every assigned problem exactly once when done.
   Before finishing, remove conflicting alternative-answer examples, blank
   Explanation labels and missing-image references. Restore powers in prose and
   constraints, including tolerance `10^-5`; do not leave `104` for `10^4`.

You can edit your assigned JSON files, their solution and generator files, your
report, and private scratch files under `corpus/scratch/<batch>/` only. Scratch
files are ignored by git. Do not rewrite shared infrastructure or frontend/server
code. If a task needs infrastructure changes, message the master and continue
with other problems. Do not spawn further repair agents.

This task is solely corpus quality and related submission handling. Do not change
unrelated application behavior. Persist through all assignments, using the report
to resume after context compaction. Send the master progress after each ~10
problems and report concrete blockers promptly.
