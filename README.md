# LeetRace

Multiplayer LeetCode racing webapp. Create a room, invite friends, and race to solve the same problem — shortest solution wins.

## How It Works

1. **Create a room** — pick a difficulty (Easy / Medium / Hard) and a time limit (1–10 min)
2. **Share the 6-character room code** with other players
3. **Race** — everyone gets the same problem and a Monaco code editor
4. **Submit** — solutions run against 100+ hidden test cases in a sandboxed subprocess
5. **Rank** — solved it? fewest characters wins (code golf). Didn't solve it? most tests passed ranks higher

## Quick Start

```bash
# requires Python 3.14+ and uv
uv sync
python main.py
```

Open `http://localhost:8000` in your browser.

## Rebuilding the Problem Set

The repo ships with 2,637 problems downloaded from the [LeetCodeDataset](https://huggingface.co/datasets/newfacade/LeetCodeDataset) on HuggingFace. To rebuild from scratch:

```bash
uv pip install datasets
python scripts/build_problems.py
```

| Difficulty | Count |
|------------|-------|
| Easy       | 637   |
| Medium     | 1,395 |
| Hard       | 605   |

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
│   └── build_problems.py    # HuggingFace dataset → JSON files
└── problems/                # 2,637 problem JSON files + index.json
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
