import { motion } from 'framer-motion';

export default function Scoreboard({ rankings }) {
  return (
    <div className="flex gap-2 px-4 py-2 bg-surface border-t border-white/[0.06] overflow-x-auto shrink-0">
      {rankings.map((r) => {
        const locked = r.locked_at !== null;
        const statusText = r.solved
          ? `${r.char_count} ch${locked ? ' \u{1f512}' : ''}`
          : r.tests_passed > 0
            ? `${r.tests_passed}/${r.tests_total}`
            : 'pending';

        return (
          <motion.div
            key={r.name}
            layout
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.2 }}
            className={`flex items-center gap-2 px-3 py-1.5 rounded bg-elevated border font-heading text-xs whitespace-nowrap transition-all ${
              r.solved ? 'border-success/30' : 'border-white/[0.06]'
            }`}
          >
            <span className="font-display text-[0.65rem] font-bold text-secondary">
              #{r.position}
            </span>
            <span className="font-semibold text-txt">
              {r.name}
            </span>
            <span className={`text-[0.7rem] ${r.solved ? 'text-success font-bold' : 'text-txt-dim'}`}>
              {statusText}
            </span>
          </motion.div>
        );
      })}
    </div>
  );
}
