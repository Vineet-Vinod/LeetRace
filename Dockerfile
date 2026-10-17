FROM node:24-slim AS build
WORKDIR /app
ARG VITE_CLERK_PUBLISHABLE_KEY
RUN corepack enable
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
RUN pnpm install --frozen-lockfile
COPY tsconfig*.json ./
COPY convex/ convex/
COPY server/ server/
COPY frontend/ frontend/
RUN pnpm build && pnpm prune --prod

FROM node:24-slim
RUN apt-get update && apt-get install -y --no-install-recommends bubblewrap python3 python3-venv && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt ./
RUN python3 -m venv .venv && .venv/bin/pip install --no-cache-dir -r requirements.txt
ARG VITE_CLERK_PUBLISHABLE_KEY
ENV NODE_ENV=production
ENV VITE_CLERK_PUBLISHABLE_KEY=$VITE_CLERK_PUBLISHABLE_KEY
COPY --from=build /app/package.json ./
COPY --from=build /app/node_modules/ node_modules/
COPY --from=build /app/dist/ dist/
COPY --from=build /app/frontend/dist/ frontend/dist/
COPY problems/ problems/
USER node
EXPOSE 8000
CMD ["node", "dist/server/index.js"]
