# Backend Prototype Core v0.1

Created: 2026-04-29

## Purpose

First backend vertical slice for Buildx Repair Platform.

Included:

- FastAPI app
- SQLite database
- SQLAlchemy models
- Pydantic schemas
- Project endpoints
- Room endpoints
- Core geometry summary endpoint
- Health endpoint
- Pytest tests

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Test

```bash
pytest
```

## Current Scope

This phase implements:

```text
Project
Room
RoomGeometry
Core Summary
Basic validation
Structured response envelope
```

Not included yet:

```text
artifact loader
execution engine
material consumption engine
cost engine
procurement engine
frontend
```
