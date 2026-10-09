import { lazy, Suspense } from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import Landing from "./pages/Landing";

const Room = lazy(() => import("./components/Room"));

export default function App() {
  return (
    <Suspense
      fallback={
        <p className="p-10 text-sm text-ink-dim">
          <span className="text-amber-lo">&gt; </span>loading room module
          <span className="cursor-block" />
        </p>
      }
    >
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/room" element={<Room />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Suspense>
  );
}
