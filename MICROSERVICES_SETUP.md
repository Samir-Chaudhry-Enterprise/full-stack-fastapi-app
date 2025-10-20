# Microservices Setup Guide

## Overview
This application now uses a microservice architecture with the following services:
- **Backend**: Main FastAPI application
- **Assignment Service**: Microservice for handling item assignments
- **Shared Models**: Shared data models package

## Architecture

### Shared Models Package
Location: `shared-models/`

Contains shared data models (User, Item) used by both backend and assignment-service.

**Models included:**
- User models: UserBase, UserCreate, UserRegister, UserUpdate, UserUpdateMe, UpdatePassword, User, UserPublic, UsersPublic
- Item models: ItemBase, ItemCreate, ItemUpdate, Item, ItemPublic, ItemsPublic

### Assignment Service
Location: `assignment-service/`

**Endpoint:** `POST /api/v1/assignments/assign`

**Request Body:**
```json
{
  "item_id": "uuid",
  "user_id": "uuid",
  "is_superuser": bool
}
```

**Functionality:**
- Validates item exists in database
- Validates user permissions (superuser or owner)
- Returns success message

## Environment Setup

### Prerequisites
- Python 3.10+
- Docker and Docker Compose
- uv package manager

### Local Development Setup

1. **Install shared-models package:**
```bash
cd shared-models
uv sync
```

2. **Install backend dependencies:**
```bash
cd backend
uv sync
```

3. **Install assignment-service dependencies:**
```bash
cd assignment-service
uv sync
```

4. **Configure environment variables:**
Ensure `.env` file has:
```env
ASSIGNMENT_SERVICE_URL=http://assignment-service:8001
```

### Running with Docker Compose

```bash
docker compose up --build
```

Services will be available at:
- Backend: http://localhost:8000
- Assignment Service: http://localhost:8001
- Frontend: http://localhost:5173

## Database

Both backend and assignment-service connect to the same PostgreSQL database using these environment variables:
- `POSTGRES_SERVER=db` (in Docker)
- `POSTGRES_PORT=5432`
- `POSTGRES_DB=app`
- `POSTGRES_USER=postgres`
- `POSTGRES_PASSWORD=changethis`

## Testing

### Lint Checks
```bash
# Backend
cd backend && uv run ruff check .

# Assignment Service
cd assignment-service && uv run ruff check .
```

### Integration Testing
The "send for assignment" endpoint can be tested through:
1. Frontend UI: Items page → Actions → Send for assignment
2. API directly: `POST /api/v1/items/{id}/send-for-assignment`

## Troubleshooting

### Shared Models Import Issues
If you encounter import errors with shared_models, ensure:
1. The shared-models package is installed in both services
2. The path in pyproject.toml is correct: `shared-models = { path = "../shared-models", editable = true }`
3. Import from `shared_models.models` not `shared_models.app.models`

### Service Communication Issues
If backend cannot reach assignment-service:
1. Check both services are running: `docker compose ps`
2. Verify ASSIGNMENT_SERVICE_URL is set correctly
3. Check assignment-service health: `docker compose logs assignment-service`
