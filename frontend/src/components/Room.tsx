import { useRef, type MutableRefObject } from "react";
import { Link, Navigate } from "react-router-dom";
import { AnimatePresence, motion } from "framer-motion";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { RoomSnapshot } from "../api";
import { formatTimer, useRoom, type RoomState } from "../hooks/useRoom";
import { usePaneLayout, type PaneLayout } from "../hooks/usePaneLayout";
import CodeEditor, { type EditorInstance } from "./CodeEditor";
import Radio from "./pitlane/Radio";
import Telemetry from "./pitlane/Telemetry";
import { Classification, TimingStrip } from "./pitlane/Standings";
import {
  MONO,
  difficultyTone,
  driverCode,
  livery,
  pitLaneTheme,
} from "./pitlane/livery";

function Header({ r, room }: { r: RoomState; room: RoomSnapshot }) {
  const racing = room.state === "playing";
  const danger = racing && room.remaining <= 30;
  return (
    <header className="relative flex items-stretch h-14 bg-pit border-b border-line shrink-0">
      <Link
        to="/"
        aria-label="LeetRace home"
        className="plate flex items-center px-6 -ml-2 bg-carbon border-r border-line"
      >
        <span className="font-display text-xl font-extrabold italic uppercase tracking-tight">
          Leet<span className="text-signal">Race</span>
        </span>
      </Link>
      <button
        onClick={() => void r.copyRoom()}
        title="Copy room code"
        className="group flex flex-col justify-center px-5 border-r border-line hover:bg-raised"
      >
        <span className="label leading-none">
          {r.copied ? "Copied" : "Room"}
        </span>
        <span className="font-mono text-sm tracking-[0.25em] text-ink group-hover:text-signal-bright">
          {room.roomId}
        </span>
      </button>
      {room.currentRound > 0 && (
        <div className="flex flex-col justify-center px-5 border-r border-line">
          <span className="label leading-none">Round</span>
          <span className="font-display text-lg font-bold italic leading-tight">
            {room.currentRound}
            <span className="text-ink-dim">/{room.totalRounds}</span>
          </span>
        </div>
      )}
      <div className="flex-1" />
      <div className="hidden sm:flex items-center gap-2.5 px-5 border-l border-line">
        <span
          className={`size-2 rounded-full ${r.connected ? "bg-sector-green shadow-[0_0_8px] shadow-sector-green" : "bg-sector-yellow animate-pulse-danger"}`}
        />
        <span className="label">{r.connected ? "Live" : "Reconnecting"}</span>
      </div>
      <div className="flex items-center gap-3 px-5 border-l border-line">
        <span
          className="w-1 h-6"
          style={{ background: livery(room.me.name) }}
        />
        <span className="font-display font-semibold tracking-wide">
          {room.me.name}
        </span>
      </div>
      {(racing || r.review) && (
        <div
          className={`relative flex items-center gap-3 px-6 border-l border-line ${danger ? "bg-signal/15" : "bg-carbon"}`}
          aria-live="off"
        >
          <span className="label">{r.review ? "Review" : "Time"}</span>
          <span
            className={`font-display text-3xl font-bold italic tabular-nums tracking-tight ${danger ? "text-signal-bright animate-pulse-danger" : "text-ink"}`}
          >
            {r.review ? "FIN" : formatTimer(room.remaining)}
          </span>
          {racing && (
            <span
              className="absolute bottom-0 left-0 h-[3px] bg-signal transition-[width] duration-1000 ease-linear"
              style={{
                width: `${(room.remaining / room.timeLimit) * 100}%`,
              }}
            />
          )}
        </div>
      )}
      <button
        onClick={() => void r.leave()}
        disabled={!r.canAct}
        className="px-5 border-l border-line label hover:text-signal-bright hover:bg-raised disabled:opacity-40"
      >
        Leave
      </button>
    </header>
  );
}

function Toolbar({ r, room }: { r: RoomState; room: RoomSnapshot }) {
  const length = Array.from(r.review?.code ?? r.code).length;
  return (
    <div className="flex items-center gap-2 h-11 pl-0 pr-2 bg-pit border-b border-line shrink-0">
      <span className="relative h-full flex items-center gap-2 px-4 bg-[#0c0e11] border-r border-line">
        <span className="absolute top-0 inset-x-0 h-[2px] bg-signal" />
        <span className="font-mono text-xs text-ink">
          {r.review ? `${r.review.name}.py` : "solution.py"}
        </span>
      </span>
      <span className="font-mono text-xs text-ink-muted tabular-nums">
        {length} <span className="text-ink-dim">chars</span>
      </span>
      <div className="flex-1" />
      {r.review ? (
        <button className="btn btn-ghost h-8" onClick={() => r.setReview(null)}>
          ← Back to results
        </button>
      ) : (
        <>
          <button
            className="btn btn-ghost h-8"
            disabled={!r.canAct || r.readOnly}
            onClick={() => void r.resign()}
          >
            Resign
          </button>
          <button
            className="btn btn-lock h-8"
            disabled={!r.canAct || r.readOnly || !r.me?.solved}
            title={r.me?.solved ? "Lock in your best solution" : "Solve the problem to lock in"}
            onClick={() => void r.lock()}
          >
            Lock in
          </button>
          <button
            className="btn btn-go h-8"
            disabled={!r.canAct || r.readOnly}
            onClick={r.submit}
          >
            {r.pending && room.state === "playing" ? "Running…" : "Submit"}
            <span className="kbd">Ctrl ↵</span>
          </button>
        </>
      )}
    </div>
  );
}

function FinishedBanner({ r }: { r: RoomState }) {
  if (!r.room || !r.finished || r.review) return null;
  const locked = r.room.me.locked;
  const others = r.waitingOn;
  return (
    <motion.div
      initial={{ height: 0, opacity: 0 }}
      animate={{ height: "auto", opacity: 1 }}
      className={`flex items-center gap-3 px-4 py-2 border-b shrink-0 ${locked ? "bg-sector-yellow/10 border-sector-yellow/30" : "bg-raised border-line"}`}
      role="status"
    >
      <span
        className={`plate px-2.5 py-0.5 font-display text-xs font-bold uppercase tracking-[0.18em] ${locked ? "bg-sector-yellow text-carbon" : "bg-ink-dim text-ink"}`}
      >
        <span className="block">{locked ? "Locked in" : "Resigned"}</span>
      </span>
      <span className="text-sm text-ink-muted">
        {others.length
          ? `Waiting on ${others.join(", ")} to finish.`
          : "Wrapping up the round…"}
      </span>
    </motion.div>
  );
}

function ReviewSummary({ r, room }: { r: RoomState; room: RoomSnapshot }) {
  const player = room.rankings.find((entry) => entry.name === r.review?.name);
  if (!player) return null;
  return (
    <div className="flex flex-col gap-2">
      <p className="label">Reviewing</p>
      <p className="font-display text-2xl font-bold italic">
        P{player.position} · {player.name}
      </p>
      <p className="font-mono text-sm text-ink-muted">
        {player.solved ? `${player.charCount} chars` : "Unsolved"} ·{" "}
        {player.testsPassed}/{player.testsTotal} tests
      </p>
    </div>
  );
}

function Track({
  r,
  room,
  layout,
  editorRef,
}: {
  r: RoomState;
  room: RoomSnapshot;
  layout: PaneLayout;
  editorRef: MutableRefObject<EditorInstance | null>;
}) {
  const problem = room.problem;
  if (!problem) return null;
  const { wide } = layout;
  return (
    <>
      <article
        className={`flex flex-col min-w-0 bg-panel ${wide ? "" : "h-[45vh] shrink-0 border-b border-line"}`}
        style={wide ? { flex: "1 1 0" } : undefined}
      >
        <div className="flex items-center gap-3 h-11 px-5 border-b border-line shrink-0">
          <span className="label">Brief</span>
          <span
            className={`plate px-2 py-0.5 font-display text-[11px] font-bold uppercase tracking-[0.14em] ${difficultyTone[problem.difficulty]}`}
          >
            <span className="block">{problem.difficulty}</span>
          </span>
        </div>
        <div className="flex-1 overflow-y-auto px-6 py-5">
          <h1 className="font-display text-2xl font-bold italic uppercase tracking-wide leading-tight mb-4">
            {problem.title}
          </h1>
          <div className="problem-description">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
              {problem.statement}
            </ReactMarkdown>
          </div>
        </div>
      </article>
      {wide && <div className="splitter" {...layout.handleProps("problem")} />}
      <div
        ref={layout.columnRef}
        className={`flex flex-col min-w-0 ${wide ? "" : "shrink-0"}`}
        style={wide ? { flex: `0 0 ${layout.editorWidth}px` } : undefined}
      >
        <Toolbar r={r} room={room} />
        <AnimatePresence>
          <FinishedBanner r={r} />
        </AnimatePresence>
        <div className={`relative bg-[#0c0e11] ${wide ? "flex-1 min-h-0" : "h-[55vh]"}`}>
          <CodeEditor
            value={r.review?.code ?? r.code}
            onChange={r.changeCode}
            readOnly={r.readOnly}
            onSubmit={r.submit}
            theme={pitLaneTheme}
            fontFamily={MONO}
            onEditor={(editor) => {
              editorRef.current = editor;
            }}
            loading={
              <div className="h-full grid place-items-center label">
                Warming tyres…
              </div>
            }
          />
        </div>
        {wide && <div className="splitter" {...layout.handleProps("results")} />}
        <section
          aria-label="Submission results"
          className="flex flex-col bg-pit min-h-0"
          style={wide ? { height: layout.resultsHeight } : undefined}
        >
          <div className="flex items-center gap-3 h-9 px-4 border-b border-line shrink-0">
            <span className="label">Telemetry</span>
            {r.pending && room.state === "playing" && (
              <span className="flex items-center gap-2 label text-signal">
                <span className="size-1.5 bg-signal rounded-full animate-pulse-danger" />
                Running tests
              </span>
            )}
          </div>
          <div className="flex-1 overflow-y-auto p-4">
            {r.review ? (
              <ReviewSummary r={r} room={room} />
            ) : (
              <Telemetry result={r.result} />
            )}
          </div>
        </section>
      </div>
    </>
  );
}

function Lights({ lit }: { lit: boolean }) {
  return (
    <div className="flex gap-3 p-3 bg-carbon border border-line w-fit">
      {[0, 1, 2, 3, 4].map((light) => (
        <div key={light} className="flex flex-col gap-2 p-1.5 bg-[#111] rounded">
          {[0, 1].map((row) => (
            <span
              key={row}
              className={`size-6 rounded-full ${lit ? "animate-light-on" : "bg-[#2a0b0d]"}`}
              style={{ animationDelay: `${light * 0.35}s` }}
            />
          ))}
        </div>
      ))}
    </div>
  );
}

function Grid({ r, room }: { r: RoomState; room: RoomSnapshot }) {
  return (
    <div className="flex-1 overflow-y-auto">
      <div className="max-w-5xl mx-auto px-6 py-12 grid lg:grid-cols-[1fr_1.1fr] gap-12">
        <section>
          <p className="label text-signal mb-3">Formation lap</p>
          <h1 className="font-display text-5xl font-extrabold italic uppercase leading-none mb-6">
            Starting grid
          </h1>
          <p className="text-ink-muted mb-8 max-w-sm">
            Share the room code. Everyone races the same problem when the host
            gets the lights going.
          </p>
          <button
            onClick={() => void r.copyRoom()}
            className="group block text-left mb-8"
            title="Copy room code"
          >
            <span className="label">{r.copied ? "Copied to clipboard" : "Room code · click to copy"}</span>
            <span className="block font-mono text-5xl tracking-[0.3em] mt-2 group-hover:text-signal-bright transition-colors">
              {room.roomId}
            </span>
          </button>
          <dl className="grid grid-cols-3 border-l-2 border-signal mb-10">
            {[
              ["Difficulty", room.difficulty ?? "Any"],
              ["Lap time", formatTimer(room.timeLimit)],
              ["Rounds", String(room.totalRounds)],
            ].map(([label, value]) => (
              <div key={label} className="px-4 border-r border-line">
                <dt className="label">{label}</dt>
                <dd className="font-display text-2xl font-bold italic mt-1">
                  {value}
                </dd>
              </div>
            ))}
          </dl>
          <Lights lit={r.isHost && r.pending} />
          <div className="mt-6">
            {r.isHost ? (
              <button
                disabled={!r.canAct}
                className="btn btn-go h-12 px-8 text-base"
                onClick={() => void r.start()}
              >
                {r.pending ? "Lights out…" : "Start the race"}
              </button>
            ) : (
              <p className="flex items-center gap-3 font-display uppercase italic tracking-[0.16em] text-ink-muted">
                <span className="size-2 bg-sector-yellow rounded-full animate-pulse-danger" />
                Waiting for {room.host} to start
              </p>
            )}
          </div>
        </section>
        <section>
          <p className="label mb-4">
            Drivers · {room.players.length}/20
          </p>
          <ol className="grid grid-cols-2 gap-x-4 gap-y-3">
            {room.players.map((name, index) => (
              <motion.li
                key={name}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.05 }}
                className={`relative flex items-center gap-3 h-16 px-4 bg-panel border-t-2 ${index % 2 ? "translate-y-6" : ""}`}
                style={{ borderColor: livery(name) }}
              >
                <span className="font-display text-2xl font-extrabold italic text-ink-dim w-8">
                  {index + 1}
                </span>
                <span className="flex flex-col min-w-0">
                  <span className="font-display text-lg font-semibold tracking-wide truncate">
                    {name}
                  </span>
                  <span className="label">
                    {driverCode(name)}
                    {name === room.host && " · Host"}
                    {name === room.me.name && " · You"}
                  </span>
                </span>
              </motion.li>
            ))}
          </ol>
        </section>
      </div>
    </div>
  );
}

function Chequered({ r, room }: { r: RoomState; room: RoomSnapshot }) {
  const onBreak = room.breakRemaining !== null;
  return (
    <div className="flex-1 overflow-y-auto">
      <div className="chequer h-6 opacity-90" />
      <div className="max-w-5xl mx-auto px-6 py-10">
        <div className="flex flex-wrap items-end justify-between gap-6 mb-8">
          <div>
            <p className="label text-signal mb-2">
              {onBreak ? `Round ${room.currentRound} of ${room.totalRounds}` : "Chequered flag"}
            </p>
            <h1 className="font-display text-5xl font-extrabold italic uppercase leading-none">
              {onBreak ? "Round complete" : "Race complete"}
            </h1>
          </div>
          {onBreak && (
            <div className="text-right">
              <p className="label">Next round in</p>
              <p className="font-display text-5xl font-bold italic tabular-nums text-signal">
                {formatTimer(room.breakRemaining ?? 0)}
              </p>
            </div>
          )}
        </div>
        <Classification
          room={room}
          onReview={(name, code) => r.setReview({ name, code })}
        />
        <div className="flex flex-wrap gap-3 mt-8">
          {r.isHost && (
            <button
              disabled={!r.canAct}
              className="btn btn-go h-11 px-6"
              onClick={() => void r.advance()}
            >
              {onBreak ? "Next round now" : "Race again"}
            </button>
          )}
          <button
            className="btn btn-ghost h-11 px-6"
            onClick={() => r.setReview({ name: room.me.name, code: r.code })}
          >
            View my code
          </button>
          {!r.isHost && onBreak && (
            <p className="self-center text-sm text-ink-dim ml-2">
              The host can start the next round early.
            </p>
          )}
        </div>
      </div>
    </div>
  );
}

export default function Room() {
  const r = useRoom();
  const editorRef = useRef<EditorInstance | null>(null);
  const layout = usePaneLayout({
    messageCount: r.room?.messages.length ?? 0,
    onChatClosed: () => editorRef.current?.focus(),
  });

  if (!r.roomId || !r.token) return <Navigate to="/" replace />;
  const { room } = r;
  if (!room)
    return (
      <main className="min-h-screen flex flex-col items-center justify-center gap-6">
        <Lights lit />
        <p className="font-display uppercase italic tracking-[0.2em] text-ink-muted">
          Connecting to room {r.roomId}
        </p>
        {r.error && (
          <p role="alert" className="text-signal-bright px-5">
            {r.error}
          </p>
        )}
        <Link className="btn btn-ghost" to="/">
          Back to the paddock
        </Link>
      </main>
    );

  const onTrack = Boolean(room.problem && (room.state === "playing" || r.review));
  return (
    <main className="h-screen flex flex-col overflow-hidden">
      <Header r={r} room={room} />
      <AnimatePresence>
        {r.error && (
          <motion.div
            role="alert"
            initial={{ height: 0 }}
            animate={{ height: "auto" }}
            exit={{ height: 0 }}
            className="overflow-hidden shrink-0"
          >
            <div className="flex items-center gap-3 px-5 py-2 bg-signal/12 border-b border-signal/40 text-sm">
              <span className="plate px-2 bg-signal font-display text-xs font-bold uppercase tracking-widest">
                <span className="block">Flag</span>
              </span>
              <p className="flex-1 text-ink">{r.error}</p>
              <button
                onClick={() => r.setError("")}
                aria-label="Dismiss error"
                className="text-ink-muted hover:text-ink"
              >
                ✕
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
      {onTrack && !r.review && <TimingStrip room={room} />}
      <div
        ref={layout.containerRef}
        className={`flex-1 min-h-0 flex ${layout.wide ? "" : "flex-col overflow-y-auto"}`}
      >
        {onTrack ? (
          <Track r={r} room={room} layout={layout} editorRef={editorRef} />
        ) : room.state === "lobby" ? (
          <Grid r={r} room={room} />
        ) : (
          <Chequered r={r} room={room} />
        )}
        {layout.wide && layout.chatOpen && (
          <div className="splitter" {...layout.handleProps("chat")} />
        )}
        <Radio room={room} layout={layout} onSend={r.sendChat} />
      </div>
    </main>
  );
}
