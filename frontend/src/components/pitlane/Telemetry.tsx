import type { Submission } from "../../api";

function Block({
  label,
  tone,
  children,
}: {
  label: string;
  tone: string;
  children: string;
}) {
  return (
    <div className="grid grid-cols-[88px_1fr] border-b border-line last:border-b-0">
      <span className={`label px-3 py-2 border-r border-line ${tone}`}>
        {label}
      </span>
      <pre className="px-3 py-2 font-mono text-[13px] whitespace-pre-wrap break-words max-h-40 overflow-y-auto">
        {children}
      </pre>
    </div>
  );
}

/** Submission status, first failing test and captured output. */
export default function Telemetry({ result }: { result: Submission | null }) {
  if (!result)
    return (
      <div className="h-full flex flex-col items-center justify-center gap-2 text-center text-ink-dim">
        <p className="font-display uppercase italic tracking-[0.18em] text-sm">
          No laps set
        </p>
        <p className="text-sm">
          Submit with <span className="kbd">Ctrl</span>{" "}
          <span className="kbd">Enter</span> to see telemetry.
        </p>
      </div>
    );
  const ratio = result.total ? result.passed / result.total : 0;
  return (
    <div className="flex flex-col gap-3">
      <div className="flex flex-wrap items-center gap-x-4 gap-y-1">
        <span
          className={`font-display text-xl font-bold uppercase italic tracking-wide ${result.solved ? "text-sector-green" : "text-sector-yellow"}`}
        >
          {result.solved ? "Clean lap" : "Track limits"}
        </span>
        <span className="font-mono text-sm">
          {result.passed}/{result.total} tests
        </span>
        {result.solved && (
          <span className="font-mono text-sm text-sector-purple">
            {result.charCount} chars
          </span>
        )}
        <span className="font-mono text-xs text-ink-dim ml-auto">
          {Math.round(result.timeMs)} ms
        </span>
      </div>
      <div className="h-1.5 bg-raised overflow-hidden" aria-hidden>
        <div
          className={`h-full ${result.solved ? "bg-sector-green" : "bg-sector-yellow"} transition-[width] duration-500`}
          style={{ width: `${ratio * 100}%` }}
        />
      </div>
      {result.error && (
        <pre className="font-mono text-[13px] text-signal-bright whitespace-pre-wrap break-words border-l-2 border-signal pl-3">
          {result.error}
        </pre>
      )}
      {result.firstFailure && (
        <section className="border border-line bg-carbon/60">
          <p className="label px-3 py-2 border-b border-line text-ink-muted">
            First failing test
          </p>
          <Block label="Input" tone="text-ink-muted">
            {result.firstFailure.input}
          </Block>
          <Block label="Expected" tone="text-sector-green">
            {result.firstFailure.expected}
          </Block>
          <Block label="Received" tone="text-signal-bright">
            {result.firstFailure.actual}
          </Block>
        </section>
      )}
      {(result.stdout || result.stderr) && (
        <section className="border border-line bg-carbon/60">
          {result.stdout && (
            <Block label="Stdout" tone="text-pit-blue">
              {result.stdout}
            </Block>
          )}
          {result.stderr && (
            <Block label="Stderr" tone="text-signal-bright">
              {result.stderr}
            </Block>
          )}
        </section>
      )}
    </div>
  );
}
