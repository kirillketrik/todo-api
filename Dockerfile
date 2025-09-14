FROM python:3.12-slim

# Copy .env-dist to .env
COPY .env-dist .env

# Set the working directory
WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy all the files
COPY . .

# Install dependencies
RUN poetry install --no-root

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "localhost", "--port", "8000"]