import { useState, type FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import { AnimatePresence, motion } from "framer-motion";
import { api, errorMessage, saveSession, type RouterInputs } from "../api";

type Difficulty = RouterInputs["createRoom"]["difficulty"];

const DIFFICULTIES: { value: Difficulty; label: string; tone: string }[] = [
  { value: null, label: "Any", tone: "bg-pit-blue text-carbon" },
  { value: "Easy", label: "Easy", tone: "bg-sector-green text-carbon" },
  { value: "Medium", label: "Medium", tone: "bg-sector-yellow text-carbon" },
  { value: "Hard", label: "Hard", tone: "bg-signal text-white" },
];

const ease = [0.16, 1, 0.3, 1] as const;

function Stepper({
  label,
  value,
  step,
  min,
  max,
  unit,
  onChange,
}: {
  label: string;
  value: number;
  step: number;
  min: number;
  max: number;
  unit: string;
  onChange: (value: number) => void;
}) {
  const set = (next: number) =>
    onChange(Math.min(max, Math.max(min, Math.round(next / step) * step)));
  return (
    <div className="flex-1 flex flex-col gap-2">
      <span className="label">{label}</span>
      <div className="flex h-11 border border-line bg-pit focus-within:border-signal">
        <button
          type="button"
          aria-label={`Decrease ${label}`}
          onClick={() => set(value - step)}
          disabled={value <= min}
          className="w-10 text-ink-muted hover:text-ink hover:bg-raised disabled:opacity-30"
        >
          −
        </button>
        <label className="flex-1 flex items-baseline justify-center gap-1.5 border-x border-line">
          <input
            aria-label={label}
            type="number"
            min={min}
            max={max}
            step={step}
            value={value}
            onChange={(event) => set(event.target.valueAsNumber || min)}
            className="w-12 bg-transparent text-center font-display text-xl font-semibold italic outline-none self-center"
          />
          <span className="label self-center -ml-1">{unit}</span>
        </label>
        <button
          type="button"
          aria-label={`Increase ${label}`}
          onClick={() => set(value + step)}
          disabled={value >= max}
          className="w-10 text-ink-muted hover:text-ink hover:bg-raised disabled:opacity-30"
        >
          +
        </button>
      </div>
    </div>
  );
}

export default function Landing() {
  const navigate = useNavigate();
  const [tab, setTab] = useState<"create" | "join">("create");
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
      setError("Enter your driver name.");
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
    <div className="min-h-screen flex flex-col">
      <div className="kerb h-1.5 opacity-90" />
      <main className="flex-1 grid lg:grid-cols-[1.1fr_1fr] items-center gap-12 px-6 py-12 lg:px-16 max-w-7xl w-full mx-auto">
        <section className="relative">
          <div className="speed-lines absolute -inset-x-16 -inset-y-10 pointer-events-none [mask-image:linear-gradient(90deg,black,transparent)]" />
          <motion.p
            initial={{ opacity: 0, x: -16 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, ease }}
            className="relative flex items-center gap-3 label text-signal mb-5"
          >
            <span className="flex gap-1">
              {[0, 1, 2, 3, 4].map((light) => (
                <span
                  key={light}
                  className="size-2.5 rounded-full animate-light-on"
                  style={{ animationDelay: `${light * 0.18}s` }}
                />
              ))}
            </span>
            Lights out and away we go
          </motion.p>
          <motion.h1
            initial={{ opacity: 0, x: -40 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.7, ease }}
            className="relative font-display font-extrabold italic uppercase leading-[0.82] tracking-tight"
            style={{ fontSize: "clamp(4.5rem, 11vw, 9rem)" }}
          >
            Leet
            <br />
            <span className="text-signal">Race</span>
            <span className="inline-block w-[0.5em] h-[0.12em] ml-3 align-middle bg-ink -skew-x-12" />
          </motion.h1>
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.3, duration: 0.6 }}
            className="relative mt-7 max-w-md text-ink-muted text-lg leading-relaxed"
          >
            Same problem, same clock. Pass every test, then trim your Python
            down: the shortest solution takes pole.
          </motion.p>
          <motion.dl
            initial={{ opacity: 0, y: 12 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.45, duration: 0.6, ease }}
            className="relative mt-10 grid grid-cols-3 max-w-md border-l-2 border-signal"
          >
            {[
              ["20", "Drivers per room"],
              ["10", "Rounds per race"],
              ["1", "Shortest wins"],
            ].map(([value, label]) => (
              <div key={label} className="px-4 border-r border-line">
                <dt className="label">{label}</dt>
                <dd className="font-display text-3xl font-bold italic mt-1">
                  {value}
                </dd>
              </div>
            ))}
          </motion.dl>
        </section>

        <motion.section
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.15, duration: 0.6, ease }}
          className="relative w-full max-w-[460px] lg:justify-self-end bg-panel border border-line shadow-[0_30px_80px_-20px_rgba(0,0,0,0.8)]"
        >
          <div className="absolute -top-px left-0 h-[3px] w-24 bg-signal" />
          <div className="grid grid-cols-2 border-b border-line">
            {(["create", "join"] as const).map((value) => (
              <button
                key={value}
                type="button"
                onClick={() => {
                  setTab(value);
                  setError("");
                }}
                aria-pressed={tab === value}
                className={`relative h-14 font-display text-sm font-semibold uppercase italic tracking-[0.18em] transition-colors ${
                  tab === value ? "text-ink" : "text-ink-dim hover:text-ink-muted"
                }`}
              >
                {value === "create" ? "Create room" : "Join room"}
                {tab === value && (
                  <motion.span
                    layoutId="landing-tab"
                    className="absolute inset-x-0 -bottom-px h-[3px] bg-signal"
                    transition={{ type: "spring", stiffness: 500, damping: 36 }}
                  />
                )}
              </button>
            ))}
          </div>
          <form onSubmit={handleSubmit} className="p-7 flex flex-col gap-6">
            <label className="flex flex-col gap-2">
              <span className="label">Driver name</span>
              <input
                required
                autoFocus
                value={name}
                onChange={(event) => setName(event.target.value)}
                maxLength={20}
                placeholder="e.g. Verstappen"
                className="field font-display text-lg italic font-medium tracking-wide"
              />
            </label>
            <AnimatePresence mode="wait" initial={false}>
              {tab === "create" ? (
                <motion.div
                  key="create"
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: 10 }}
                  transition={{ duration: 0.18 }}
                  className="flex flex-col gap-6"
                >
                  <fieldset className="flex flex-col gap-2">
                    <legend className="label mb-2">Difficulty</legend>
                    <div className="grid grid-cols-4 gap-1.5">
                      {DIFFICULTIES.map((option) => (
                        <button
                          key={option.label}
                          type="button"
                          aria-pressed={difficulty === option.value}
                          onClick={() => setDifficulty(option.value)}
                          className={`plate h-10 font-display text-sm font-semibold uppercase tracking-[0.12em] transition-colors ${
                            difficulty === option.value
                              ? option.tone
                              : "bg-pit text-ink-muted hover:bg-raised hover:text-ink"
                          }`}
                        >
                          <span className="block">{option.label}</span>
                        </button>
                      ))}
                    </div>
                  </fieldset>
                  <div className="flex gap-4">
                    <Stepper
                      label="Lap time"
                      unit="min"
                      value={timeLimit}
                      step={0.5}
                      min={1}
                      max={60}
                      onChange={setTimeLimit}
                    />
                    <Stepper
                      label="Rounds"
                      unit="laps"
                      value={rounds}
                      step={1}
                      min={1}
                      max={10}
                      onChange={setRounds}
                    />
                  </div>
                </motion.div>
              ) : (
                <motion.label
                  key="join"
                  initial={{ opacity: 0, x: 10 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -10 }}
                  transition={{ duration: 0.18 }}
                  className="flex flex-col gap-2"
                >
                  <span className="label">Room code</span>
                  <input
                    required
                    minLength={6}
                    maxLength={6}
                    value={roomCode}
                    onChange={(event) =>
                      setRoomCode(event.target.value.slice(0, 6).toUpperCase())
                    }
                    placeholder="A1B2C3"
                    className="field h-16 text-center font-mono text-3xl tracking-[0.45em] uppercase"
                  />
                </motion.label>
              )}
            </AnimatePresence>
            <button
              type="submit"
              disabled={loading}
              className="btn btn-go h-12 text-base w-full"
            >
              {loading ? (
                <span className="size-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
              ) : tab === "create" ? (
                "Create room"
              ) : (
                "Join the grid"
              )}
              {!loading && <span aria-hidden>→</span>}
            </button>
            <AnimatePresence>
              {error && (
                <motion.p
                  role="alert"
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: "auto" }}
                  exit={{ opacity: 0, height: 0 }}
                  className="text-signal-bright text-sm border-l-2 border-signal pl-3"
                >
                  {error}
                </motion.p>
              )}
            </AnimatePresence>
          </form>
        </motion.section>
      </main>
      <footer className="px-6 lg:px-16 py-5 flex justify-between label border-t border-line">
        <span>Python · Monaco</span>
        <span>Ranked by characters, then lock-in time</span>
      </footer>
    </div>
  );
}
