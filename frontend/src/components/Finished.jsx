import { motion } from 'framer-motion';

function formatTime(seconds) {
  if (seconds == null) return '—';
  return `${seconds.toFixed(1)}s`;
}

export default function Finished({
  rankings,
  isHost,
  playerName,
  onRestart,
  onViewCode,
  breakRemaining,
  currentRound,
  totalRounds,
  roundOver,
}) {
  if (!rankings || rankings.length === 0) return null;

  const top3 = rankings.slice(0, 3);
  // Podium order: 2nd, 1st, 3rd
  const podiumOrder = top3.length >= 3
    ? [top3[1], top3[0], top3[2]]
    : top3.length === 2
    ? [top3[1], top3[0]]
    : [top3[0]];

  const barClasses = ['bar-2', 'bar-1', 'bar-3'];
  const barHeights = ['h-[70px]', 'h-[100px]', 'h-[50px]'];
  const barGradients = [
    'bg-gradient-to-b from-silver/12 to-silver/2 border border-silver/20',
    'bg-gradient-to-b from-gold/15 to-gold/3 border border-gold/25',
    'bg-gradient-to-b from-bronze/12 to-bronze/2 border border-bronze/20',
  ];
  const posColors = ['text-silver', 'text-gold', 'text-bronze'];
  const posShadows = [
    '0 0 12px rgba(192,192,192,0.3)',
    '0 0 14px rgba(255,215,0,0.4)',
    '0 0 12px rgba(205,127,50,0.3)',
  ];

  // For 2-player: index 0=2nd, 1=1st. For 1-player: 0=1st
  const podiumStartIdx = top3.length >= 3 ? 0 : top3.length === 2 ? 0 : 1;

  return (
    <div className="flex-1 flex flex-col items-center px-5 py-10 overflow-y-auto">
      {/* Title */}
      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="font-display text-[0.82rem] font-semibold tracking-[0.2em] uppercase text-dim mb-2"
      >
        {roundOver ? 'Round Over' : 'Game Over'}
      </motion.p>

      {totalRounds > 1 && (
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.1 }}
          className="font-mono text-[0.78rem] text-muted mb-8"
        >
          Round {currentRound} of {totalRounds}
        </motion.p>
      )}

      {/* Break countdown */}
      {roundOver && breakRemaining > 0 && (
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          className="text-center mb-8"
        >
          <p className="font-display text-[0.72rem] font-semibold tracking-[0.12em] uppercase text-dim mb-1">
            Next round in
          </p>
          <p
            className="font-mono text-[2rem] font-bold text-primary"
            style={{ textShadow: '0 0 20px rgba(0,229,199,0.3)' }}
          >
            {breakRemaining}
          </p>
        </motion.div>
      )}

      {/* Podium */}
      <motion.div
        initial={{ opacity: 0, y: 16 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.15, duration: 0.5 }}
        className="flex items-end gap-2 mb-9"
      >
        {podiumOrder.map((r, idx) => {
          const actualIdx = top3.length < 3 ? idx + podiumStartIdx : idx;
          return (
            <motion.div
              key={r.name}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 + idx * 0.12, duration: 0.45 }}
              className="flex flex-col items-center w-[130px]"
            >
              <span
                className={`font-display text-[1.5rem] font-bold mb-1.5 ${posColors[actualIdx]}`}
                style={{ textShadow: posShadows[actualIdx] }}
              >
                {r.position}
              </span>
              <span className={`font-display text-[0.92rem] font-semibold text-center break-all mb-1 ${r.name === playerName ? 'text-primary' : 'text-light'}`}>
                {r.name}
              </span>
              <span className="font-mono text-[0.72rem] text-muted mb-2.5">
                {r.solved ? `${r.char_count} chars` : `${r.tests_passed}/${r.tests_total}`}
              </span>
              <div
                className={`w-full rounded-t ${barGradients[actualIdx]} ${barHeights[actualIdx]}`}
              />
            </motion.div>
          );
        })}
      </motion.div>

      {/* Rankings Table */}
      <motion.table
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5, duration: 0.4 }}
        className="w-full max-w-[700px] border-separate"
        style={{ borderSpacing: '0 4px' }}
      >
        <thead>
          <tr>
            <th className="font-display text-[0.65rem] font-semibold tracking-[0.15em] uppercase text-dim px-3.5 py-2 text-center w-[50px]">#</th>
            <th className="font-display text-[0.65rem] font-semibold tracking-[0.15em] uppercase text-dim px-3.5 py-2 text-left">Player</th>
            <th className="font-display text-[0.65rem] font-semibold tracking-[0.15em] uppercase text-dim px-3.5 py-2 text-left">Status</th>
            <th className="font-display text-[0.65rem] font-semibold tracking-[0.15em] uppercase text-dim px-3.5 py-2 text-left">Tests</th>
            <th className="font-display text-[0.65rem] font-semibold tracking-[0.15em] uppercase text-dim px-3.5 py-2 text-left">Time</th>
          </tr>
        </thead>
        <tbody>
          {rankings.map((r, i) => {
            const posClass = r.position === 1 ? 'text-gold' : r.position === 2 ? 'text-silver' : r.position === 3 ? 'text-bronze' : 'text-dim';
            return (
              <motion.tr
                key={r.name}
                initial={{ opacity: 0, x: -12 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.55 + i * 0.06, duration: 0.3 }}
              >
                <td className={`bg-elevated border-t border-b border-l border-brd rounded-l px-3.5 py-3 text-center font-mono font-bold ${posClass}`}>
                  {r.position}
                </td>
                <td className="bg-elevated border-t border-b border-brd px-3.5 py-3">
                  <span className={`font-display font-semibold tracking-[0.02em] ${r.name === playerName ? 'text-primary' : 'text-light'}`}>
                    {r.name}
                  </span>
                </td>
                <td className="bg-elevated border-t border-b border-brd px-3.5 py-3">
                  {r.solved ? (
                    <span className="text-ok font-semibold font-mono text-[0.82rem]">
                      {r.char_count} chars
                      {r.locked_at != null && <span className="text-warn ml-1.5 text-[0.72rem]">(locked)</span>}
                    </span>
                  ) : r.error ? (
                    <span className="text-err text-[0.78rem]">Error</span>
                  ) : (
                    <span className="text-dim font-mono text-[0.82rem]">Unsolved</span>
                  )}
                </td>
                <td className="bg-elevated border-t border-b border-brd px-3.5 py-3 font-mono text-[0.82rem] text-muted">
                  {r.tests_passed}/{r.tests_total}
                </td>
                <td className="bg-elevated border-t border-b border-r border-brd rounded-r px-3.5 py-3 font-mono text-[0.82rem] text-muted">
                  {r.submit_time > 0 ? formatTime(r.submit_time) : '—'}
                </td>
              </motion.tr>
            );
          })}
        </tbody>
      </motion.table>

      {/* Actions */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.7, duration: 0.3 }}
        className="flex gap-3 flex-wrap justify-center mt-4"
      >
        {!roundOver && isHost && (
          <button
            onClick={onRestart}
            className="inline-flex items-center justify-center gap-2 px-7 py-3 bg-primary text-inverse font-display text-[0.85rem] font-semibold tracking-[0.1em] uppercase rounded-lg transition-all duration-150 hover:bg-primary-bright hover:shadow-glow hover:-translate-y-px"
          >
            Play Again
          </button>
        )}
        <button
          onClick={onViewCode}
          className="inline-flex items-center justify-center gap-2 px-7 py-3 bg-transparent text-primary border border-primary/25 font-display text-[0.85rem] font-semibold tracking-[0.1em] uppercase rounded-lg transition-all duration-150 hover:bg-primary/8 hover:border-primary hover:shadow-glow-sm"
        >
          View Code
        </button>
      </motion.div>
    </div>
  );
}
