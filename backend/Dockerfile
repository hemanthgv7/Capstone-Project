# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy only requirements first (layer caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Create non-root user (security best practice)
RUN useradd -m appuser

# Copy installed packages from builder
COPY --from=builder /usr/local /usr/local

# Copy application code
COPY app.py db.py ./

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
