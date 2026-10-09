import type { HTMLAttributes, ReactNode } from "react";

export function Box({
  title,
  right,
  double = false,
  className = "",
  children,
  ...rest
}: {
  title?: ReactNode;
  right?: ReactNode;
  double?: boolean;
  className?: string;
  children: ReactNode;
} & Omit<HTMLAttributes<HTMLElement>, "title">) {
  return (
    <section
      className={`box ${double ? "box-double" : ""} ${className}`}
      {...rest}
    >
      {title && (
        <div className="box-legend">
          {typeof title === "string" ? (
            <span className="min-w-0 truncate">{title}</span>
          ) : (
            title
          )}
        </div>
      )}
      {right && <div className="box-legend box-legend-right">{right}</div>}
      {children}
    </section>
  );
}

export function Blocks({
  value,
  total,
  width = 10,
  className = "",
}: {
  value: number;
  total: number;
  width?: number;
  className?: string;
}) {
  const filled = total > 0 ? Math.round((value / total) * width) : 0;
  const complete = total > 0 && value >= total;
  return (
    <span
      role="img"
      aria-label={`${value} of ${total} tests passed`}
      className={`whitespace-pre tracking-[-0.05em] ${className}`}
    >
      <span className={complete ? "text-phos glow-phos" : "text-amber"}>
        {"█".repeat(filled)}
      </span>
      <span className="text-ink-faint/80">{"░".repeat(width - filled)}</span>
    </span>
  );
}

export function DifficultyTag({ difficulty }: { difficulty: string | null }) {
  const tone =
    difficulty === "Easy"
      ? "text-phos border-phos-lo"
      : difficulty === "Hard"
        ? "text-alarm border-alarm-lo"
        : difficulty === "Medium"
          ? "text-ember border-[#7a4a1f]"
          : "text-ink-dim border-line-hi";
  return (
    <span
      className={`inline-block border px-1.5 text-[0.625rem] font-semibold uppercase leading-[1.5] tracking-[0.14em] ${tone}`}
    >
      {difficulty ?? "Any"}
    </span>
  );
}

export function Tag({
  tone,
  children,
}: {
  tone: "amber" | "phos" | "alarm" | "dim";
  children: ReactNode;
}) {
  const tones = {
    amber: "bg-amber text-crt-0",
    phos: "bg-phos text-crt-0",
    alarm: "bg-alarm text-crt-0",
    dim: "bg-crt-3 text-ink-dim",
  };
  return (
    <span
      className={`inline-block px-1 text-[0.5625rem] font-bold uppercase leading-[1.5] tracking-[0.12em] ${tones[tone]}`}
    >
      {children}
    </span>
  );
}

export function Prompt({
  symbol = "$",
  children,
  className = "",
}: {
  symbol?: string;
  children: ReactNode;
  className?: string;
}) {
  return (
    <span className={className}>
      <span aria-hidden="true" className="text-amber-lo">
        {symbol}{" "}
      </span>
      {children}
    </span>
  );
}
