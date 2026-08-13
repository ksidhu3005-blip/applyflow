\# ApplyFlow



A private job application tracker — built to replace a messy spreadsheet with a real full-stack tool that tracks every application's company, role, status, and key dates in one place.



\*\*Live app:\*\* https://applyflow-pi.vercel.app

\*\*API:\*\* https://applyflow-nign.onrender.com/docs



\---



\## The Problem It Solves



Job searching across multiple markets (I was applying to roles in the UAE, Saudi Arabia, and the UK simultaneously) quickly turns into a mess of half-updated spreadsheets and forgotten follow-ups. ApplyFlow gives me one place to log every application, see my pipeline at a glance (Applied / Interview / Offer / Rejected), and never lose track of a link or a note again.



\## Tech Stack



\*\*Backend\*\*

\- FastAPI (Python)

\- PostgreSQL

\- SQLAlchemy (ORM)

\- Pydantic (validation)



\*\*Frontend\*\*

\- React (Vite)

\- Tailwind CSS

\- Axios



\*\*Deployment\*\*

\- Backend + database: Render

\- Frontend: Vercel



\## Features



\- Full CRUD — add, view, and delete job applications

\- Status tracking with color-coded badges (Applied, Interview, Offer, Rejected)

\- Live dashboard showing counts per status

\- Data persists in a real PostgreSQL database, not local storage



\## Architecture



React Frontend (Vercel) → FastAPI Backend (Render) → PostgreSQL Database (Render)



The backend follows a layered structure — `models.py` (database shape), `schemas.py` (API contract), `crud.py` (business logic), and `routers/` (HTTP endpoints) — keeping each concern isolated and independently testable.



\## Run It Locally



\### Backend



```bash

cd backend

python -m venv venv

venv\\Scripts\\activate          # Windows

pip install -r requirements.txt

```



Create a `.env` file in `backend/`:DATABASE\_URL=postgresql://user:password@localhost/applyflow

Then run:

```bash

uvicorn app.main:app --reload

```



API available at `http://localhost:8000`, interactive docs at `http://localhost:8000/docs`.



\### Frontend



```bash

cd frontend

npm install

npm run dev

```



App available at `http://localhost:5173`.



\## API Endpoints



| Method | Endpoint | Description |

|---|---|---|

| POST | /applications | Create a new application |

| GET | /applications | List all applications (filter by status, sort by date) |

| GET | /applications/{id} | Get a single application |

| PATCH | /applications/{id} | Update an application |

| DELETE | /applications/{id} | Delete an application |

| GET | /applications/summary | Get counts grouped by status |

| GET | /health | Health check |



\## What's Next



\- Inline editing (currently requires delete + re-add to change a status)

\- Filter and sort controls in the UI

\- Automated tests with pytest

\- CI pipeline via GitHub Actions



\## Author



\*\*Sandeep Kaur\*\*

\[GitHub](https://github.com/ksidhu3005-blip) · \[LinkedIn](https://linkedin.com/in/sandeep-kaur-172272422)

