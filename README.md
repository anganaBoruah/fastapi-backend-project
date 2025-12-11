# FastAPI Backend with PostgreSQL and Docker

This project is a FastAPI backend that supports user authentication, media uploads, and a feed system. It was originally built with SQLite but has now been migrated to PostgreSQL. The entire application runs using Docker for easier setup and deployment.

## Features

- FastAPI backend  
- PostgreSQL database  
- SQLAlchemy + Alembic migrations  
- Docker and Docker Compose support  
- JWT authentication  
- Media upload and feed endpoints  

## How to Run (Docker)

1. Create a `.env` file using `.env.example` as a reference.  
2. Build and start the containers:  
   ```bash
   docker-compose up --build
   ```
3. Apply database migrations:  
   ```bash
   docker-compose exec web alembic upgrade head
   ```
4. Open the API documentation:  
   http://localhost:8000/docs

## Environment Variables

Example `.env` values:
```
DATABASE_URL=postgresql://postgres:password@db:5432/fastapi_db
SECRET_KEY=your_secret_key
```

## Notes

- SQLite has been removed; the project now uses PostgreSQL.  
- Alembic handles all database migrations.  
- `.gitignore` and `.dockerignore` are configured to avoid committing sensitive or unnecessary files.
