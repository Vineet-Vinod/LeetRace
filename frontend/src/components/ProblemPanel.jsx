import { useGame } from '../context/GameContext';

export default function ProblemPanel() {
  const { problem } = useGame();

  if (!problem) return null;

  const diffClass = {
    Easy: 'bg-success/10 text-success border border-success/20',
    Medium: 'bg-warning/10 text-warning border border-warning/20',
    Hard: 'bg-danger/10 text-danger border border-danger/20',
  }[problem.difficulty] || '';

  return (
    <div className="h-full overflow-y-auto p-6 bg-base flex flex-col">
      <h2 className="font-heading text-lg font-bold text-txt mb-1">
        {problem.title}
      </h2>

      <span className={`inline-block self-start font-heading text-[0.65rem] font-bold px-2 py-0.5 rounded-sm uppercase tracking-wider mb-4 ${diffClass}`}>
        {problem.difficulty}
      </span>

      <div className="font-mono text-[0.85rem] leading-relaxed whitespace-pre-wrap text-problem-text flex-1 overflow-y-auto min-h-[50px]">
        {problem.description}
      </div>
    </div>
  );
}
