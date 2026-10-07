# Corpus repair record

All 2,469 problems were retained and rebuilt from saved Python reference
solutions and seeded input generators. The corpus contains 1,466,499 tests.
2,426 suites have 500–999 distinct inputs; 43 suites enumerate a smaller
complete legal domain. Domain reasoning is recorded in the ownership reports.

The repair authors were ten Luna 6 High workers for Easy problems, ten Luna 6
High workers for Medium problems, and twenty Sol 6.1 High workers for Hard
problems. Batch manifests and completed reports are saved in this directory.

Nine separate Sol 6.1 Low auditors checked a reproducibly sampled set of
210 problems, 8.5% of the corpus, using independent oracles and
additional exhaustive checks. Initial findings are preserved. Recheck and final
reports record the repairs; coverage limitations are retained where relevant.

The broad numeric scan checked all problems and 1,466,506 generated inputs.
It found 38 problems with invalid inputs or damaged constraint text. The final
check of those problems covers both seeds and 45,731 inputs with no remaining
violations. A separate tree/list scan checked 162 problems and 97,945 inputs;
its final repair checks also pass. These mechanical scans do not prove symbolic,
structural, or semantic constraints that their parsers cannot recognize. Their
reports explicitly list those limits.

Every saved suite has passed its reference solution through the actual submission
sandbox. Every generator passed input-count and duplicate checks with seeds 0 and
17, and a repeated seed-0 check across separate Python processes. The automated
statement scan checked 5,801 examples with no output mismatches; 181 examples
require notation or interfaces unsupported by that parser. Repair workers and
sample auditors performed additional direct example checks.

The application checks pass: 300 pytest tests, Python type checks, Ruff, and the
frontend production build. The test run retains the pre-existing unawaited
`break_task` coroutine warning.

`problems/validation_report.json` contains the final counts and sandbox timings.
Use `uv run task corpus build <id>` to regenerate a suite and
`uv run task corpus verify` to verify the stored suites. The older import scripts
do not preserve the revised deterministic contracts.

The larger suites increase repository size. Large literal inputs and expected
lists use lossless compressed JSON. Ordered equality remains exact; floats use
the stated tolerance. Fresh solution instances and mutation assertions prevent
state carried between tests from disguising incorrect submissions.
