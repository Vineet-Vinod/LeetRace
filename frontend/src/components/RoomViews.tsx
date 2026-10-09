import type { ReactNode } from "react";
import { formatTimer, type RoomState } from "../hooks/useRoom";
import type { PaneLayout } from "../hooks/usePaneLayout";
import { ChatDock } from "./ChatDock";
import { Box, DifficultyTag, Tag } from "./crt";
import { ResultsTable } from "./Standings";

type Room = NonNullable<RoomState["room"]>;

const pad = (value: number) => String(value).padStart(2, "0");

function Screen({
  r,
  room,
  layout,
  children,
}: {
  r: RoomState;
  room: Room;
  layout: PaneLayout;
  children: ReactNode;
}) {
  return (
    <div className="flex min-h-0 flex-1 px-3 pt-3 pb-2">
      <div className="min-w-0 flex-1 overflow-y-auto">
        <div className="mx-auto flex min-h-full max-w-5xl flex-col justify-center px-2 py-8">
          {children}
        </div>
      </div>
      <ChatDock
        room={room}
        layout={layout}
        onSend={r.sendChat}
        resizable={false}
      />
    </div>
  );
}

export function LobbyView({
  r,
  room,
  layout,
}: {
  r: RoomState;
  room: Room;
  layout: PaneLayout;
}) {
  const count = room.players.length;
  return (
    <Screen r={r} room={room} layout={layout}>
      <Box
        double
        title="[ lobby :: waiting room ]"
        right={
          <span className="font-normal text-ink-dim">
            {count} connected
          </span>
        }
        className="power-on mx-auto w-full max-w-4xl"
      >
        <div className="grid md:grid-cols-[1.2fr_1fr]">
          <div className="flex flex-col gap-6 p-6 pt-7">
            <div>
              <p className="label">
                <span aria-hidden="true" className="text-amber-lo">
                  ${" "}
                </span>
                room code
              </p>
              <button
                onClick={() => void r.copyRoom()}
                aria-label={`Room code ${r.roomId}. Click to copy.`}
                className="group mt-2 -ml-2 block px-2 hover:bg-amber"
              >
                <span className="font-display text-[clamp(3.5rem,8vw,5.75rem)] leading-[0.95] tracking-[0.16em] text-amber-hi glow group-hover:text-crt-0 group-hover:[text-shadow:none]">
                  {r.roomId}
                </span>
              </button>
              <p className="mt-2 text-xs text-ink-dim" aria-live="polite">
                {r.copied ? (
                  <span className="text-phos">✔ copied to clipboard</span>
                ) : (
                  "click the code to copy · share it with your rivals"
                )}
              </p>
            </div>
            <div className="flex flex-col gap-2.5">
              <p className="rule">config</p>
              <dl className="grid grid-cols-[8.5rem_1fr] items-center gap-y-1.5 text-sm">
                <dt className="text-ink-faint">difficulty</dt>
                <dd>
                  <DifficultyTag difficulty={room.difficulty} />
                </dd>
                <dt className="text-ink-faint">time_limit</dt>
                <dd className="text-ink">
                  <span className="text-amber-hi">
                    {formatTimer(room.timeLimit)}
                  </span>{" "}
                  / round
                </dd>
                <dt className="text-ink-faint">rounds</dt>
                <dd className="text-amber-hi">{room.totalRounds}</dd>
              </dl>
            </div>
          </div>
          <div className="flex flex-col gap-2.5 border-t border-dashed border-line-hi p-6 pt-7 md:border-t-0 md:border-l">
            <p className="rule">players · {count}</p>
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="text-[0.625rem] tracking-[0.14em] text-ink-faint uppercase">
                  <th scope="col" className="w-12 py-1 font-normal">
                    pid
                  </th>
                  <th scope="col" className="py-1 font-normal">
                    user
                  </th>
                  <th scope="col" className="py-1 text-right font-normal">
                    role
                  </th>
                </tr>
              </thead>
              <tbody>
                {room.players.map((name, index) => {
                  const mine = name === room.me.name;
                  return (
                    <tr
                      key={name}
                      className={`border-t border-dashed border-line ${mine ? "bg-amber/[0.06]" : ""}`}
                    >
                      <td className="py-1.5 text-ink-faint tabular-nums">
                        {String(index + 1).padStart(3, "0")}
                      </td>
                      <td
                        className={`py-1.5 ${mine ? "font-semibold text-amber-hi" : "text-ink"}`}
                      >
                        {name}
                      </td>
                      <td className="py-1.5 text-right">
                        <span className="inline-flex gap-1">
                          {name === room.host && <Tag tone="amber">Host</Tag>}
                          {mine && <Tag tone="dim">You</Tag>}
                        </span>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
        <div className="flex flex-wrap items-center justify-between gap-3 border-t border-line px-6 py-4">
          {r.isHost ? (
            <>
              <p className="text-xs text-ink-dim">
                {count === 1
                  ? "waiting for rivals to join"
                  : `${count} players connected`}
                <span className="cursor-block" />
              </p>
              <button
                className="btn btn-solid btn-lg"
                disabled={!r.canAct}
                onClick={() => void r.start()}
              >
                {r.pending ? "Starting…" : "Start race"}
              </button>
            </>
          ) : (
            <p className="text-sm text-amber">
              waiting for host <span className="font-semibold text-amber-hi">{room.host}</span> to
              start the race
              <span className="cursor-block" />
            </p>
          )}
        </div>
      </Box>
    </Screen>
  );
}

export function FinishedView({
  r,
  room,
  layout,
}: {
  r: RoomState;
  room: Room;
  layout: PaneLayout;
}) {
  const nextIn = room.breakRemaining;
  const top = room.rankings[0];
  const winner = top?.solved ? top : null;
  return (
    <Screen r={r} room={room} layout={layout}>
      <Box
        double
        title={
          nextIn !== null
            ? `[ round ${room.currentRound}/${room.totalRounds} :: complete ]`
            : "[ race complete ]"
        }
        right={
          room.problem ? (
            <span className="font-normal text-ink-dim normal-case tracking-normal">
              {room.problem.title}
            </span>
          ) : undefined
        }
        className="power-on w-full"
      >
        <div className="flex flex-wrap items-end justify-between gap-6 px-6 pt-8 pb-6">
          <div className="flex flex-col gap-2">
            <p className="label">
              <span aria-hidden="true" className="text-amber-lo">
                ${" "}
              </span>
              ./results --round {room.currentRound}
            </p>
            <h1 className="font-display text-[clamp(2.6rem,5vw,3.9rem)] leading-[0.9] tracking-[0.04em] text-amber glow">
              {nextIn !== null
                ? `ROUND ${pad(room.currentRound)} COMPLETE`
                : "RACE COMPLETE"}
            </h1>
            <p className="text-sm text-ink-dim">
              {winner ? (
                <>
                  <span className="text-amber">▶ </span>
                  <span className="font-semibold text-amber-hi">
                    {winner.name}
                  </span>{" "}
                  {nextIn !== null ? "takes the round" : "takes the final round"}{" "}
                  with <span className="text-phos">{winner.charCount} chars</span>
                </>
              ) : (
                "nobody cracked it this round"
              )}
            </p>
          </div>
          {nextIn !== null && (
            <div className="text-right" role="timer" aria-label={`Next round in ${formatTimer(nextIn)}`}>
              <p className="label">next round in</p>
              <p className="font-display text-[3.9rem] leading-[0.9] text-amber-hi glow tabular-nums">
                {formatTimer(nextIn).padStart(5, "0")}
              </p>
            </div>
          )}
        </div>
        <div className="px-6">
          <ResultsTable
            room={room}
            onReview={(name, code) => r.setReview({ name, code })}
          />
        </div>
        <div className="mt-6 flex flex-wrap items-center gap-3 border-t border-line px-6 py-4">
          {r.isHost ? (
            <button
              className="btn btn-solid btn-lg"
              disabled={!r.canAct}
              onClick={() => void r.advance()}
            >
              {nextIn !== null ? "Continue" : "Play again"}
            </button>
          ) : (
            <p className="text-sm text-ink-dim">
              {nextIn !== null
                ? "next round starts automatically"
                : `waiting for ${room.host} to start a new race`}
              <span className="cursor-block" />
            </p>
          )}
          <button
            className="btn btn-lg"
            onClick={() => r.setReview({ name: room.me.name, code: r.code })}
          >
            View my code
          </button>
        </div>
      </Box>
    </Screen>
  );
}
