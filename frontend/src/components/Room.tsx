import { useRef, type MutableRefObject } from "react";
import { Link, Navigate } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { editor as monacoEditor } from "monaco-editor/esm/vs/editor/editor.api.js";
import { formatTimer, useRoom, type RoomState } from "../hooks/useRoom";
import { usePaneLayout, type PaneLayout } from "../hooks/usePaneLayout";
import CodeEditor, { type EditorInstance } from "./CodeEditor";
import { ChatDock } from "./ChatDock";
import { Box, DifficultyTag, Tag } from "./crt";
import { EDITOR_FONT, phosphorTheme } from "./phosphorTheme";
import { ReviewSummary, SubmissionResults } from "./ResultsPane";
import { FinishedView, LobbyView } from "./RoomViews";
import { StandingsStrip } from "./Standings";

type Room = NonNullable<RoomState["room"]>;

const clock = (seconds: number) => formatTimer(seconds).padStart(5, "0");

function Header({ r, room }: { r: RoomState; room: Room }) {
  const playing = room.state === "playing" && !r.review;
  const danger = playing && room.remaining <= 30;
  let timerLabel = "standby";
  let timerValue = clock(room.timeLimit);
  if (playing) {
    timerLabel = "t-minus";
    timerValue = clock(room.remaining);
  } else if (r.review) {
    timerLabel = "mode";
    timerValue = "REVIEW";
  } else if (room.state === "finished") {
    timerLabel = room.breakRemaining !== null ? "next rnd" : "game over";
    timerValue =
      room.breakRemaining !== null ? clock(room.breakRemaining) : "00:00";
  }

  return (
    <header className="flex flex-none flex-wrap items-center gap-x-4 gap-y-1 border-b border-line bg-crt-1 px-4 py-1.5">
      <span
        className="font-display text-[2rem] leading-none tracking-[0.08em] text-amber-hi glow select-none"
        aria-label="LeetRace"
      >
        LEETRACE
        <span aria-hidden="true" className="ml-0.5 animate-blink text-amber-lo">
          _
        </span>
      </span>
      <button
        onClick={() => void r.copyRoom()}
        title="Copy room code"
        aria-label={`Room code ${r.roomId}. Click to copy.`}
        className="group flex items-baseline gap-2 border border-line-hi px-2 py-0.5 hover:border-amber hover:bg-amber hover:text-crt-0"
      >
        <span className="label group-hover:text-crt-0">room</span>
        <span className="font-semibold tracking-[0.25em] text-amber-hi group-hover:text-crt-0">
          {r.roomId}
        </span>
        <span className="text-[0.625rem] text-ink-faint uppercase group-hover:text-crt-0 max-lg:hidden">
          {r.copied ? "✔ copied" : "⧉ copy"}
        </span>
      </button>
      <span className="flex items-baseline gap-2">
        <span className="label">rnd</span>
        <span className="tabular-nums text-ink">
          {String(room.currentRound).padStart(2, "0")}
          <span className="text-ink-faint">/</span>
          {String(room.totalRounds).padStart(2, "0")}
        </span>
      </span>
      <div className="flex min-w-0 flex-1 items-center gap-2 overflow-hidden max-lg:hidden">
        {room.problem && room.state !== "lobby" && (
          <>
            <span aria-hidden="true" className="text-amber-lo">
              »
            </span>
            <h1 className="min-w-0 truncate font-semibold text-ink">
              {room.problem.title}
            </h1>
            <DifficultyTag difficulty={room.problem.difficulty} />
          </>
        )}
      </div>
      <div
        className="flex items-baseline gap-2 max-lg:ml-auto"
        role="timer"
        aria-label={`${timerLabel} ${timerValue}`}
      >
        <span className={`label ${danger ? "text-alarm" : ""} max-lg:hidden`}>
          {timerLabel}
        </span>
        <span
          className={`font-display text-[2.6rem] leading-[0.9] tabular-nums ${danger ? "danger-pulse text-alarm glow-alarm" : playing ? "text-amber-hi glow" : "text-ink-dim"}`}
        >
          {timerValue}
        </span>
      </div>
      <span className="flex items-center gap-2 border-l border-line pl-4">
        <span className="text-ink-faint">@</span>
        <span className="max-w-[14ch] truncate font-semibold text-amber">
          {room.me.name}
        </span>
        {r.isHost && <Tag tone="amber">Host</Tag>}
      </span>
      <span
        role="status"
        className={`flex items-center gap-1.5 text-[0.6875rem] tracking-[0.1em] uppercase ${r.connected ? "text-phos" : "text-alarm"}`}
      >
        <span aria-hidden="true" className={r.connected ? "glow-phos" : "animate-blink"}>
          {r.connected ? "●" : "○"}
        </span>
        <span className="max-lg:sr-only">
          {r.connected ? "online" : "reconnecting"}
        </span>
      </span>
      <button
        className="btn btn-danger"
        onClick={() => void r.leave()}
        disabled={!r.canAct}
      >
        Leave
      </button>
    </header>
  );
}

function ErrorBanner({ r }: { r: RoomState }) {
  return (
    <div
      role="alert"
      className="flex flex-none items-center gap-3 border-b border-alarm-lo bg-alarm/10 px-4 py-1.5 text-xs text-alarm"
    >
      <span className="font-bold tracking-[0.12em]">!! ERR</span>
      <p className="min-w-0 flex-1 break-words">{r.error}</p>
      <button
        className="btn btn-danger py-0.5"
        onClick={() => r.setError("")}
        aria-label="Dismiss error"
      >
        x
      </button>
    </div>
  );
}

function DoneBanner({ r, room }: { r: RoomState; room: Room }) {
  const resigned = room.me.resigned;
  const waiting = r.waitingOn.length
    ? `waiting on ${r.waitingOn.join(", ")}`
    : "round wrapping up";
  return (
    <div
      role="status"
      className={`flex flex-none flex-wrap items-center gap-x-3 gap-y-1 border-b px-4 py-1.5 text-xs ${resigned ? "border-alarm-lo bg-alarm/[0.08]" : "border-phos-lo bg-phos/[0.06]"}`}
    >
      <span
        className={`font-bold tracking-[0.12em] uppercase ${resigned ? "text-alarm glow-alarm" : "text-phos glow-phos"}`}
      >
        {resigned
          ? "✘ You resigned"
          : `■ Score locked${r.me?.charCount ? ` · ${r.me.charCount} chars` : ""}`}
      </span>
      <span className="text-ink-faint">·</span>
      <span className="text-ink">
        {waiting}
        <span className="cursor-block" />
      </span>
      <span className="ml-auto text-ink-faint">editor is read-only</span>
    </div>
  );
}

function StatusLine({
  r,
  room,
  layout,
}: {
  r: RoomState;
  room: Room;
  layout: PaneLayout;
}) {
  const mode = r.review
    ? "review"
    : room.state === "lobby"
      ? "lobby"
      : room.state === "finished"
        ? room.breakRemaining !== null
          ? "break"
          : "game over"
        : room.me.resigned
          ? "resigned"
          : room.me.locked
            ? "locked"
            : "race";
  return (
    <footer className="statusline" aria-label="Status line">
      <span
        className={`seg-mode uppercase ${mode === "resigned" ? "bg-alarm" : mode === "locked" ? "bg-phos" : ""}`}
      >
        {mode}
      </span>
      <span className="seg-alt">⎇ {r.roomId}</span>
      <span>
        round {room.currentRound}/{room.totalRounds}
      </span>
      <span className="max-sm:hidden">
        {room.players.length} player{room.players.length === 1 ? "" : "s"}
      </span>
      {room.state === "playing" && !r.review && (
        <span className="max-md:hidden">
          {Array.from(r.code).length} chars · python3 · utf-8
        </span>
      )}
      <span className="ml-auto max-md:hidden">
        ^D chat
        {layout.unread > 0 && (
          <span className="bg-amber px-1 font-bold text-crt-0">
            {layout.unread}
          </span>
        )}
      </span>
      {room.state === "playing" && !r.readOnly && (
        <span className="max-md:hidden">^⏎ submit</span>
      )}
      <span className={`seg-alt ${r.connected ? "" : "text-alarm"}`}>
        {r.connected ? "LINK OK" : "NO CARRIER"}
      </span>
    </footer>
  );
}

function Workspace({
  r,
  room,
  layout,
  editorRef,
}: {
  r: RoomState;
  room: Room;
  layout: PaneLayout;
  editorRef: MutableRefObject<EditorInstance | null>;
}) {
  const problem = room.problem;
  const reviewing = useRef(r.review);
  reviewing.current = r.review;
  if (!problem) return null;

  const review = r.review;
  const value = review?.code ?? r.code;
  const chars = Array.from(value).length;
  const wide = layout.wide;

  const problemPane = (
    <Box
      title={`[ ${problem.id}.md ]`}
      right={<DifficultyTag difficulty={problem.difficulty} />}
      style={wide ? { flex: "1 1 0", minWidth: 0 } : { height: "46vh", minHeight: 260 }}
      aria-label="Problem"
      className={wide ? "" : "flex-none"}
    >
      <article className="problem-description min-h-0 flex-1 overflow-y-auto px-5 pt-5 pb-6">
        <h1 className="!mt-0 !text-[2.1rem]">{problem.title}</h1>
        <ReactMarkdown remarkPlugins={[remarkGfm]}>{problem.statement}</ReactMarkdown>
      </article>
    </Box>
  );

  const toolbar = review ? (
    <div className="flex flex-none flex-wrap items-center gap-x-3 gap-y-1 border-b border-line px-3 pt-3 pb-2 text-xs">
      <span className="text-ink-dim">
        reviewing <span className="font-semibold text-amber-hi">{review.name}</span>
        <span className="text-ink-faint"> · </span>
        <span className="tabular-nums text-amber-hi">{chars}</span> chars
      </span>
      <button className="btn btn-solid ml-auto" onClick={() => r.setReview(null)}>
        Back to results <span className="kbd">◂</span>
      </button>
    </div>
  ) : (
    <div className="flex flex-none flex-wrap items-center gap-x-3 gap-y-1 border-b border-line px-3 pt-3 pb-2 text-xs">
      <span className="text-ink-dim">
        <span className="tabular-nums font-semibold text-amber-hi">{chars}</span> chars
        <span className="text-ink-faint"> · </span>
        <span className={r.readOnly ? "text-alarm" : "text-phos"}>
          {r.readOnly ? "-- READ-ONLY --" : "-- INSERT --"}
        </span>
      </span>
      <div className="ml-auto flex flex-wrap gap-1">
        <button
          className="btn btn-solid"
          disabled={!r.canAct || r.readOnly}
          onClick={r.submit}
          aria-keyshortcuts="Control+Enter"
        >
          {r.pending ? "Running…" : "Submit"} <span className="kbd">^⏎</span>
        </button>
        <button
          className="btn btn-ok"
          disabled={!r.canAct || r.readOnly || !r.me?.solved}
          onClick={() => void r.lock()}
          title={r.me?.solved ? "Lock your best score and finish" : "Solve first to lock a score"}
        >
          Lock score
        </button>
        <button
          className="btn btn-danger"
          disabled={!r.canAct || r.readOnly}
          onClick={() => void r.resign()}
        >
          Resign
        </button>
      </div>
    </div>
  );

  const editorPane = (
    <Box
      double
      title={`[ ${review ? `${review.name}.py` : "solution.py"} ]`}
      right={
        <span className={r.readOnly ? "text-ink-faint" : "text-phos"}>
          {r.readOnly ? "ro" : "rw"}
        </span>
      }
      aria-label="Code editor"
      className={wide ? "min-h-0 flex-1" : "flex-none"}
      style={wide ? undefined : { height: "64vh", minHeight: 380 }}
    >
      {toolbar}
      <div className="relative min-h-0 flex-1">
        <div className="absolute inset-0">
          <CodeEditor
            value={value}
            onChange={(next) => {
              if (!reviewing.current) r.changeCode(next);
            }}
            readOnly={r.readOnly}
            onSubmit={r.submit}
            theme={phosphorTheme}
            fontFamily={EDITOR_FONT}
            onEditor={(editor) => {
              editorRef.current = editor;
              void document.fonts.ready.then(() => monacoEditor.remeasureFonts());
            }}
            loading={
              <p className="text-sm text-ink-dim">
                loading editor
                <span className="cursor-block" />
              </p>
            }
          />
        </div>
      </div>
    </Box>
  );

  const resultsPane = (
    <Box
      title={review ? "[ review ]" : "[ results ]"}
      right={
        !review && r.result ? (
          <span className="font-normal text-ink-faint">
            {Math.round(r.result.timeMs)} ms
          </span>
        ) : undefined
      }
      aria-label="Results"
      className="flex-none"
      style={{ height: wide ? layout.resultsHeight : 260 }}
    >
      <div className="min-h-0 flex-1 overflow-y-auto px-4 pt-4 pb-3">
        {review ? (
          <ReviewSummary
            name={review.name}
            player={room.rankings.find((player) => player.name === review.name)}
            chars={chars}
          />
        ) : (
          <SubmissionResults result={r.result} pending={r.pending} />
        )}
      </div>
    </Box>
  );

  const chat = (
    <ChatDock room={room} layout={layout} onSend={r.sendChat} resizable />
  );

  if (!wide)
    return (
      <div className="flex min-h-0 flex-1 flex-col gap-5 overflow-y-auto px-3 pt-4 pb-4">
        {problemPane}
        {editorPane}
        {resultsPane}
        {chat}
      </div>
    );

  return (
    <div ref={layout.containerRef} className="flex min-h-0 flex-1 px-3 pt-3 pb-2">
      {problemPane}
      <div className="handle" {...layout.handleProps("problem")} />
      <div
        ref={layout.columnRef}
        className="flex min-h-0 flex-col"
        style={{ flex: `0 0 ${layout.editorWidth}px` }}
      >
        {editorPane}
        <div className="handle handle-h" {...layout.handleProps("results")} />
        {resultsPane}
      </div>
      {chat}
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
  const room = r.room;
  if (!room)
    return (
      <main className="grid h-dvh place-items-center px-5">
        <div className="flex max-w-lg flex-col gap-4 text-sm">
          <p className="text-ink-dim">
            <span aria-hidden="true" className="text-amber-lo">
              &gt;{" "}
            </span>
            ATDT {r.roomId} — dialing room
            <span className="cursor-block" />
          </p>
          {r.error && (
            <p role="alert" className="text-alarm">
              !! {r.error}
            </p>
          )}
          <Link className="btn self-start" to="/">
            Back to terminal
          </Link>
        </div>
      </main>
    );

  const workspace =
    room.problem !== null && (room.state === "playing" || r.review !== null);

  return (
    <div className="flex h-dvh flex-col">
      <Header r={r} room={room} />
      {r.error && <ErrorBanner r={r} />}
      {room.state === "playing" && <StandingsStrip room={room} />}
      {room.state === "playing" && r.finished && <DoneBanner r={r} room={room} />}
      <main className="flex min-h-0 flex-1 flex-col">
        {workspace ? (
          <Workspace r={r} room={room} layout={layout} editorRef={editorRef} />
        ) : room.state === "lobby" ? (
          <LobbyView r={r} room={room} layout={layout} />
        ) : (
          <FinishedView r={r} room={room} layout={layout} />
        )}
      </main>
      <StatusLine r={r} room={room} layout={layout} />
    </div>
  );
}
