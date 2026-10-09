import { motion } from "framer-motion";
import type { RoomSnapshot } from "../api";
import type { Ranking } from "../hooks/useRoom";
import { Blocks, Tag } from "./crt";

const pad = (value: number) => String(value).padStart(2, "0");

function Badges({ player }: { player: Ranking }) {
  return (
    <>
      {player.lockedAt !== null && <Tag tone="phos">Locked</Tag>}
      {player.resigned && <Tag tone="alarm">Resigned</Tag>}
      {player.away && <Tag tone="dim">Away</Tag>}
    </>
  );
}

export function StandingsStrip({ room }: { room: RoomSnapshot }) {
  return (
    <section
      aria-label="Live standings"
      className="flex h-8 flex-none items-stretch border-b border-line bg-crt-1 text-xs"
    >
      <h2 className="flex flex-none items-center gap-1.5 border-r border-line bg-crt-2 px-3 text-[0.6875rem] tracking-[0.12em] text-amber uppercase">
        <span aria-hidden="true" className="text-amber-lo">
          $
        </span>
        ps --race
      </h2>
      <ol className="flex min-w-0 flex-1 items-stretch overflow-x-auto">
        {room.rankings.map((player) => {
          const mine = player.name === room.me.name;
          return (
            <li
              key={player.name}
              className={`flex flex-none items-center gap-2 border-r border-line px-3 whitespace-nowrap ${mine ? "bg-amber/[0.07]" : ""}`}
            >
              <span className="text-ink-faint tabular-nums">
                {pad(player.position)}
              </span>
              <span
                className={`max-w-[12ch] truncate ${mine ? "font-semibold text-amber-hi glow" : "text-ink"} ${player.resigned ? "line-through decoration-alarm-lo" : ""}`}
              >
                {player.name}
              </span>
              <Blocks
                value={player.testsPassed}
                total={player.testsTotal}
                width={8}
              />
              <span
                className={`tabular-nums ${player.solved ? "text-phos" : "text-ink-dim"}`}
              >
                {player.solved
                  ? `${player.charCount}ch`
                  : `${player.testsPassed}/${player.testsTotal}`}
              </span>
              <Badges player={player} />
            </li>
          );
        })}
      </ol>
    </section>
  );
}

export function ResultsTable({
  room,
  onReview,
}: {
  room: RoomSnapshot;
  onReview: (name: string, code: string) => void;
}) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full min-w-[620px] border-collapse text-left text-[0.8125rem]">
        <thead>
          <tr className="bg-amber text-crt-0 text-[0.6875rem] tracking-[0.12em] uppercase">
            <th scope="col" className="px-3 py-1 font-bold">
              Pos
            </th>
            <th scope="col" className="px-3 py-1 font-bold">
              User
            </th>
            <th scope="col" className="px-3 py-1 font-bold">
              State
            </th>
            <th scope="col" className="px-3 py-1 font-bold">
              Tests
            </th>
            <th scope="col" className="px-3 py-1 text-right font-bold">
              Chars
            </th>
            <th scope="col" className="px-3 py-1 text-right font-bold">
              Code
            </th>
          </tr>
        </thead>
        <tbody>
          {room.rankings.map((player, index) => {
            const mine = player.name === room.me.name;
            const winner = player.position === 1 && player.solved;
            return (
              <motion.tr
                key={player.name}
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.08 * index, duration: 0.01 }}
                className={`border-b border-dashed border-line ${mine ? "bg-amber/[0.06]" : ""}`}
              >
                <td className="px-3 py-2 tabular-nums">
                  <span className={winner ? "text-amber-hi glow" : "text-ink-dim"}>
                    {winner ? "▶ " : "  "}
                    {pad(player.position)}
                  </span>
                </td>
                <td className="px-3 py-2">
                  <span
                    className={
                      mine ? "font-semibold text-amber-hi" : "text-ink"
                    }
                  >
                    {player.name}
                  </span>
                  {mine && (
                    <span className="ml-2 text-[0.625rem] text-ink-faint uppercase">
                      (you)
                    </span>
                  )}
                </td>
                <td className="px-3 py-2">
                  <span className="flex flex-wrap items-center gap-1.5">
                    <span
                      className={`text-[0.6875rem] tracking-[0.1em] uppercase ${player.solved ? "text-phos glow-phos" : player.resigned ? "text-alarm" : "text-ink-faint"}`}
                    >
                      {player.solved
                        ? "Solved"
                        : player.resigned
                          ? "Resigned"
                          : "Unsolved"}
                    </span>
                    {player.lockedAt !== null && <Tag tone="phos">Locked</Tag>}
                    {player.away && <Tag tone="dim">Away</Tag>}
                  </span>
                </td>
                <td className="px-3 py-2 whitespace-nowrap">
                  <Blocks value={player.testsPassed} total={player.testsTotal} />
                  <span className="ml-2 text-ink-dim tabular-nums">
                    {player.testsPassed}/{player.testsTotal}
                  </span>
                </td>
                <td className="px-3 py-2 text-right tabular-nums">
                  {player.solved ? (
                    <span className="text-amber-hi">{player.charCount}</span>
                  ) : (
                    <span className="text-ink-faint">—</span>
                  )}
                </td>
                <td className="px-3 py-1 text-right">
                  {player.code !== null ? (
                    <button
                      className="btn"
                      aria-label={`View ${player.name}'s code`}
                      onClick={() => onReview(player.name, player.code ?? "")}
                    >
                      View
                    </button>
                  ) : (
                    <span className="text-[0.6875rem] text-ink-faint">n/a</span>
                  )}
                </td>
              </motion.tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
