FROM python:3.11-slim

WORKDIR /app

# system deps needed for asyncpg + pg tools
RUN apt-get update \
  && apt-get install -y build-essential libpq-dev postgresql-client gcc --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

# copy and install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY . .

# make entrypoint executable
RUN chmod +x ./entrypoint.sh

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

# default command: wait for db, run migrations, start uvicorn
CMD ["./entrypoint.sh", "db"]
