import { createAppServer } from './http.js';
import { appRouter, rooms, persistence } from './router.js';
import { validateConfiguration } from './config.js';
import { clerkWebhook } from './webhooks.js';
import { verifyRunnerIsolation } from './sandbox.js';

const port = Number(process.env.BACKEND_PORT ?? process.env.PORT ?? 8000);
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error('BACKEND_PORT or PORT must be between 1 and 65535.');
validateConfiguration();
await verifyRunnerIsolation();
const server = createAppServer(appRouter, undefined, {
  health: () => persistence.healthy,
  webhook: (request) => clerkWebhook(request, rooms),
});
const ticker = setInterval(() => {
  rooms.tick();
  void persistence.flush().catch(() => console.error('Stats could not be saved. They remain queued for retry.'));
}, 1000);
ticker.unref();
server.listen(port, '0.0.0.0', () => console.log(`Terse listening on http://localhost:${port}`));

async function shutdown() {
  clearInterval(ticker);
  server.close();
  server.closeAllConnections();
  await persistence.flush().catch(() => console.error('Shutdown could not finish saving queued stats.'));
}
process.on('SIGTERM', () => { void shutdown(); });
process.on('SIGINT', () => { void shutdown(); });
