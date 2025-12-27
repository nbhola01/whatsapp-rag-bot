FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Set environment
ENV PYTHONUNBUFFERED=1

# Run bot
CMD ["python", "src/main.py"]
