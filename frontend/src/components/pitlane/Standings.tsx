import { motion } from "framer-motion";
import type { RoomSnapshot } from "../../api";
import type { Ranking } from "../../hooks/useRoom";
import { driverCode, livery } from "./livery";

function Status({ player }: { player: Ranking }) {
  if (player.away)
    return <span className="text-pit-blue">Away</span>;
  if (player.resigned) return <span className="text-ink-dim">Resigned</span>;
  if (player.lockedAt !== null)
    return <span className="text-sector-yellow">Locked</span>;
  return null;
}

function result(player: Ranking) {
  if (player.solved) return `${player.charCount} ch`;
  return `${player.testsPassed}/${player.testsTotal}`;
}

/** Broadcast-style live ticker shown above the panes during a round. */
export function TimingStrip({ room }: { room: RoomSnapshot }) {
  const pole = room.rankings[0]?.solved ? room.rankings[0].name : null;
  return (
    <div
      className="flex items-stretch h-9 bg-pit border-b border-line overflow-x-auto"
      aria-label="Live standings"
    >
      <span className="plate shrink-0 flex items-center px-4 -ml-1 bg-signal">
        <span className="font-display text-xs font-bold uppercase tracking-[0.2em] italic">
          Live
        </span>
      </span>
      <ol className="flex items-stretch">
        {room.rankings.map((player) => (
          <motion.li
            layout
            key={player.name}
            className={`flex items-center gap-2.5 pl-3 pr-4 border-r border-line whitespace-nowrap ${player.resigned || player.away ? "opacity-50" : ""}`}
          >
            <span className="font-display font-bold italic text-ink-muted w-4 text-right">
              {player.position}
            </span>
            <span
              className="w-[3px] h-4"
              style={{ background: livery(player.name) }}
            />
            <span
              className={`font-display font-semibold tracking-[0.12em] ${player.name === room.me.name ? "text-ink" : "text-ink-muted"}`}
              title={player.name}
            >
              {driverCode(player.name)}
            </span>
            <span
              className={`font-mono text-xs ${player.name === pole ? "text-sector-purple" : player.solved ? "text-sector-green" : "text-ink-muted"}`}
            >
              {result(player)}
            </span>
            <span className="font-display text-[10px] font-semibold uppercase tracking-[0.16em]">
              <Status player={player} />
            </span>
          </motion.li>
        ))}
      </ol>
    </div>
  );
}

const podium = ["text-gold", "text-silver", "text-bronze"];

/** Full classification after a round, with code review links. */
export function Classification({
  room,
  onReview,
}: {
  room: RoomSnapshot;
  onReview: (name: string, code: string) => void;
}) {
  return (
    <table className="w-full text-left border-separate border-spacing-y-1">
      <thead>
        <tr className="label">
          <th className="px-4 py-2 w-16">Pos</th>
          <th className="px-4 py-2">Driver</th>
          <th className="px-4 py-2">Result</th>
          <th className="px-4 py-2">Tests</th>
          <th className="px-4 py-2">Locked at</th>
          <th className="px-4 py-2 text-right">Code</th>
        </tr>
      </thead>
      <tbody>
        {room.rankings.map((player, index) => (
          <motion.tr
            key={player.name}
            initial={{ opacity: 0, x: -16 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.06, duration: 0.35 }}
            className="bg-panel"
          >
            <td
              className={`px-4 py-3 font-display text-2xl font-extrabold italic ${podium[index] ?? "text-ink-dim"}`}
            >
              {player.position}
            </td>
            <td className="px-4 py-3">
              <span className="flex items-center gap-3">
                <span
                  className="w-1 h-7"
                  style={{ background: livery(player.name) }}
                />
                <span className="font-display text-lg font-semibold tracking-wide">
                  {player.name}
                </span>
                {player.name === room.me.name && (
                  <span className="label text-signal">You</span>
                )}
              </span>
            </td>
            <td className="px-4 py-3 font-mono text-sm">
              {player.solved ? (
                <span
                  className={
                    index === 0 ? "text-sector-purple" : "text-sector-green"
                  }
                >
                  {player.charCount} chars
                </span>
              ) : (
                <span className="text-ink-dim">
                  {player.resigned ? "Resigned" : "Unsolved"}
                </span>
              )}
            </td>
            <td className="px-4 py-3 font-mono text-sm text-ink-muted">
              {player.testsPassed}/{player.testsTotal}
            </td>
            <td className="px-4 py-3 font-mono text-sm text-ink-muted">
              {player.lockedAt === null ? "—" : `${player.lockedAt.toFixed(1)}s`}
            </td>
            <td className="px-4 py-3 text-right">
              {player.code !== null ? (
                <button
                  className="btn btn-ghost h-8 text-xs"
                  onClick={() => onReview(player.name, player.code ?? "")}
                >
                  View
                </button>
              ) : (
                <span className="text-ink-dim">—</span>
              )}
            </td>
          </motion.tr>
        ))}
      </tbody>
    </table>
  );
}
