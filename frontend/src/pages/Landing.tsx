import { useEffect, useRef, useState, type FormEvent, type ReactNode } from "react";
import { useNavigate } from "react-router-dom";
import { motion, useReducedMotion } from "framer-motion";
import { api, errorMessage, saveSession, type RouterInputs } from "../api";
import { Box } from "../components/crt";

type Difficulty = RouterInputs["createRoom"]["difficulty"];

const DIFFICULTIES: { value: Difficulty; label: string; tone: string }[] = [
  { value: null, label: "Any", tone: "text-amber-hi glow" },
  { value: "Easy", label: "Easy", tone: "text-phos glow-phos" },
  { value: "Medium", label: "Medium", tone: "text-ember" },
  { value: "Hard", label: "Hard", tone: "text-alarm glow-alarm" },
];

const BOOT: [string, string][] = [
  ["PHOSPHOR/OS 8.6 — LEETRACE SYSTEMS", ""],
  ...[
    "MEMORY CHECK 640K",
    "PYTHON 3 INTERPRETER",
    "HIDDEN TEST JUDGE",
    "MULTIPLAYER UPLINK",
  ].map((text): [string, string] => [`${text} `.padEnd(34, "."), " OK"]),
];
const BOOT_LENGTH = BOOT.reduce((sum, [text, ok]) => sum + text.length + ok.length, 0);

const GLYPHS: Record<string, string[]> = {
  L: ["██╗     ", "██║     ", "██║     ", "██║     ", "███████╗", "╚══════╝"],
  E: ["███████╗", "██╔════╝", "█████╗  ", "██╔══╝  ", "███████╗", "╚══════╝"],
  T: ["████████╗", "╚══██╔══╝", "   ██║   ", "   ██║   ", "   ██║   ", "   ╚═╝   "],
  R: ["██████╗ ", "██╔══██╗", "██████╔╝", "██╔══██╗", "██║  ██║", "╚═╝  ╚═╝"],
  A: [" █████╗ ", "██╔══██╗", "███████║", "██╔══██║", "██║  ██║", "╚═╝  ╚═╝"],
  C: [" ██████╗", "██╔════╝", "██║     ", "██║     ", "╚██████╗", " ╚═════╝"],
};
const LOGO = Array.from({ length: 6 }, (_, row) =>
  [..."LEETRACE"].map((letter) => GLYPHS[letter]?.[row] ?? "").join(""),
).join("\n");

function useBoot() {
  const reduced = useReducedMotion();
  const [typed, setTyped] = useState(0);
  const done = reduced || typed >= BOOT_LENGTH;
  useEffect(() => {
    if (done) return;
    const skip = () => setTyped(BOOT_LENGTH);
    const timer = window.setInterval(
      () => setTyped((value) => Math.min(BOOT_LENGTH, value + 4)),
      14,
    );
    window.addEventListener("keydown", skip);
    window.addEventListener("pointerdown", skip);
    return () => {
      window.clearInterval(timer);
      window.removeEventListener("keydown", skip);
      window.removeEventListener("pointerdown", skip);
    };
  }, [done]);
  return { typed: done ? BOOT_LENGTH : typed, done };
}

function BootLog({ typed, done }: { typed: number; done: boolean }) {
  let budget = typed;
  return (
    <pre
      aria-hidden="true"
      className="min-h-[6.6em] text-[0.6875rem] leading-[1.6] text-ink-faint"
    >
      {BOOT.map(([text, ok], index) => {
        const shown = text.slice(0, Math.max(0, budget));
        budget -= text.length;
        const okShown = ok.slice(0, Math.max(0, budget));
        budget -= ok.length;
        if (!shown) return null;
        return (
          <span key={index} className="block">
            {index === 0 ? <span className="text-ink-dim">{shown}</span> : shown}
            {okShown && <span className="text-phos">{okShown}</span>}
          </span>
        );
      })}
      <span className="block text-amber">
        {done ? "READY." : ""}
        <span className="cursor-block" />
      </span>
    </pre>
  );
}

function FieldRow({
  label,
  htmlFor,
  id,
  children,
}: {
  label: string;
  htmlFor?: string;
  id?: string;
  children: ReactNode;
}) {
  const text = (
    <>
      <span aria-hidden="true" className="text-amber-lo">
        ${" "}
      </span>
      {label}
    </>
  );
  return (
    <div className="grid items-center gap-x-4 gap-y-1.5 sm:grid-cols-[9.5rem_1fr]">
      {htmlFor ? (
        <label htmlFor={htmlFor} className="text-sm text-ink-dim">
          {text}
        </label>
      ) : (
        <span id={id} className="text-sm text-ink-dim">
          {text}
        </span>
      )}
      <div className="flex min-w-0 flex-wrap items-center gap-2">{children}</div>
    </div>
  );
}

function Stepper({
  id,
  label,
  value,
  min,
  max,
  step,
  unit,
  onChange,
}: {
  id: string;
  label: string;
  value: number;
  min: number;
  max: number;
  step: number;
  unit: string;
  onChange: (value: number) => void;
}) {
  const set = (next: number) => onChange(Math.min(max, Math.max(min, next)));
  return (
    <>
      <button
        type="button"
        className="btn px-1.5"
        aria-label={`Decrease ${label.toLowerCase()}`}
        disabled={value <= min}
        onClick={() => set(value - step)}
      >
        -
      </button>
      <input
        id={id}
        aria-label={label}
        type="number"
        min={min}
        max={max}
        step={step}
        value={value}
        onChange={(event) => onChange(event.target.valueAsNumber || 1)}
        onBlur={() => set(value)}
        className="field w-[5ch] text-center tabular-nums"
      />
      <button
        type="button"
        className="btn px-1.5"
        aria-label={`Increase ${label.toLowerCase()}`}
        disabled={value >= max}
        onClick={() => set(value + step)}
      >
        +
      </button>
      <span className="text-xs text-ink-faint">{unit}</span>
    </>
  );
}

export default function Landing() {
  const navigate = useNavigate();
  const { typed, done } = useBoot();
  const nameInput = useRef<HTMLInputElement>(null);
  const [tab, setTab] = useState<"create" | "join">("create");
  const [name, setName] = useState("");
  const [difficulty, setDifficulty] = useState<Difficulty>(null);
  const [timeLimit, setTimeLimit] = useState(5);
  const [rounds, setRounds] = useState(1);
  const [roomCode, setRoomCode] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (done) nameInput.current?.focus();
  }, [done]);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!name.trim()) {
      setError("Enter your name.");
      nameInput.current?.focus();
      return;
    }
    setError("");
    setLoading(true);
    try {
      const session =
        tab === "create"
          ? await api.createRoom.mutate({
              name: name.trim(),
              difficulty,
              timeLimit: Math.round(timeLimit * 60),
              rounds,
            })
          : await api.joinRoom.mutate({
              roomId: roomCode.trim().toUpperCase(),
              name: name.trim(),
            });
      saveSession(session);
      navigate(`/room?id=${session.roomId}`);
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="h-dvh overflow-y-auto">
      <main className="mx-auto flex min-h-full w-full max-w-[860px] flex-col justify-center gap-5 px-4 py-8">
        <Box
          double
          title="[ tty0 :: guest@leetrace ]"
          right={<span className="font-normal text-ink-faint">80×24</span>}
          className="power-on"
        >
          <div className="flex flex-col gap-5 px-6 pt-6 pb-6 sm:px-8">
            <BootLog typed={typed} done={done} />
            <motion.div
              initial={false}
              animate={{ opacity: done ? 1 : 0.08 }}
              transition={{ duration: 0.3 }}
              className="flex flex-col gap-3"
            >
              <h1 className="sr-only">LeetRace</h1>
              <pre
                aria-hidden="true"
                className="overflow-hidden text-[clamp(0.42rem,1.45vw,0.8125rem)] leading-[1.02] text-amber glow"
              >
                {LOGO}
              </pre>
              <p className="font-display text-[1.45rem] leading-none tracking-[0.08em] text-amber-hi">
                MULTIPLAYER PYTHON SPEEDRUNS
                <span className="text-amber-lo"> // </span>
                FEWEST CHARS WINS
              </p>
            </motion.div>
          </div>

          <div className="border-t border-dashed border-line-hi px-6 pt-5 pb-6 sm:px-8">
            <div role="group" aria-label="Mode" className="mb-5 flex flex-wrap gap-2">
              {(["create", "join"] as const).map((mode) => (
                <button
                  key={mode}
                  type="button"
                  className="btn"
                  aria-pressed={tab === mode}
                  onClick={() => {
                    setTab(mode);
                    setError("");
                  }}
                >
                  {mode === "create" ? "Create Room" : "Join Room"}
                </button>
              ))}
            </div>

            <form
              key={tab}
              onSubmit={(event) => void handleSubmit(event)}
              className="flex flex-col gap-4"
            >
              <FieldRow label="handle" htmlFor="name">
                <input
                  ref={nameInput}
                  id="name"
                  aria-label="Your name"
                  required
                  type="text"
                  value={name}
                  onChange={(event) => setName(event.target.value)}
                  maxLength={20}
                  placeholder="enter your name"
                  autoComplete="nickname"
                  spellCheck={false}
                  className="field w-full max-w-[22rem]"
                />
              </FieldRow>

              {tab === "create" ? (
                <>
                  <FieldRow label="difficulty" id="difficulty-label">
                    <div
                      role="radiogroup"
                      aria-labelledby="difficulty-label"
                      className="flex flex-wrap gap-x-4 gap-y-1"
                    >
                      {DIFFICULTIES.map((option) => {
                        const checked = difficulty === option.value;
                        return (
                          <label
                            key={option.label}
                            className="cursor-pointer text-sm tracking-[0.08em] uppercase"
                          >
                            <input
                              type="radio"
                              name="difficulty"
                              className="peer sr-only"
                              checked={checked}
                              onChange={() => setDifficulty(option.value)}
                            />
                            <span
                              className={`inline-block px-1 peer-focus-visible:outline peer-focus-visible:outline-1 peer-focus-visible:outline-dashed peer-focus-visible:outline-amber-hi ${checked ? option.tone : "text-ink-faint hover:text-ink"}`}
                            >
                              {checked ? "(•)" : "( )"} {option.label}
                            </span>
                          </label>
                        );
                      })}
                    </div>
                  </FieldRow>
                  <FieldRow label="time_limit" htmlFor="time">
                    <Stepper
                      id="time"
                      label="Time in minutes"
                      value={timeLimit}
                      min={1}
                      max={60}
                      step={0.5}
                      unit="min / round"
                      onChange={setTimeLimit}
                    />
                  </FieldRow>
                  <FieldRow label="rounds" htmlFor="rounds">
                    <Stepper
                      id="rounds"
                      label="Rounds"
                      value={rounds}
                      min={1}
                      max={10}
                      step={1}
                      unit={rounds === 1 ? "round" : "rounds"}
                      onChange={(value) => setRounds(Math.round(value))}
                    />
                  </FieldRow>
                </>
              ) : (
                <FieldRow label="room_code" htmlFor="code">
                  <input
                    id="code"
                    aria-label="Room code"
                    required
                    minLength={6}
                    maxLength={6}
                    type="text"
                    value={roomCode}
                    onChange={(event) =>
                      setRoomCode(event.target.value.toUpperCase().slice(0, 6))
                    }
                    placeholder="XXXXXX"
                    autoComplete="off"
                    spellCheck={false}
                    className="field w-[11ch] font-display text-[1.9rem] leading-none tracking-[0.3em] uppercase"
                  />
                </FieldRow>
              )}

              <div className="mt-2 flex flex-wrap items-center gap-4 sm:pl-[10.5rem]">
                <button type="submit" disabled={loading} className="btn btn-solid btn-lg">
                  {loading
                    ? tab === "create"
                      ? "Creating…"
                      : "Joining…"
                    : tab === "create"
                      ? "Create Room"
                      : "Join Room"}
                  <span className="kbd">⏎</span>
                </button>
                {error && (
                  <p role="alert" className="text-sm text-alarm">
                    <span className="font-bold">!! ERR:</span> {error}
                  </p>
                )}
              </div>
            </form>
          </div>
        </Box>

        <ol className="grid gap-x-6 gap-y-1 px-1 text-xs text-ink-faint sm:grid-cols-3">
          <li>
            <span className="text-amber-lo">01</span> pass every hidden test
          </li>
          <li>
            <span className="text-amber-lo">02</span> fewer characters rank higher
          </li>
          <li>
            <span className="text-amber-lo">03</span> lock your score or keep golfing
          </li>
        </ol>
      </main>
    </div>
  );
}
