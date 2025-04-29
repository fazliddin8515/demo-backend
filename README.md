# 🚀 Demo Backend

This is a learning-focused backend project built with FastAPI, designed to explore modern backend development and deployment workflows. It integrates a PostgreSQL database, asynchronous operations, CI/CD pipelines, and containerization.​

The project is part of a full-stack application, with the frontend repository available at [fazliddin8515/demo-frontend](https://github.com/fazliddin8515/demo-frontend).​

## 🧰 Tech Stack

- Backend Framework: [FastAPI](https://github.com/fastapi/fastapi)
- Database: PostgreSQL with [asyncpg](https://github.com/MagicStack/asyncpg)
- ORM: [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) (async)
- Migrations: [Alembic](https://github.com/sqlalchemy/alembic)
- Containerization: Docker & Docker Compose
- Web Server: NGINX (via [SWAG](https://github.com/linuxserver/docker-swag))
- CI/CD: GitHub Actions + [Watchtower](https://github.com/containrrr/watchtower)
- Code Quality: [pre-commit](https://github.com/pre-commit/pre-commit), [Ruff](https://github.com/astral-sh/ruff), [mypy](https://github.com/python/mypy)

## 🐳 Docker & Deployment

### Docker Compose Setup

The application is containerized using Docker. The `docker-compose.yml` includes services for the backend, frontend, database, NGINX (via SWAG), and Watchtower for automated updates.​

Production `docker-compose.yml`:

```yml
services:
  watchtower:
    image: containrrr/watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --cleanup --interval 60

  swag:
    image: linuxserver/swag
    environment:
      - URL=uzbots.uz
    volumes:
      - ./swag:/config
    ports:
      - 80:80
      - 443:443

  demo-frontend:
    image: ghcr.io/fazliddin8515/demo-frontend:main
    depends_on:
      - demo-backend

  demo-backend:
    image: ghcr.io/fazliddin8515/demo-backend:main
    environment:
      DB_URI: postgresql+asyncpg://postgres:123@demo-database:5432/demo
    depends_on:
      - demo-database

  demo-database:
    image: postgres
    environment:
      POSTGRES_PASSWORD: 123
      POSTGRES_DB: demo
```

### NGINX Configuration

The NGINX configuration (`swag/nginx/proxy-confs/demo.subdomain.conf`) routes traffic to the frontend and backend services:

```nginx
server {
    listen 443;
    server_name uzbots.uz;

    location / {
        proxy_pass http://demo-frontend;
    }

    location /api {
        proxy_pass http://demo-backend:8000;
        proxy_set_header Host $host;
    }
}
```

## 🔄 CI/CD Pipeline

The project utilizes GitHub Actions for continuous integration and deployment:​

- **Build & Test**: On each push, the application is built and tests are executed.
- **Docker Image**: Successful builds are pushed to GitHub Container Registry.
- **Deployment**: Watchtower monitors the running containers and automatically updates them when new images are available.​

## 🌐 Frontend Integration

The corresponding frontend for this project is available at [fazliddin8515/demo-frontend](https://github.com/fazliddin8515/demo-frontend).​

The frontend is a simple HTML, CSS, and JavaScript application, served via NGINX, and communicates with the backend API.
