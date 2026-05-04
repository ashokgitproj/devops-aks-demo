# Stage 1 — nothing to build for static HTML, just copy
FROM nginx:1.25-alpine AS runtime
COPY src/index.html /usr/share/nginx/html/index.html
EXPOSE 80