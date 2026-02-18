import { useGame } from '../context/GameContext';

export default function OutputPanel() {
  const { lastResult } = useGame();

  if (!lastResult) return null;

  const lines = [];
  lines.push(`Tests: ${lastResult.passed}/${lastResult.total} passed`);
  if (lastResult.error) lines.push(`Error: ${lastResult.error}`);
  if (lastResult.stdout) lines.push(`\nStdout:\n${lastResult.stdout}`);
  if (lastResult.stderr) lines.push(`\nStderr:\n${lastResult.stderr}`);

  return (
    <div className="h-full flex flex-col bg-[#0d0b09] border-l border-white/[0.06]">
      <div className="px-4 py-2 font-heading font-bold text-[0.7rem] uppercase tracking-[1.5px] text-warning border-b border-white/[0.06] shrink-0">
        Output
      </div>
      <div className="flex-1 overflow-auto p-4 min-h-0">
        <pre className="font-mono text-[0.82rem] text-warning whitespace-pre-wrap break-all leading-relaxed m-0">
          {lines.join('\n')}
        </pre>
      </div>
    </div>
  );
}
