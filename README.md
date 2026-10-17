# LeetRace

Race friends to solve the same problem in Python. Create a room, share its private invite link, and complete the Python starter in the Monaco editor. Correct solutions rank by character count, then lock time. Unsolved solutions rank by tests passed. Rooms support timed rounds, chat, resignation, and code review after each round.

Use **Copy join link** in the lobby to share `https://terse.codes/join/<room-code>`. Joiners must sign in or create an account before entering the room. Clicking the room code still copies just the code.

## Run locally

Install Node.js 24 or newer, pnpm, and Python 3.9 or newer, then run:

```sh
pnpm install
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
pnpm setup:dev
pnpm dev
```

Create `.env` from `.env.example` and supply Clerk development keys before starting. `pnpm setup:dev` configures Convex and a shared server secret without displaying it. The Convex CLI can use a local development deployment or a linked cloud project. `.env.local` overrides `.env`; both are gitignored.

Open http://localhost:3000. Vite proxies tRPC requests to port 8000. `pnpm dev` runs the frontend, API, and Convex development watcher. Use `APP_ORIGIN` if accessing the frontend through a different host or forwarded URL.

For the production build:

```sh
pnpm build
pnpm start
```

The TypeScript backend serves the React build and tRPC from http://localhost:8000. Python is used only to execute submissions. The Dockerfile includes both runtimes. The Fly configuration allocates 1 GB for large suites and submission workers. `/health` returns the server's health status.

## Development

```sh
pnpm run ci      # Type check, lint, test, and build locally
pnpm typecheck
pnpm lint
pnpm test
```

One package and lockfile cover both frontend and backend.

- `frontend/src/` contains the React UI, Python editor, and tRPC client, all written in TypeScript.
- `server/` contains the tRPC router, room state, problem loader, and submission judge.
- `tests/` checks judging, room transitions, transport, and the problem corpus.
- `problems/` contains one JSON file per repaired problem. There is no separate index.

The client infers request and response types from the tRPC router. Zod validates incoming requests and problem files. Clerk handles Google, GitHub, and username/password authentication. Every API call verifies the Clerk session, and Convex enforces the newest active session per account. Names come from the verified account; emails never enter room snapshots or public profiles.

[tRPC subscriptions](https://trpc.io/docs/server/subscriptions) send personalized room snapshots over server-sent events. Multiple tabs in the same session share one player slot. Heartbeats keep membership alive; after the last connection disappears or stops sending heartbeats, a player has 30 seconds to reconnect. The host can kick a player for the lifetime of the room. New entrants can join only in the lobby. Invite links use random 144-bit identifiers.

Rooms and source code live only in server memory and reset when the server restarts. Run exactly one backend process and one Fly Machine per deployment. The last member leaving or expiring closes the room and invalidates its invite. Convex retains numeric results, unique solved problems, ratings, wins, career points, and current/best streaks. Source code stays available only for the latest round review, then is discarded when the next round or tournament starts or the room closes. It is never written to Convex or application logs. Players can copy code during review. Refreshing the editor resets its unsubmitted draft.

## Problem data

The retained corpus originated from [LeetCodeDataset](https://huggingface.co/datasets/newfacade/LeetCodeDataset). Each filename is the problem ID. JSON files retain the title, difficulty, Markdown statement with examples and constraints, Python submission interface, and test inputs with expected outputs. Example explanations appear as prose outside the input and output snippets. Problems with unavailable illustrations are omitted. Floating-point problems also retain their comparison tolerances.

Statements support inline code and LaTeX. Use `$$x_{i}$$` for inline math and put `$$` delimiters on their own lines for display equations. Single dollar signs remain literal for prices and string examples. Plain powers such as `10^5` render as exponents in prose; code snippets remain unchanged.

Tests contain data, not executable assertions. Saved reference solutions, generators, duplicate test functions, topic tags, repair logs, and older problem snapshots have been removed. Linked lists and trees are stored as JSON data and become `ListNode` and `TreeNode` objects when passed to Python solutions. The judge checks in-place mutations where required. Integers beyond JavaScript's safe range use a decimal `$bigint` tag in storage and ordinary Python integers in submissions.

Large testcase values use a `$json` field containing base64-encoded zlib JSON, with a `bytes` field for the decoded size. This lossless encoding keeps large suites small on disk and lets the judge decode expected results one testcase at a time.

## Submission judging

Python submissions complete the supplied starter, usually a method on `Solution`. The judge preloads wildcard imports from `typing`, `string`, `re`, `datetime`, `collections`, `heapq`, `bisect`, `copy`, `math`, `random`, `statistics`, `itertools`, `functools`, `operator`, `io`, `sys`, `json`, `builtins`, and `sortedcontainers`, in that order. These imports do not count toward the score. The runner uses `.venv/bin/python3` when available, or `PYTHON_BIN` if set.

The TypeScript judge runs code in a separate Python process, with a fresh namespace for every testcase. Expected outputs stay in the parent process. Feedback includes tests passed, runtime, bounded stdout and stderr, and the first failing input and output. Character counts include whitespace.

The runner limits execution time, output, concurrency, and memory. Production additionally requires the Linux sandbox described below. Development execution is a plain subprocess and must remain on a trusted development machine.


## Scoring and statistics

Round placement sorts solved submissions by character count, then lock time. At equal length, any locked solution beats an unlocked one; earlier locks beat later locks. Unlocked ties use the first submission time of that best solution. A later attempt replaces a correct best solution only when it is shorter. Timely submissions may finish judging after the deadline; the round waits for accepted jobs before finalizing. A correct judged submission counts as a unique solved problem immediately, even if the player leaves before the round ends.

For solved competitive entries, round points are `100 × (2 × shortestCharacters / characters + timeBonus) / 3`, where `timeBonus = 1 − lockTime / roundDuration` for locked entries and zero for unlocked entries. Full precision is retained internally. Character counts are actual source lengths, including whitespace. The character component has twice the normalized time component's weight. Unsolved entries earn zero. Tournament standings sum completed round points. Placement and tournament points are different: a longer but faster submission can earn more points. True placement ties receive no arbitrary winner.

Solo rounds contribute only unique solved problems. Competitive round and tournament wins have separate current and best streaks. Ties and losses reset the corresponding competitive streak. Ratings start at 1000 and use pairwise Elo with K=32 divided by the initial opponent count. Equal scores produce no rating change. On departure, only completed rounds settle comparisons against the remaining players; each pair settles once. Remaining comparisons settle at the tournament's end. Events are idempotent, and stats writes retry while the server remains alive.

## Browser testing

Run the dev server first, then:

```sh
pnpm exec playwright install chromium
pnpm test:e2e
```

Playwright uses the real Clerk development instance and local API/Convex deployment. It creates clearly scoped test accounts; it does not modify existing users or use production keys. Reports and failure traces go under `/tmp/leetrace-playwright-*`. Test accounts remain available for inspecting results in Clerk. Unit tests use isolated in-process Convex state and never need credentials.

## Production on Fly

Production setup is separate from local development. No Fly runtime validation is performed by the local test suite.

1. Configure the Clerk production instance for Google/GitHub, required verified email, required immutable username of 4–12 characters, and password authentication. Supply production OAuth credentials and complete Clerk's DNS setup.
2. Link the Convex CLI to the intended project and deploy the functions with `pnpm exec convex deploy`. Configure a random `TERSE_SERVER_SECRET` of at least 32 characters in the production Convex environment, and provide the identical value to Fly. The Convex functions accept only this server credential; browsers access application data through authenticated tRPC.
3. Set Fly runtime secrets `CLERK_SECRET_KEY`, `CONVEX_URL`, `TERSE_SERVER_SECRET`, and `CLERK_WEBHOOK_SIGNING_SECRET`. Set `APP_ORIGIN` to the exact HTTPS application origin. Secrets must never use a `VITE_` prefix.
4. Register Clerk's webhook at `https://YOUR_DOMAIN/webhooks/clerk` for `user.deleted`, `session.ended`, `session.revoked`, and `session.removed`; use its signing secret on Fly. Webhook signatures are verified, deleted accounts are tombstoned, and stale session events cannot revoke a newer session.
5. Build with `VITE_CLERK_PUBLISHABLE_KEY` set to the matching `pk_live_...` value, for example `fly deploy --build-arg VITE_CLERK_PUBLISHABLE_KEY=pk_live_...`. This publishable value is embedded in the frontend and passed to the runtime by the Dockerfile. Private keys are never build arguments.
6. Keep exactly one Fly Machine: use `fly scale count 1`, and deploy with `fly deploy --ha=false` to avoid provisioning a second Machine. Multiple replicas cannot share ephemeral rooms. Deployments and process restarts end active rooms; schedule deployments accordingly.
7. Check `/health` and exercise the production sign-in, judge isolation, room lifecycle, and webhook flow before opening access. Linux namespace support must be checked on the actual target. The runner refuses unsafe fallback execution in production.

The Docker image includes Bubblewrap. Each production submission gets isolated user/process/network/mount namespaces, no application files or credentials, a read-only Python runtime, and disposable scratch space. CPU, memory, output, process, and wall-time limits constrain the worker. The initial limit is one concurrent judge and eight accepted jobs globally; excess submissions receive a busy response. Development subprocess execution on macOS is not a security boundary and must not be exposed as a public judge.
