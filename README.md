# ApplyFlow — Capstone Edition

A private job application tracker, taken from a working prototype through the full software lifecycle: tested, containerized, running in CI, and deployed live from its own Docker image.

**Live app:** https://applyflow-pi.vercel.app
**Live API:** https://applyflow-jdpr.onrender.com/health
**API docs:** https://applyflow-jdpr.onrender.com/docs

---

## Why This Version Exists

ApplyFlow already worked as a deployed app. This version proves something different: that the same codebase can survive the process a real engineering team would put it through before trusting it in production — automated tests, a reproducible container, continuous integration that actually catches regressions, and a deploy pipeline that runs from that same container rather than a hand-configured server.

## Tech Stack

**Backend**
- FastAPI (Python) + SQLAlchemy + PostgreSQL
- pytest + pytest-cov (testing)
- Docker + Docker Compose (containerization)
- GitHub Actions (CI)

**Frontend**
- React (Vite) + Tailwind CSS

**Deployment**
- Backend: Render, built and deployed directly from the Dockerfile
- Frontend: Vercel

## Testing

14 tests covering every endpoint's happy path and failure path, plus filtering, sorting, and partial-update behavior — 96% coverage of the application code.

```bash
cd backend
pip install pytest pytest-cov httpx
pytest --cov=app --cov-report=term-missing
```

Tests run against an isolated, throwaway SQLite database (see `tests/conftest.py`) — they never touch real data, and every test starts from a clean slate.

**Verified, not just claimed:** CI was deliberately broken (an assertion changed to expect the wrong status code) and confirmed to fail red, then restored and confirmed to pass green again — proof the pipeline actually catches regressions rather than just running without checking anything.

## Containerization

```bash
docker build -t applyflow-backend .
docker run -p 8000:8000 --env-file .env.docker applyflow-backend
```

Or, to run the whole stack (app + a fresh PostgreSQL) with one command:

```bash
docker compose up --build
```

`docker-compose.yml` spins up both the API and a disposable Postgres instance together, networked automatically — no manual database setup required to try the project locally.

## Continuous Integration

Every push and pull request triggers `.github/workflows/ci.yml`, which:
1. Checks out the code
2. Sets up Python 3.12
3. Installs dependencies
4. Runs the full pytest suite with coverage

This runs on GitHub's own servers, independent of any single developer's machine — the guarantee a green checkmark is supposed to represent.

## Architecture

```
React Frontend (Vercel)
        |
        | HTTPS / JSON
        v
FastAPI Backend (Render — deployed from Docker image)
        |
        | SQLAlchemy
        v
PostgreSQL Database (Render)
```

## Run It Locally

### With Docker (recommended — matches production exactly)

```bash
docker compose up --build
```

API available at `http://localhost:8000`.

### Without Docker

```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

Create `.env`:
```
DATABASE_URL=postgresql://user:password@localhost/applyflow
```

```bash
uvicorn app.main:app --reload
```

```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /applications | Create an application |
| GET | /applications | List applications (filter by status, sort by field) |
| GET | /applications/{id} | Get one application |
| PATCH | /applications/{id} | Update an application |
| DELETE | /applications/{id} | Delete an application |
| GET | /applications/summary | Counts grouped by status |
| GET | /health | Health check |

## What Carrying This Through the Full Lifecycle Actually Involved

Worth being honest about, since it's part of the real story: getting Docker running locally on Windows required enabling virtualization at the BIOS/firmware level (not just a Windows setting), which wasn't obvious from the error messages alone. This is a genuine, common real-world environment issue — not a shortcut skipped, a real one worked through.

## Author

**Sandeep Kaur**
[GitHub](https://github.com/ksidhu3005-blip) - [LinkedIn](https://linkedin.com/in/sandeep-kaur-172272422)