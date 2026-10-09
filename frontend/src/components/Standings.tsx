import type { RoomSnapshot } from "../api";
import type { Ranking } from "../hooks/useRoom";
import { Avatar, Icon, cx } from "./ui";

function StatusBadges({ player }: { player: Ranking }) {
  return (
    <>
      {player.lockedAt !== null && (
        <span className="pill pill-warn">
          <Icon.lock size={10} strokeWidth={2} />
          Locked
        </span>
      )}
      {player.resigned && <span className="pill">Resigned</span>}
      {player.away && (
        <span className="pill border-dashed text-fg-subtle">Away</span>
      )}
    </>
  );
}

function Score({ player }: { player: Ranking }) {
  if (player.solved)
    return (
      <span className="font-mono text-[12px] tabular-nums text-ok">
        {player.charCount}
        <span className="text-ok/60"> ch</span>
      </span>
    );
  return (
    <span className="font-mono text-[12px] tabular-nums text-fg-muted">
      {player.testsPassed}
      <span className="text-fg-subtle">/{player.testsTotal}</span>
    </span>
  );
}

/** Compact live standings bar shown under the header while racing. */
export function StandingsStrip({
  room,
  racing,
}: {
  room: RoomSnapshot;
  racing: number;
}) {
  return (
    <section
      aria-label="Live standings"
      className="flex h-11 flex-none items-center gap-3 px-3"
    >
      <h2 className="section-label hidden flex-none items-center gap-1.5 sm:flex">
        <Icon.trophy size={13} />
        Standings
      </h2>
      <ol className="flex min-w-0 flex-1 items-center gap-1.5 overflow-x-auto py-1 [scrollbar-width:none]">
        {room.rankings.map((player) => {
          const me = player.name === room.me.name;
          return (
            <li
              key={player.name}
              aria-current={me || undefined}
              className={cx(
                "flex h-7 flex-none items-center gap-2 rounded-md border pl-1.5 pr-2 transition-colors",
                me
                  ? "border-accent/35 bg-accent/[0.07]"
                  : "border-line bg-surface",
                (player.resigned || player.away) && "opacity-60",
              )}
            >
              <span
                className={cx(
                  "w-4 text-center font-mono text-[11px] tabular-nums",
                  player.position === 1 && player.solved ? "text-warn" : "text-fg-subtle",
                )}
              >
                {player.position}
              </span>
              <Avatar name={player.name} size={18} />
              <span className="max-w-[120px] truncate text-[12.5px] font-medium text-fg">
                {player.name}
                {me && <span className="font-normal text-fg-subtle"> (you)</span>}
              </span>
              <Score player={player} />
              <StatusBadges player={player} />
            </li>
          );
        })}
      </ol>
      <p className="hidden flex-none items-center gap-1.5 text-[12px] text-fg-subtle md:flex">
        <span className="font-mono tabular-nums text-fg-muted">{racing}</span>
        of {room.rankings.length} still racing
      </p>
    </section>
  );
}

/** Full results table for the finished-round view. */
export function ResultsTable({
  room,
  onReview,
}: {
  room: RoomSnapshot;
  onReview: (name: string, code: string) => void;
}) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full min-w-[520px] text-left text-[13px]">
        <thead>
          <tr className="border-b border-line text-[12px] text-fg-subtle">
            <th scope="col" className="w-12 py-2.5 pl-4 font-medium">#</th>
            <th scope="col" className="py-2.5 font-medium">Player</th>
            <th scope="col" className="py-2.5 font-medium">Result</th>
            <th scope="col" className="py-2.5 font-medium">Tests</th>
            <th scope="col" className="py-2.5 pr-4 text-right font-medium">
              <span className="sr-only">Code</span>
            </th>
          </tr>
        </thead>
        <tbody>
          {room.rankings.map((player) => {
            const me = player.name === room.me.name;
            const winner = player.position === 1 && player.solved;
            return (
              <tr
                key={player.name}
                className={cx(
                  "border-b border-line transition-colors last:border-b-0 hover:bg-white/[0.02]",
                  me && "bg-accent/[0.04]",
                )}
              >
                <td className="py-2.5 pl-4">
                  {winner ? (
                    <span className="flex size-6 items-center justify-center rounded-md border border-warn/30 bg-warn/10 text-warn">
                      <Icon.trophy size={13} />
                    </span>
                  ) : (
                    <span className="flex size-6 items-center justify-center font-mono text-[12px] tabular-nums text-fg-subtle">
                      {player.position}
                    </span>
                  )}
                </td>
                <td className="py-2.5">
                  <span className="flex items-center gap-2.5">
                    <Avatar name={player.name} size={24} />
                    <span className="truncate font-medium text-fg">{player.name}</span>
                    {me && <span className="pill">You</span>}
                    {player.name === room.host && <span className="pill pill-accent">Host</span>}
                  </span>
                </td>
                <td className="py-2.5">
                  <span className="flex flex-wrap items-center gap-1.5">
                    {player.solved ? (
                      <span className="font-mono tabular-nums text-ok">
                        {player.charCount} chars
                      </span>
                    ) : (
                      <span className="text-fg-subtle">Unsolved</span>
                    )}
                    <StatusBadges player={player} />
                  </span>
                </td>
                <td className="py-2.5 font-mono tabular-nums text-fg-muted">
                  {player.testsPassed}
                  <span className="text-fg-subtle"> / {player.testsTotal}</span>
                </td>
                <td className="py-2.5 pr-4 text-right">
                  {player.code !== null && (
                    <button
                      type="button"
                      className="btn btn-ghost btn-sm"
                      onClick={() => onReview(player.name, player.code ?? "")}
                      aria-label={`View ${player.name}'s code`}
                    >
                      <Icon.eye size={14} />
                      View code
                    </button>
                  )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
