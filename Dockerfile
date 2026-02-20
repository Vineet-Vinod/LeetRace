# --- Stage 1: Build the Vite frontend ---
FROM node:22-slim AS frontend

WORKDIR /app/frontend
COPY frontend/package.json frontend/pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile
COPY frontend/ .
RUN pnpm build

# --- Stage 2: Python runtime ---
FROM python:3.13-slim

WORKDIR /app

# Install uv for fast dependency resolution
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Install Python dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev --frozen

# Copy application code
COPY server/ server/
COPY main.py .
COPY problems/ problems/
COPY static/ static/

# Copy built frontend from stage 1
COPY --from=frontend /app/frontend/dist frontend/dist

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
