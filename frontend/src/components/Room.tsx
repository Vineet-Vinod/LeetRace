import { useEffect, useRef, useState, type FormEvent } from "react";
import { Link, Navigate, useNavigate, useSearchParams } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {
  api,
  errorMessage,
  sessionToken,
  type RoomSnapshot,
  type Submission,
} from "../api";
import CodeEditor from "./CodeEditor";

const primaryButton =
  "px-5 py-2.5 bg-primary text-inverse rounded-lg font-display text-sm font-semibold uppercase tracking-wider hover:bg-primary-bright disabled:opacity-40 disabled:cursor-not-allowed";
const secondaryButton =
  "px-4 py-2.5 border border-brd-light rounded-lg font-display text-sm text-muted hover:text-light hover:border-primary disabled:opacity-40 disabled:cursor-not-allowed";

function formatTimer(seconds: number) {
  const rounded = Math.max(0, Math.ceil(seconds));
  return `${Math.floor(rounded / 60)}:${String(rounded % 60).padStart(2, "0")}`;
}

function Scoreboard({
  room,
  onReview,
}: {
  room: RoomSnapshot;
  onReview?: (name: string, code: string) => void;
}) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-left text-sm border-separate border-spacing-y-2">
        <thead className="font-display uppercase text-xs tracking-wider text-dim">
          <tr>
            <th className="p-3">Rank</th>
            <th className="p-3">Player</th>
            <th className="p-3">Best</th>
            <th className="p-3">Tests</th>
            {onReview && <th className="p-3">Code</th>}
          </tr>
        </thead>
        <tbody>
          {room.rankings.map((player) => (
            <tr key={player.name} className="bg-elevated">
              <td className="p-3 rounded-l-lg font-mono text-muted">
                {player.position}
              </td>
              <td
                className={`p-3 font-display ${player.name === room.me.name ? "text-primary" : "text-light"}`}
              >
                {player.name}
              </td>
              <td className="p-3 font-mono whitespace-nowrap">
                <span className={player.solved ? "text-ok" : "text-dim"}>
                  {player.solved
                    ? `${player.charCount} chars`
                    : player.resigned
                      ? "Resigned"
                      : "Unsolved"}
                </span>
                {player.lockedAt !== null && (
                  <span className="text-warn text-xs ml-2">Locked</span>
                )}
              </td>
              <td className="p-3 font-mono text-muted">
                {player.testsPassed}/{player.testsTotal}
              </td>
              {onReview && (
                <td className="p-3 rounded-r-lg">
                  {player.code !== null && (
                    <button
                      className="text-primary hover:underline"
                      onClick={() => onReview(player.name, player.code ?? "")}
                    >
                      View
                    </button>
                  )}
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function Output({ result }: { result: Submission | null }) {
  if (!result)
    return (
      <p className="text-dim">
        Submit your code to see results. Ctrl/Cmd + Enter submits.
      </p>
    );
  return (
    <div className="flex flex-col gap-2 font-mono text-sm whitespace-pre-wrap break-words">
      <p className={result.solved ? "text-ok" : "text-warn"}>
        {result.solved
          ? `Solved! ${result.charCount} characters`
          : `${result.passed}/${result.total} tests passed`}{" "}
        <span className="text-dim">{Math.round(result.timeMs)} ms</span>
      </p>
      {result.error && <p className="text-err">{result.error}</p>}
      {result.firstFailure && (
        <div className="p-3 bg-elevated rounded border border-brd">
          <p className="text-muted mb-2">First failing test</p>
          <p>Input: {result.firstFailure.input}</p>
          <p className="text-ok">Expected: {result.firstFailure.expected}</p>
          <p className="text-err">Received: {result.firstFailure.actual}</p>
        </div>
      )}
      {result.stdout && (
        <div className="border-t border-brd pt-2 text-muted">
          Output:{"\n"}
          {result.stdout}
        </div>
      )}
      {result.stderr && <div className="text-err">{result.stderr}</div>}
    </div>
  );
}

function Chat({
  room,
  onSend,
}: {
  room: RoomSnapshot;
  onSend: (message: string) => Promise<boolean>;
}) {
  const [collapsed, setCollapsed] = useState(true);
  const [text, setText] = useState("");
  const [sending, setSending] = useState(false);
  const end = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (!collapsed) end.current?.scrollIntoView();
  }, [room.messages.length, collapsed]);

  async function send(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!text.trim() || sending) return;
    setSending(true);
    if (await onSend(text.trim())) setText("");
    setSending(false);
  }

  return (
    <aside className="fixed bottom-0 right-4 w-72 max-w-[calc(100vw-2rem)] z-30 bg-surface border border-brd rounded-t-lg shadow-panel">
      <button
        className="w-full flex justify-between p-3 font-display uppercase tracking-wider text-xs text-muted"
        onClick={() => setCollapsed(!collapsed)}
        aria-expanded={!collapsed}
      >
        Chat{" "}
        <span>
          {collapsed ? "+" : "−"} · {room.messages.length}
        </span>
      </button>
      {!collapsed && (
        <>
          <div
            className="h-48 overflow-y-auto p-3 space-y-2 border-t border-brd"
            role="log"
            aria-live="polite"
          >
            {room.messages.length === 0 && (
              <p className="text-dim text-xs">No messages yet</p>
            )}
            {room.messages.map((message) => (
              <div key={message.id} className="text-sm break-words">
                <span
                  className={`font-display text-xs ${message.sender === room.me.name ? "text-primary" : "text-muted"}`}
                >
                  {message.sender}
                </span>
                <p>{message.message}</p>
              </div>
            ))}
            <div ref={end} />
          </div>
          <form
            onSubmit={(event) => {
              void send(event);
            }}
            className="p-2 flex gap-2 border-t border-brd"
          >
            <input
              aria-label="Chat message"
              className="min-w-0 flex-1 bg-elevated border border-brd rounded p-2 text-sm outline-none focus:border-primary"
              value={text}
              onChange={(event) => setText(event.target.value)}
              maxLength={200}
              placeholder="Say something..."
            />
            <button
              disabled={sending || !text.trim()}
              className="text-primary text-sm disabled:opacity-40"
            >
              Send
            </button>
          </form>
        </>
      )}
    </aside>
  );
}

export default function Room() {
  const [params] = useSearchParams();
  const roomId = params.get("id") ?? "";
  const token = sessionToken(roomId);
  const navigate = useNavigate();
  const [room, setRoom] = useState<RoomSnapshot | null>(null);
  const [connected, setConnected] = useState(false);
  const [error, setError] = useState("");
  const [pending, setPending] = useState(false);
  const pendingRef = useRef(false);
  const [code, setCode] = useState("");
  const [result, setResult] = useState<Submission | null>(null);
  const [review, setReview] = useState<{ name: string; code: string } | null>(
    null,
  );
  const [copied, setCopied] = useState(false);
  const draftKey = room?.problem
    ? `leetrace:draft:${roomId}:${room.currentRound}:${room.problem.id}`
    : null;

  useEffect(() => {
    if (!roomId || !token) return;
    const subscription = api.roomUpdates.subscribe(
      { roomId, token },
      {
        onStarted() {
          setConnected(true);
          setError("");
        },
        onConnectionStateChange(state) {
          setConnected(state.state === "pending");
        },
        onData(snapshot) {
          setRoom(snapshot);
          setConnected(true);
        },
        onError(error) {
          setConnected(false);
          setError(errorMessage(error));
        },
      },
    );
    return () => subscription.unsubscribe();
  }, [roomId, token]);

  const starterCode = room?.problem?.starterCode;
  useEffect(() => {
    if (!draftKey || starterCode === undefined) return;
    setCode(sessionStorage.getItem(draftKey) ?? starterCode);
    setResult(null);
    setReview(null);
  }, [draftKey, starterCode]);

  async function perform(action: () => Promise<unknown>) {
    if (pendingRef.current) return false;
    pendingRef.current = true;
    setPending(true);
    setError("");
    try {
      await action();
      return true;
    } catch (error) {
      setError(errorMessage(error));
      return false;
    } finally {
      pendingRef.current = false;
      setPending(false);
    }
  }

  function changeCode(value: string) {
    setCode(value);
    if (draftKey) sessionStorage.setItem(draftKey, value);
  }

  function submit() {
    if (
      !room ||
      room.state !== "playing" ||
      room.me.locked ||
      room.me.resigned ||
      review ||
      !connected
    )
      return;
    void perform(async () => {
      setResult(await api.submit.mutate({ roomId, code }));
    });
  }

  async function leave() {
    if (await perform(() => api.leave.mutate({ roomId }))) {
      sessionStorage.removeItem(`leetrace:${roomId}`);
      navigate("/");
    }
  }

  async function copyRoom() {
    try {
      await navigator.clipboard.writeText(roomId);
      setCopied(true);
      window.setTimeout(() => setCopied(false), 2000);
    } catch {
      setError(`Room code: ${roomId}`);
    }
  }

  if (!roomId || !token) return <Navigate to="/" replace />;
  if (!room)
    return (
      <main className="min-h-screen flex flex-col items-center justify-center gap-5">
        <p className="text-muted">Connecting to room {roomId}...</p>
        {error && (
          <p role="alert" className="text-err px-5">
            {error}
          </p>
        )}
        <Link className="text-primary" to="/">
          Back home
        </Link>
      </main>
    );

  const isHost = room.host === room.me.name;
  const canAct = connected && !pending;
  const me = room.rankings.find((player) => player.name === room.me.name);
  const showEditor = room.problem && (room.state === "playing" || review);
  const readOnly =
    room.state !== "playing" ||
    room.me.locked ||
    room.me.resigned ||
    review !== null;

  return (
    <main className="min-h-screen flex flex-col">
      <header className="flex flex-wrap items-center justify-between gap-3 px-5 py-4 bg-surface border-b border-brd">
        <div className="flex items-center gap-5">
          <button
            onClick={() => {
              void leave();
            }}
            disabled={!canAct}
            className="font-display font-bold tracking-[0.15em] text-lg"
          >
            LEET<span className="text-primary">RACE</span>
          </button>
          <button
            onClick={() => {
              void copyRoom();
            }}
            title="Copy room code"
            className="font-mono tracking-widest text-primary text-sm"
          >
            {copied ? "Copied!" : roomId}
          </button>
        </div>
        <div className="flex items-center gap-4">
          <span className="font-display text-sm text-muted">
            {room.me.name}
          </span>
          <span className={`text-xs ${connected ? "text-ok" : "text-warn"}`}>
            {connected ? "Connected" : "Reconnecting..."}
          </span>
          <button
            onClick={() => {
              void leave();
            }}
            disabled={!canAct}
            className="text-muted hover:text-light text-sm disabled:opacity-40"
          >
            Leave
          </button>
        </div>
      </header>
      {error && (
        <div
          role="alert"
          className="flex justify-between gap-3 px-5 py-3 text-err bg-err/10 border-b border-err/20"
        >
          <p>{error}</p>
          <button onClick={() => setError("")} aria-label="Dismiss error">
            ×
          </button>
        </div>
      )}
      {room.state === "lobby" && (
        <section className="m-auto w-full max-w-xl px-5 py-14 text-center">
          <h1 className="font-display text-3xl font-semibold uppercase tracking-wider mb-3">
            Room lobby
          </h1>
          <p className="text-muted mb-7">
            Share the room code to invite your friends.
          </p>
          <button
            onClick={() => {
              void copyRoom();
            }}
            className="font-mono text-primary text-4xl tracking-[0.3em] mb-8"
          >
            {roomId}
          </button>
          <div className="bg-surface border border-brd rounded-xl p-6 mb-7 text-left">
            <p className="text-xs font-display uppercase tracking-wider text-dim mb-4">
              Players · {room.players.length}
            </p>
            {room.players.map((name) => (
              <p key={name} className="py-2 font-display text-light">
                {name}
                <span className="text-xs text-muted ml-3">
                  {name === room.host ? "Host" : ""}
                  {name === room.me.name ? " · You" : ""}
                </span>
              </p>
            ))}
          </div>
          <p className="text-muted text-sm mb-6">
            {room.difficulty ?? "Any difficulty"} ·{" "}
            {formatTimer(room.timeLimit)} per round · {room.totalRounds}{" "}
            {room.totalRounds === 1 ? "round" : "rounds"}
          </p>
          {isHost ? (
            <button
              disabled={!canAct}
              className={primaryButton}
              onClick={() => {
                void perform(() => api.start.mutate({ roomId }));
              }}
            >
              {pending ? "Starting..." : "Start race"}
            </button>
          ) : (
            <p className="text-primary-dim">Waiting for the host to start...</p>
          )}
        </section>
      )}
      {showEditor && room.problem && (
        <section className="flex-1 flex flex-col">
          <div className="flex flex-wrap justify-between items-center gap-3 px-5 py-3 border-b border-brd bg-panel">
            <div className="flex items-center gap-4">
              <h1 className="font-display font-semibold">
                {room.problem.title}
              </h1>
              <span
                className={`text-xs ${room.problem.difficulty === "Easy" ? "text-ok" : room.problem.difficulty === "Hard" ? "text-err" : "text-warn"}`}
              >
                {room.problem.difficulty}
              </span>
              <span className="text-xs text-dim">
                Round {room.currentRound}/{room.totalRounds}
              </span>
            </div>
            {review ? (
              <div className="flex gap-3 items-center text-sm">
                <span className="text-muted">Reviewing {review.name}</span>
                <button
                  className="text-primary"
                  onClick={() => setReview(null)}
                >
                  Back to results
                </button>
              </div>
            ) : (
              <span
                className={`font-mono text-xl ${room.remaining <= 30 ? "text-err animate-pulse-danger" : "text-primary"}`}
              >
                {formatTimer(room.remaining)}
              </span>
            )}
          </div>
          <div className="grid lg:grid-cols-[42%_58%] flex-1 min-h-0">
            <article className="problem-description p-6 border-b lg:border-b-0 lg:border-r border-brd overflow-y-auto lg:max-h-[calc(100vh-9rem)] text-sm leading-relaxed">
              <ReactMarkdown remarkPlugins={[remarkGfm]}>
                {room.problem.statement}
              </ReactMarkdown>
            </article>
            <div className="min-w-0 flex flex-col">
              <div className="flex items-center justify-between gap-3 px-4 py-2 bg-surface border-b border-brd">
                <span className="font-mono text-xs text-dim">solution.py</span>
                <span className="font-mono text-xs text-muted">
                  {Array.from(review?.code ?? code).length} chars
                </span>
              </div>
              <div className="h-[45vh] min-h-64">
                <CodeEditor
                  value={review?.code ?? code}
                  onChange={changeCode}
                  readOnly={readOnly}
                  onSubmit={submit}
                />
              </div>
              {!review && (
                <div className="flex flex-wrap gap-2 p-3 border-y border-brd bg-surface">
                  <button
                    className={primaryButton}
                    disabled={!canAct || readOnly}
                    onClick={submit}
                  >
                    {pending ? "Running..." : "Submit"}
                  </button>
                  <button
                    className={secondaryButton}
                    disabled={!canAct || readOnly || !me?.solved}
                    onClick={() => {
                      void perform(() => api.lock.mutate({ roomId }));
                    }}
                  >
                    Lock score
                  </button>
                  <button
                    className={secondaryButton}
                    disabled={!canAct || readOnly}
                    onClick={() => {
                      void perform(() => api.resign.mutate({ roomId }));
                    }}
                  >
                    Resign
                  </button>
                  {room.me.locked && (
                    <span className="self-center text-warn text-sm">
                      Score locked
                    </span>
                  )}
                  {room.me.resigned && (
                    <span className="self-center text-muted text-sm">
                      Resigned
                    </span>
                  )}
                </div>
              )}
              <div className="p-4 overflow-y-auto max-h-64 bg-panel">
                {!review && <Output result={result ?? room.me.submission} />}
              </div>
            </div>
          </div>
          {!review && (
            <div className="p-4 bg-surface border-t border-brd">
              <h2 className="font-display text-xs uppercase tracking-wider text-muted">
                Live scoreboard
              </h2>
              <Scoreboard room={room} />
            </div>
          )}
        </section>
      )}
      {room.state === "finished" && !review && (
        <section className="w-full max-w-4xl mx-auto px-5 py-14">
          <h1 className="text-center font-display text-3xl uppercase tracking-wider mb-3">
            {room.breakRemaining !== null
              ? `Round ${room.currentRound} complete`
              : "Race complete"}
          </h1>
          {room.breakRemaining !== null && (
            <p className="text-center text-muted mb-6">
              Next round in{" "}
              <span className="font-mono text-primary">
                {formatTimer(room.breakRemaining)}
              </span>
            </p>
          )}
          <Scoreboard
            room={room}
            onReview={(name, code) => setReview({ name, code })}
          />
          <div className="flex flex-wrap justify-center gap-3 mt-8">
            {isHost && (
              <button
                disabled={!canAct}
                className={primaryButton}
                onClick={() => {
                  void perform(() =>
                    room.breakRemaining !== null
                      ? api.skipBreak.mutate({ roomId })
                      : api.restart.mutate({ roomId }),
                  );
                }}
              >
                {room.breakRemaining !== null ? "Continue" : "Play again"}
              </button>
            )}
            <button
              className={secondaryButton}
              onClick={() => setReview({ name: room.me.name, code })}
            >
              View my code
            </button>
          </div>
        </section>
      )}
      <Chat
        room={room}
        onSend={(message) =>
          perform(() => api.chat.mutate({ roomId, message }))
        }
      />
    </main>
  );
}
