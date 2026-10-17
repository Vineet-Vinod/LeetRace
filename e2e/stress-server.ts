import { randomUUID } from 'node:crypto';
import { createAppServer } from '../server/http.js';
import { Persistence } from '../server/persistence.js';
import type { Problem } from '../server/problems.js';
import { createRouter } from '../server/router.js';
import { RoomStore } from '../server/rooms.js';

if (process.env.NODE_ENV === 'production' || !process.env.CLERK_SECRET_KEY?.startsWith('sk_test_')) {
  throw new Error('Stress tests require Clerk development credentials.');
}

const runId = randomUUID();
let problemNumber = 0;
function problem(): Problem {
  const offset = ++problemNumber;
  return {
    id: `stress-${runId}-${offset}`,
    title: `Stress challenge ${offset}`,
    difficulty: 'Easy',
    statement: `Return value + ${offset}. This synthetic puzzle exercises the real submission judge.`,
    starterCode: 'class Solution:\n    def solve(self, value: int) -> int:\n        pass\n',
    entryPoint: 'Solution().solve',
    parameters: [{ name: 'value', type: 'int' }],
    returnType: 'int',
    tests: Array.from({ length: 64 }, (_, index) => ({ input: [index - 32], expected: index - 32 + offset })),
  };
}

const persistence = new Persistence();
const rooms = new RoomStore(problem, undefined, undefined, { onEvent: (event) => persistence.enqueue(event) });
const router = createRouter(rooms, undefined, () => persistence.flush());
const server = createAppServer(router, undefined, { health: () => persistence.healthy });
const ticker = setInterval(() => {
  rooms.tick();
  void persistence.flush().catch(() => console.error('Stress-test stats remain queued.'));
}, 1000);
const port = Number(new URL(process.env.E2E_BASE_URL ?? 'http://127.0.0.1:3011').port);
server.listen(port, '127.0.0.1', () => console.log(`Stress server listening on ${port}`));
async function shutdown() {
  clearInterval(ticker);
  server.close();
  server.closeAllConnections();
  await persistence.flush();
}
process.on('SIGTERM', () => { void shutdown(); });
process.on('SIGINT', () => { void shutdown(); });
