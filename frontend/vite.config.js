import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';

const frontendPort = parseInt(process.env.FRONTEND_PORT || '3000', 10);
const backendPort = parseInt(process.env.BACKEND_PORT || '8000', 10);

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    port: frontendPort,
    host: '0.0.0.0',
    proxy: {
      '/api': `http://localhost:${backendPort}`,
      '/ws': {
        target: `http://localhost:${backendPort}`,
        ws: true,
      },
    },
  },
});
