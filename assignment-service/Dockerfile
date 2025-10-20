FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY --from=ghcr.io/astral-sh/uv:0.5.11 /uv /uvx /bin/

ENV PATH="/app/.venv/bin:$PATH"

ENV UV_COMPILE_BYTECODE=1

ENV UV_LINK_MODE=copy

COPY ./shared-models /shared-models/

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=assignment-service/uv.lock,target=uv.lock \
    --mount=type=bind,source=assignment-service/pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

ENV PYTHONPATH=/app

COPY ./assignment-service/pyproject.toml ./assignment-service/uv.lock /app/

COPY ./assignment-service/app /app/app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync

CMD ["fastapi", "run", "--port", "8001", "--workers", "4", "app/main.py"]
