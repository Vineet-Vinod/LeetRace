# LeetRace

Multiplayer LeetCode racing webapp. Create a room, invite friends, and race to solve the same problem — shortest solution wins.

## How It Works

1. **Create a room** — pick a difficulty (Easy / Medium / Hard) and a time limit (1–10 min)
2. **Share the 6-character room code** with other players
3. **Race** — everyone gets the same problem and a Monaco code editor
4. **Submit** — solutions run against 500–999 hidden test cases, or the complete legal domain for smaller problems
5. **Rank** — solved it? fewest characters wins (code golf). Didn't solve it? most tests passed ranks higher

## Quick Start

```bash
# requires Python 3.14+ and uv
uv sync
python main.py
```

Open `http://localhost:8000` in your browser.

## Problem set

The corpus originated from [LeetCodeDataset](https://huggingface.co/datasets/newfacade/LeetCodeDataset).
The bundled problems are maintained with local reference solutions and input generators.

| Difficulty | Count |
|------------|-------|
| Easy       | 583   |
| Medium     | 1,315 |
| Hard       | 571   |

## Corpus maintenance

Each retained problem has a Python reference solution in `corpus/solutions/` and
a seeded input generator in `corpus/generators/`. Generators produce 500–999
distinct inputs, or enumerate the complete legal domain when it is smaller.
Statements specify output ordering and tie rules, and use Markdown.

Rebuild a problem's expected outputs from its reference solution:

```bash
uv run task corpus build two-sum
```

The build checks input uniqueness, computes expected outputs, and verifies the
full suite in the submission sandbox before writing the JSON. Mutation wrappers
check both the return value and the required changed state. Large literal inputs
and expected lists use lossless compressed JSON; comparison still checks the
exact order and values.

```bash
uv run task corpus verify           # Verify all bundled reference solutions
uv run task corpus verify two-sum   # Verify one saved suite
uv run task ci                     # Type checks, lint, and project tests
```

Repair reports and seeded random audit selections are saved under `corpus/`.
Use these saved references to maintain the corpus; the older dataset-import
scripts do not implement its deterministic output contracts.

## Architecture

```
leetrace/
├── main.py                  # Entry point — uvicorn on 0.0.0.0:8000
├── server/
│   ├── app.py               # FastAPI routes + WebSocket mount
│   ├── ws.py                # WebSocket handler (join, start, submit, timer)
│   ├── rooms.py             # In-memory room & player state
│   ├── scoring.py           # Ranking: solved > char_count > time > tests_passed
│   ├── problems.py          # Problem loading with difficulty filtering
│   └── sandbox.py           # Subprocess execution with resource limits
├── static/
│   ├── index.html           # Landing page (create / join)
│   ├── room.html            # Game room (lobby → playing → finished)
│   ├── css/style.css        # Dark theme
│   └── js/
│       ├── app.js           # Landing page logic
│       ├── room.js          # WebSocket client & game state
│       └── editor.js        # Monaco editor wrapper
├── scripts/
│   └── corpus.py            # Generate expected outputs and verify saved suites
├── corpus/                  # Reference solutions, generators, and repair/audit reports
└── problems/                # Problem JSON files + index.json
```

## API

| Method | Endpoint           | Description                        |
|--------|--------------------|------------------------------------|
| POST   | `/api/rooms`       | Create a room (host, time, difficulty) |
| GET    | `/api/rooms/{id}`  | Get room state                     |
| GET    | `/api/problems`    | List all problems                  |
| WS     | `/ws/{room_id}`    | Game WebSocket                     |

## Sandbox

User code runs in an isolated subprocess with hard limits:

- **CPU**: 5 seconds
- **Memory**: 256 MB
- **Wall clock**: 10 seconds
- **File writes**: 1 MB
- **Subprocesses**: none allowed

These are the default limits. Problems with large finite output domains declare
their own CPU and memory budgets. Each testcase gets a fresh solution instance,
and comparisons preserve list ordering.

## Scoring

Players are ranked by:

1. **Solved** (yes before no)
2. **Character count** (fewer is better — code golf)
3. **Submit time** (faster is better)
4. **Tests passed** (more is better — tiebreaker for unsolved)

## Tech Stack

- **Backend**: FastAPI + uvicorn, vanilla Python (no database)
- **Frontend**: Vanilla JS, [Monaco Editor](https://microsoft.github.io/monaco-editor/) v0.45.0
- **Problems**: [newfacade/LeetCodeDataset](https://huggingface.co/datasets/newfacade/LeetCodeDataset) (HuggingFace)
