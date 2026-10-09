import { useState, type FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import { AnimatePresence, MotionConfig, motion } from "framer-motion";
import { api, errorMessage, saveSession, type RouterInputs } from "../api";
import { Icon, Kbd, Spinner, Wordmark, cx, difficultyDot } from "../components/ui";

type Difficulty = RouterInputs["createRoom"]["difficulty"];
type Tab = "create" | "join";

const DIFFICULTIES: { value: Difficulty; label: string }[] = [
  { value: null, label: "Any" },
  { value: "Easy", label: "Easy" },
  { value: "Medium", label: "Medium" },
  { value: "Hard", label: "Hard" },
];

const ease = [0.22, 1, 0.36, 1] as const;

function Stepper({
  id,
  label,
  value,
  onChange,
  min,
  max,
  step,
  suffix,
}: {
  id: string;
  label: string;
  value: number;
  onChange: (value: number) => void;
  min: number;
  max: number;
  step: number;
  suffix?: string;
}) {
  const clamp = (next: number) =>
    Math.min(max, Math.max(min, Math.round(next / step) * step));
  return (
    <div className="flex min-w-0 flex-1 flex-col gap-1.5">
      <label htmlFor={id} className="text-[12.5px] font-medium text-fg-muted">
        {label}
      </label>
      <div className="group flex h-10 items-center rounded-lg border border-line-strong bg-sunken transition-colors hover:border-line-hover focus-within:border-accent focus-within:shadow-[0_0_0_3px_rgb(139_140_248/0.18)]">
        <button
          type="button"
          aria-label={`Decrease ${label.toLowerCase()}`}
          disabled={value <= min}
          onClick={() => onChange(clamp(value - step))}
          className="flex h-full w-9 flex-none items-center justify-center rounded-l-lg text-fg-subtle transition-colors hover:text-fg disabled:opacity-30 disabled:hover:text-fg-subtle"
        >
          <Icon.minus size={14} />
        </button>
        <input
          id={id}
          type="number"
          inputMode="decimal"
          min={min}
          max={max}
          step={step}
          value={value}
          onChange={(event) => onChange(event.target.valueAsNumber || min)}
          onBlur={() => onChange(clamp(value))}
          className="h-full w-full min-w-0 bg-transparent text-center font-mono text-[14px] tabular-nums text-fg outline-none"
        />
        {suffix && (
          <span className="pointer-events-none -ml-1 pr-1 text-[12px] text-fg-subtle">
            {suffix}
          </span>
        )}
        <button
          type="button"
          aria-label={`Increase ${label.toLowerCase()}`}
          disabled={value >= max}
          onClick={() => onChange(clamp(value + step))}
          className="flex h-full w-9 flex-none items-center justify-center rounded-r-lg text-fg-subtle transition-colors hover:text-fg disabled:opacity-30 disabled:hover:text-fg-subtle"
        >
          <Icon.plus size={14} />
        </button>
      </div>
    </div>
  );
}

export default function Landing() {
  const navigate = useNavigate();
  const [tab, setTab] = useState<Tab>("create");
  const [name, setName] = useState("");
  const [difficulty, setDifficulty] = useState<Difficulty>(null);
  const [timeLimit, setTimeLimit] = useState(5);
  const [rounds, setRounds] = useState(1);
  const [roomCode, setRoomCode] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!name.trim()) {
      setError("Enter your name.");
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
    <MotionConfig reducedMotion="user">
      <div className="relative flex min-h-full flex-col items-center justify-center overflow-hidden px-5 py-12">
        <div aria-hidden className="backdrop-grid pointer-events-none absolute inset-0" />
        <div
          aria-hidden
          className="pointer-events-none absolute left-1/2 top-[-280px] h-[560px] w-[900px] -translate-x-1/2 rounded-full opacity-70"
          style={{
            background:
              "radial-gradient(closest-side, rgb(110 110 246 / 0.16), rgb(110 110 246 / 0.04) 55%, transparent)",
          }}
        />

        <motion.header
          initial={{ opacity: 0, y: 6 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, ease }}
          className="relative mb-8 flex flex-col items-center text-center"
        >
          <Wordmark size={36} />
          <h1 className="mt-6 text-[28px] font-semibold leading-tight tracking-[-0.03em] text-fg sm:text-[32px]">
            Race your friends to the
            <br />
            shortest correct solution.
          </h1>
          <p className="mt-3 max-w-[380px] text-[14px] text-fg-muted">
            Same problem, same clock. Pass every test in Python, then shave
            characters until time runs out.
          </p>
        </motion.header>

        <motion.main
          initial={{ opacity: 0, y: 10, scale: 0.99 }}
          animate={{ opacity: 1, y: 0, scale: 1 }}
          transition={{ duration: 0.5, delay: 0.08, ease }}
          className="pop relative w-full max-w-[420px] overflow-hidden bg-raised/90 backdrop-blur-xl"
        >
          <div className="border-b border-line p-1.5">
            <div
              role="tablist"
              aria-label="Room mode"
              className="relative grid grid-cols-2 gap-1 rounded-lg bg-sunken p-1"
            >
              {(["create", "join"] as const).map((value) => (
                <button
                  key={value}
                  role="tab"
                  type="button"
                  id={`tab-${value}`}
                  aria-selected={tab === value}
                  aria-controls={`panel-${value}`}
                  onClick={() => {
                    setTab(value);
                    setError("");
                  }}
                  className={cx(
                    "relative h-8 rounded-md text-[13px] font-medium transition-colors",
                    tab === value ? "text-fg" : "text-fg-subtle hover:text-fg-muted",
                  )}
                >
                  {tab === value && (
                    <motion.span
                      layoutId="landing-tab"
                      transition={{ duration: 0.25, ease }}
                      className="absolute inset-0 rounded-md border border-line-strong bg-overlay shadow-[inset_0_1px_0_rgb(255_255_255/0.05),0_1px_2px_rgb(0_0_0/0.4)]"
                    />
                  )}
                  <span className="relative">
                    {value === "create" ? "Create a room" : "Join with code"}
                  </span>
                </button>
              ))}
            </div>
          </div>

          <form
            id={`panel-${tab}`}
            role="tabpanel"
            aria-labelledby={`tab-${tab}`}
            onSubmit={(event) => {
              void handleSubmit(event);
            }}
            className="flex flex-col gap-5 p-5"
          >
            <div className="flex flex-col gap-1.5">
              <label htmlFor="name" className="text-[12.5px] font-medium text-fg-muted">
                Display name
              </label>
              <input
                id="name"
                required
                autoFocus
                autoComplete="nickname"
                type="text"
                value={name}
                onChange={(event) => setName(event.target.value)}
                maxLength={20}
                placeholder="Ada Lovelace"
                className="field"
              />
            </div>

            <AnimatePresence mode="wait" initial={false}>
              {tab === "create" ? (
                <motion.div
                  key="create"
                  initial={{ opacity: 0, y: 4 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -4 }}
                  transition={{ duration: 0.16 }}
                  className="flex flex-col gap-5"
                >
                  <div className="flex flex-col gap-1.5">
                    <span id="difficulty-label" className="text-[12.5px] font-medium text-fg-muted">
                      Difficulty
                    </span>
                    <div
                      role="radiogroup"
                      aria-labelledby="difficulty-label"
                      className="grid grid-cols-4 gap-1 rounded-lg border border-line-strong bg-sunken p-1"
                    >
                      {DIFFICULTIES.map((option) => {
                        const active = difficulty === option.value;
                        return (
                          <button
                            key={option.label}
                            type="button"
                            role="radio"
                            aria-checked={active}
                            onClick={() => setDifficulty(option.value)}
                            className={cx(
                              "inline-flex h-8 items-center justify-center gap-1.5 rounded-md text-[12.5px] font-medium transition-colors",
                              active
                                ? "bg-overlay text-fg shadow-[inset_0_0_0_1px_var(--color-line-strong),inset_0_1px_0_rgb(255_255_255/0.05)]"
                                : "text-fg-subtle hover:bg-white/[0.03] hover:text-fg-muted",
                            )}
                          >
                            <span
                              aria-hidden
                              className={cx(
                                "size-1.5 rounded-full transition-opacity",
                                difficultyDot[option.label],
                                !active && "opacity-50",
                              )}
                            />
                            {option.label}
                          </button>
                        );
                      })}
                    </div>
                  </div>
                  <div className="flex gap-3">
                    <Stepper
                      id="time-limit"
                      label="Time limit"
                      value={timeLimit}
                      onChange={setTimeLimit}
                      min={1}
                      max={60}
                      step={0.5}
                      suffix="min"
                    />
                    <Stepper
                      id="rounds"
                      label="Rounds"
                      value={rounds}
                      onChange={setRounds}
                      min={1}
                      max={10}
                      step={1}
                    />
                  </div>
                </motion.div>
              ) : (
                <motion.div
                  key="join"
                  initial={{ opacity: 0, y: 4 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -4 }}
                  transition={{ duration: 0.16 }}
                  className="flex flex-col gap-1.5"
                >
                  <label htmlFor="room-code" className="text-[12.5px] font-medium text-fg-muted">
                    Room code
                  </label>
                  <input
                    id="room-code"
                    required
                    minLength={6}
                    maxLength={6}
                    type="text"
                    autoComplete="off"
                    spellCheck={false}
                    value={roomCode}
                    onChange={(event) =>
                      setRoomCode(event.target.value.toUpperCase().slice(0, 6))
                    }
                    placeholder="ABC123"
                    className="field h-12 text-center font-mono text-[20px] tracking-[0.42em] uppercase placeholder:tracking-[0.42em] placeholder:text-fg-subtle/60"
                  />
                  <p className="text-[12px] text-fg-subtle">
                    Ask the host for the 6-character code shown in their lobby.
                  </p>
                </motion.div>
              )}
            </AnimatePresence>

            <AnimatePresence>
              {error && (
                <motion.p
                  role="alert"
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: "auto" }}
                  exit={{ opacity: 0, height: 0 }}
                  className="-mt-1 flex items-start gap-2 overflow-hidden text-[13px] text-bad"
                >
                  <Icon.alert size={15} className="mt-[2px] flex-none" />
                  {error}
                </motion.p>
              )}
            </AnimatePresence>

            <button type="submit" disabled={loading} className="btn btn-primary btn-lg w-full">
              {loading ? (
                <>
                  <Spinner />
                  {tab === "create" ? "Creating room…" : "Joining…"}
                </>
              ) : (
                <>
                  {tab === "create" ? "Create room" : "Join room"}
                  <Kbd keys={["↵"]} />
                </>
              )}
            </button>
          </form>
        </motion.main>

        <motion.ul
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.6, delay: 0.25 }}
          className="relative mt-6 flex flex-wrap items-center justify-center gap-x-5 gap-y-2 text-[12.5px] text-fg-subtle"
        >
          <li className="inline-flex items-center gap-1.5">
            <Icon.terminal size={14} /> Python 3
          </li>
          <li className="inline-flex items-center gap-1.5">
            <Icon.users size={14} /> Real-time multiplayer
          </li>
          <li className="inline-flex items-center gap-1.5">
            <Icon.trophy size={14} /> Fewest characters wins
          </li>
        </motion.ul>
      </div>
    </MotionConfig>
  );
}
