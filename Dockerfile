# Build the Application
FROM python:3.12-slim
WORKDIR /app

# Install CA certificates needed for MongoDB Atlas TLS
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*

# Install backend dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code (Backend + Frontend natively)
COPY . .

# Environment variables
ENV PYTHONUNBUFFERED=1

# Expose the application port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
