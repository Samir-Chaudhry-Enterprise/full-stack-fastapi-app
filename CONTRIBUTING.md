# Contributing

Thank you for your interest in contributing to the Full Stack FastAPI Template! This document provides
guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Documentation](#documentation)
- [Community](#community)

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code. Please
report unacceptable behavior to the project maintainers.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/full-stack-fastapi-template.git
   cd full-stack-fastapi-template
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/fastapi/full-stack-fastapi-template.git
   ```
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/my-feature
   ```

## Development Setup

Follow the [README Quickstart](README.md#quickstart) to set up your development environment.

**Quick setup:**

```bash
# Start all services with Docker Compose
docker compose up --build

# Or for local development:
# Backend
cd backend
uv sync
source .venv/bin/activate
docker compose up -d db
uv run bash scripts/prestart.sh
fastapi dev app/main.py

# Frontend (in another terminal)
cd frontend
npm install
npm run dev
```

## Development Workflow

1. **Keep your fork up to date**:
   ```bash
   git fetch upstream
   git checkout master
   git merge upstream/master
   ```

2. **Create a feature branch** from `master`:
   ```bash
   git checkout -b feature/my-feature
   ```

3. **Make your changes** following the coding standards

4. **Test your changes** thoroughly:
   ```bash
   # Backend tests
   cd backend
   uv run bash scripts/tests-start.sh
   
   # Frontend tests
   cd frontend
   npm run build
   docker compose run --rm playwright npx playwright test
   ```

5. **Lint and format your code**:
   ```bash
   # Backend
   cd backend
   uv run bash scripts/format.sh
   uv run bash scripts/lint.sh
   
   # Frontend
   cd frontend
   npm run lint
   ```

6. **Commit your changes** with a descriptive message

7. **Push to your fork**:
   ```bash
   git push origin feature/my-feature
   ```

8. **Create a Pull Request** on GitHub

## Coding Standards

### General Guidelines

- Write clear, readable, and maintainable code
- Follow existing code style and conventions
- Add comments for complex logic, but prefer self-documenting code
- Keep functions small and focused on a single responsibility
- Use meaningful variable and function names

### Backend (Python)

- **Style**: Follow PEP 8 guidelines
- **Formatting**: Use Ruff for formatting (configured in `pyproject.toml`)
- **Linting**: Use Ruff for linting
- **Type Hints**: Use type hints for all function signatures
- **Imports**: Organize imports (stdlib, third-party, local)
- **Docstrings**: Use docstrings for public functions and classes

**Example:**
```python
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.api.deps import CurrentUser, SessionDep
from app.models import Item, ItemCreate, ItemPublic


def create_item(
    *,
    session: SessionDep,
    item_in: ItemCreate,
    current_user: CurrentUser,
) -> Item:
    """
    Create a new item for the current user.
    """
    item = Item.model_validate(item_in, update={"owner_id": current_user.id})
    session.add(item)
    session.commit()
    session.refresh(item)
    return item
```

**Run formatting and linting:**
```bash
cd backend
uv run bash scripts/format.sh  # Auto-format code
uv run bash scripts/lint.sh    # Check for issues
uv run mypy app                # Type checking
```

### Frontend (TypeScript/React)

- **Style**: Follow TypeScript and React best practices
- **Formatting**: Use Biome for formatting and linting
- **Type Safety**: Use TypeScript types, avoid `any`
- **Components**: Use functional components with hooks
- **State Management**: Use TanStack Query for server state
- **Naming**: Use PascalCase for components, camelCase for functions

**Example:**
```typescript
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { ItemsService, type ItemCreate } from "@/client"

export function useCreateItem() {
  const queryClient = useQueryClient()
  
  return useMutation({
    mutationFn: (data: ItemCreate) =>
      ItemsService.createItem({ requestBody: data }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["items"] })
    },
  })
}
```

**Run linting:**
```bash
cd frontend
npm run lint  # Auto-format and lint
```

## Testing

### Backend Tests

- Write tests for all new features and bug fixes
- Use pytest for testing
- Aim for high test coverage (90%+)
- Test both success and error cases
- Use fixtures for common test data

**Run tests:**
```bash
cd backend
uv run bash scripts/tests-start.sh  # Run all tests with coverage
uv run pytest tests/api/routes/test_items.py  # Run specific test file
uv run pytest -v tests/  # Verbose output
```

**Example test:**
```python
def test_create_item(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    data = {"title": "Test Item", "description": "Test Description"}
    response = client.post(
        f"{settings.API_V1_STR}/items/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert "id" in content
```

### Frontend Tests

- Write E2E tests for critical user flows
- Use Playwright for end-to-end testing
- Test across different browsers if applicable
- Test both desktop and mobile viewports

**Run tests:**
```bash
cd frontend
npm run build
docker compose run --rm playwright npx playwright test
docker compose run --rm playwright npx playwright test --ui  # Interactive mode
```

## Pull Request Process

1. **Update documentation** if you're changing functionality
2. **Add tests** for new features or bug fixes
3. **Ensure all tests pass** locally before submitting
4. **Run linting and formatting** on your code
5. **Update the README** if you're adding new features or changing setup
6. **Keep PRs focused** - one feature or fix per PR
7. **Write a clear PR description**:
   - What changes were made
   - Why the changes were necessary
   - How to test the changes
   - Screenshots for UI changes

### PR Title Format

Use conventional commit format for PR titles:

- `feat: add user profile page`
- `fix: resolve CORS issue in production`
- `docs: update deployment guide`
- `refactor: simplify authentication logic`
- `test: add tests for item CRUD operations`
- `chore: update dependencies`

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests you ran to verify your changes.

## Screenshots (if applicable)
Add screenshots for UI changes.

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
```

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that don't affect code meaning (formatting, etc.)
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Performance improvement
- **test**: Adding or updating tests
- **chore**: Changes to build process or auxiliary tools

### Examples

```bash
feat(auth): add password reset functionality

Implement password reset flow with email verification.
Users can now request a password reset link via email.

Closes #123

---

fix(api): resolve CORS issue in production

Update CORS origins to include production frontend URL.

---

docs(readme): update quickstart instructions

Add missing step for database initialization.
```

## Documentation

- Update the README.md for user-facing changes
- Update inline code comments for complex logic
- Add docstrings for new functions and classes
- Update API documentation if changing endpoints
- Consider adding examples for new features

## Community

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/fastapi/full-stack-fastapi-template/issues)
- **Discussions**: Ask questions or share ideas in [GitHub Discussions](https://github.com/fastapi/full-stack-fastapi-template/discussions)
- **Pull Requests**: Submit contributions via [Pull Requests](https://github.com/fastapi/full-stack-fastapi-template/pulls)

## Questions?

If you have questions about contributing, feel free to:
- Open a [GitHub Discussion](https://github.com/fastapi/full-stack-fastapi-template/discussions)
- Ask in an existing issue or PR
- Check the [README](README.md) for general documentation

Thank you for contributing to the Full Stack FastAPI Template! 🎉
