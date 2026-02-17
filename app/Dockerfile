# ----------------------------
# Stage 1: Builder
# ----------------------------
FROM python:3.9-slim AS builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies in a separate directory
RUN pip install --prefix=/install -r requirements.txt

# Copy the application code
COPY . .

# ----------------------------
# Stage 2: Final image
# ----------------------------
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY --from=builder /app /app

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
