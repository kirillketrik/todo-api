# Stage 1: Build the virtual environment
FROM python:3.12-slim as builder

# Install poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy the dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root --no-dev

# Stage 2: Build the runtime image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
