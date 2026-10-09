import type { ReactNode } from "react";
import type { Submission } from "../api";
import type { Ranking } from "../hooks/useRoom";
import { Blocks } from "./crt";

function Row({ label, children }: { label: string; children: ReactNode }) {
  return (
    <>
      <dt className="text-[0.6875rem] tracking-[0.12em] text-ink-faint uppercase">
        {label}
      </dt>
      <dd className="min-w-0">{children}</dd>
    </>
  );
}

function Output({
  label,
  tone = "text-ink",
  children,
}: {
  label: string;
  tone?: string;
  children: string;
}) {
  return (
    <div className="flex flex-col gap-1.5">
      <p className="rule">{label}</p>
      <pre
        className={`max-h-48 overflow-auto bg-crt-0 px-3 py-2 text-xs leading-relaxed whitespace-pre-wrap break-words ${tone}`}
      >
        {children}
      </pre>
    </div>
  );
}

export function SubmissionResults({
  result,
  pending,
}: {
  result: Submission | null;
  pending: boolean;
}) {
  if (pending)
    return (
      <p className="text-sm text-amber" role="status">
        <span aria-hidden="true" className="text-amber-lo">
          &gt;{" "}
        </span>
        running test suite
        <span className="cursor-block" />
      </p>
    );
  if (!result)
    return (
      <div className="flex flex-col gap-1.5 text-sm">
        <p className="text-ink-dim">
          <span aria-hidden="true" className="text-amber-lo">
            ${" "}
          </span>
          awaiting first submission
          <span className="cursor-block" />
        </p>
        <p className="text-xs text-ink-faint">
          Press Ctrl/Cmd + Enter or [ SUBMIT ] to run your code against the
          hidden tests.
        </p>
      </div>
    );

  return (
    <div className="flex flex-col gap-4 text-sm" role="status">
      <div className="flex flex-wrap items-baseline gap-x-4 gap-y-1">
        <p
          className={`font-display text-[1.75rem] leading-none tracking-[0.06em] ${result.solved ? "text-phos glow-phos" : "text-alarm glow-alarm"}`}
        >
          {result.solved
            ? "✔ ACCEPTED"
            : result.firstFailure || !result.error
              ? "✘ REJECTED"
              : "✘ ERROR"}
        </p>
        <p className="text-xs text-ink-dim">
          {result.solved
            ? "all tests passed — lock it in or keep golfing"
            : `${result.total - result.passed} test${result.total - result.passed === 1 ? "" : "s"} failing`}
        </p>
      </div>
      <dl className="grid grid-cols-[6.5rem_1fr] items-baseline gap-x-3 gap-y-1">
        <Row label="tests">
          <Blocks value={result.passed} total={result.total} width={20} />
          <span className="ml-2 tabular-nums text-ink">
            {result.passed}/{result.total}
          </span>
        </Row>
        <Row label="chars">
          <span className="tabular-nums text-amber-hi">{result.charCount}</span>
        </Row>
        <Row label="runtime">
          <span className="tabular-nums text-ink">
            {Math.round(result.timeMs)} ms
          </span>
        </Row>
      </dl>
      {result.error && (
        <Output label="error" tone="text-alarm">
          {result.error}
        </Output>
      )}
      {result.firstFailure && (
        <div className="flex flex-col gap-1.5">
          <p className="rule">first failing test</p>
          <dl className="grid grid-cols-[6.5rem_1fr] gap-x-3 gap-y-1 bg-crt-0 px-3 py-2 font-mono text-xs leading-relaxed">
            <Row label="input">
              <code className="block max-h-28 overflow-y-auto break-words whitespace-pre-wrap text-ink">
                {result.firstFailure.input}
              </code>
            </Row>
            <Row label="expected">
              <code className="break-words whitespace-pre-wrap text-phos">
                {result.firstFailure.expected}
              </code>
            </Row>
            <Row label="received">
              <code className="break-words whitespace-pre-wrap text-alarm">
                {result.firstFailure.actual}
              </code>
            </Row>
          </dl>
        </div>
      )}
      {result.stdout && <Output label="stdout">{result.stdout}</Output>}
      {result.stderr && (
        <Output label="stderr" tone="text-alarm">
          {result.stderr}
        </Output>
      )}
    </div>
  );
}

export function ReviewSummary({
  name,
  player,
  chars,
}: {
  name: string;
  player: Ranking | undefined;
  chars: number;
}) {
  return (
    <div className="flex flex-col gap-3 text-sm">
      <p className="text-ink-dim">
        <span aria-hidden="true" className="text-amber-lo">
          ${" "}
        </span>
        cat ~{name}/solution.py
        <span className="ml-2 text-ink-faint">(read-only)</span>
      </p>
      <dl className="grid grid-cols-[6.5rem_1fr] items-baseline gap-x-3 gap-y-1">
        <Row label="status">
          <span
            className={
              player?.solved
                ? "text-phos"
                : player?.resigned
                  ? "text-alarm"
                  : "text-ink-dim"
            }
          >
            {player?.solved
              ? "SOLVED"
              : player?.resigned
                ? "RESIGNED"
                : "UNSOLVED"}
          </span>
        </Row>
        {player && (
          <Row label="tests">
            <Blocks value={player.testsPassed} total={player.testsTotal} width={20} />
            <span className="ml-2 tabular-nums">
              {player.testsPassed}/{player.testsTotal}
            </span>
          </Row>
        )}
        <Row label="chars">
          <span className="tabular-nums text-amber-hi">{chars}</span>
        </Row>
      </dl>
    </div>
  );
}
