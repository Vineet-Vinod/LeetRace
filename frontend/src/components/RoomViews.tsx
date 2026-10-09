import { motion } from "framer-motion";
import { formatTimer, type RoomState } from "../hooks/useRoom";
import { ResultsTable } from "./Standings";
import { Avatar, DifficultyPill, Icon, LiveDot, Spinner, cx } from "./ui";

const enter = {
  initial: { opacity: 0, y: 8 },
  animate: { opacity: 1, y: 0 },
  transition: { duration: 0.35, ease: [0.22, 1, 0.36, 1] },
} as const;

export function Lobby({ r }: { r: RoomState }) {
  const room = r.room!;
  return (
    <div className="relative min-h-0 min-w-0 flex-1 overflow-y-auto">
      <div aria-hidden className="backdrop-grid pointer-events-none absolute inset-0" />
      <motion.div {...enter} className="relative mx-auto w-full max-w-[540px] px-4 py-10 sm:py-14">
        <div className="mb-6 text-center">
          <span className="pill pill-accent mb-4">
            <LiveDot tone="accent" /> Lobby open
          </span>
          <h1 className="text-[24px] font-semibold tracking-[-0.02em] text-fg">
            Invite your rivals
          </h1>
          <p className="mt-1.5 text-[14px] text-fg-muted">
            Share this code. Others join from the home page.
          </p>
        </div>

        <section className="pop overflow-hidden">
          <div className="flex flex-col items-center gap-4 px-6 py-6">
            <button
              type="button"
              onClick={() => {
                void r.copyRoom();
              }}
              aria-label={`Copy room code ${r.roomId}`}
              className="group flex gap-1.5 rounded-xl p-1 transition-colors"
            >
              {Array.from(r.roomId).map((char, index) => (
                <span
                  key={index}
                  className="flex h-14 w-11 items-center justify-center rounded-lg border border-line-strong bg-sunken font-mono text-[26px] font-medium text-fg shadow-[inset_0_1px_0_rgb(255_255_255/0.03)] transition-colors group-hover:border-line-hover"
                >
                  {char}
                </span>
              ))}
            </button>
            <button
              type="button"
              onClick={() => {
                void r.copyRoom();
              }}
              className={cx("btn btn-secondary btn-sm", r.copied && "!text-ok")}
            >
              {r.copied ? <Icon.check size={14} /> : <Icon.copy size={14} />}
              {r.copied ? "Copied to clipboard" : "Copy code"}
            </button>
          </div>

          <dl className="grid grid-cols-3 border-y border-line bg-surface/60">
            <div className="flex flex-col gap-1 px-5 py-3.5">
              <dt className="section-label">Difficulty</dt>
              <dd>
                <DifficultyPill difficulty={room.difficulty} />
              </dd>
            </div>
            <div className="flex flex-col gap-1 border-x border-line px-5 py-3.5">
              <dt className="section-label">Time per round</dt>
              <dd className="font-mono text-[14px] tabular-nums text-fg">
                {formatTimer(room.timeLimit)}
              </dd>
            </div>
            <div className="flex flex-col gap-1 px-5 py-3.5">
              <dt className="section-label">Rounds</dt>
              <dd className="font-mono text-[14px] tabular-nums text-fg">
                {room.totalRounds}
              </dd>
            </div>
          </dl>

          <div className="px-5 py-4">
            <h2 className="section-label mb-2 flex items-center gap-1.5">
              Players
              <span className="font-mono tabular-nums text-fg-muted">
                {room.players.length}
              </span>
            </h2>
            <ul className="flex flex-col">
              {room.players.map((name) => (
                <motion.li
                  key={name}
                  layout
                  initial={{ opacity: 0, x: -4 }}
                  animate={{ opacity: 1, x: 0 }}
                  className="flex h-10 items-center gap-3 border-b border-line/70 last:border-b-0"
                >
                  <Avatar name={name} size={26} />
                  <span className="truncate text-[13.5px] font-medium text-fg">{name}</span>
                  <span className="ml-auto flex gap-1.5">
                    {name === room.me.name && <span className="pill">You</span>}
                    {name === room.host && <span className="pill pill-accent">Host</span>}
                  </span>
                </motion.li>
              ))}
            </ul>
          </div>

          <footer className="flex items-center justify-between gap-3 border-t border-line bg-surface/60 px-5 py-3.5">
            {r.isHost ? (
              <>
                <p className="text-[12.5px] text-fg-subtle">
                  {room.players.length === 1
                    ? "You can start solo or wait for others."
                    : `${room.players.length} players ready.`}
                </p>
                <button
                  type="button"
                  disabled={!r.canAct}
                  className="btn btn-primary"
                  onClick={() => {
                    void r.start();
                  }}
                >
                  {r.pending ? <Spinner /> : <Icon.play size={13} />}
                  {r.pending ? "Starting…" : "Start race"}
                </button>
              </>
            ) : (
              <p className="flex items-center gap-2.5 text-[13px] text-fg-muted">
                <Spinner className="text-fg-subtle" />
                <span>
                  Waiting for <span className="font-medium text-fg">{room.host}</span> to
                  start the race
                </span>
              </p>
            )}
          </footer>
        </section>
      </motion.div>
    </div>
  );
}

export function Finished({ r }: { r: RoomState }) {
  const room = r.room!;
  const breakLeft = room.breakRemaining;
  const leader = room.rankings[0];
  const lastRound = breakLeft === null;

  return (
    <div className="min-h-0 min-w-0 flex-1 overflow-y-auto">
      <motion.div {...enter} className="mx-auto w-full max-w-[780px] px-4 py-10 sm:py-14">
        <div className="mb-6 flex flex-wrap items-end justify-between gap-4">
          <div>
            <p className="section-label mb-2">
              Round {room.currentRound} of {room.totalRounds}
            </p>
            <h1 className="text-[24px] font-semibold tracking-[-0.02em] text-fg">
              {lastRound ? "Race complete" : `Round ${room.currentRound} complete`}
            </h1>
            <p className="mt-1.5 text-[14px] text-fg-muted">
              {leader?.solved ? (
                <>
                  <span className="font-medium text-fg">
                    {leader.name === room.me.name ? "You" : leader.name}
                  </span>{" "}
                  took the round with{" "}
                  <span className="font-mono tabular-nums text-ok">{leader.charCount}</span>{" "}
                  characters.
                </>
              ) : (
                "Nobody solved this one."
              )}
            </p>
          </div>
          {!lastRound && (
            <div className="panel flex items-center gap-3 px-4 py-2.5">
              <Icon.clock size={15} className="text-fg-subtle" />
              <div>
                <p className="text-[11.5px] text-fg-subtle">Next round in</p>
                <p
                  className="font-mono text-[20px] font-medium leading-tight tabular-nums text-fg"
                  aria-live="off"
                >
                  {formatTimer(breakLeft ?? 0)}
                </p>
              </div>
            </div>
          )}
        </div>

        <section className="panel overflow-hidden">
          {room.problem && (
            <header className="flex items-center gap-2 border-b border-line px-4 py-3">
              <Icon.doc size={14} className="text-fg-subtle" />
              <h2 className="truncate text-[13px] font-medium text-fg">{room.problem.title}</h2>
              <DifficultyPill difficulty={room.problem.difficulty} />
            </header>
          )}
          <ResultsTable room={room} onReview={(name, code) => r.setReview({ name, code })} />
        </section>

        <div className="mt-6 flex flex-wrap items-center justify-end gap-2">
          {!r.isHost && (
            <p className="mr-auto text-[12.5px] text-fg-subtle">
              {lastRound
                ? `Waiting for ${room.host} to start a new race.`
                : `${room.host} can skip the break.`}
            </p>
          )}
          <button
            type="button"
            className="btn btn-secondary"
            onClick={() => r.setReview({ name: room.me.name, code: r.code })}
          >
            <Icon.file size={14} />
            View my code
          </button>
          {r.isHost && (
            <button
              type="button"
              disabled={!r.canAct}
              className="btn btn-primary"
              onClick={() => {
                void r.advance();
              }}
            >
              {r.pending ? <Spinner /> : <Icon.play size={13} />}
              {lastRound ? "Play again" : "Continue"}
            </button>
          )}
        </div>
      </motion.div>
    </div>
  );
}
