# FastAPI User Application

A minimal FastAPI starter project with basic CRUD endpoints, Pydantic schemas, and Jinja2 templates for quick UI demos.

## Features
- Simple REST endpoints for listing, creating, searching and deleting items
- Pydantic `schema` validation and model examples
- Lightweight data layer and example templates using Jinja2
- Ready to run with `uvicorn` for local development

## Requirements
- Python 3.9+
- See `requirements.txt` for project dependencies

## Quickstart

1. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app (development)

```bash
uvicorn main:app --reload
```

Open http://localhost:8000 in your browser.

## API Documentation
- Interactive Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Important Endpoints
- `GET /` — Root (returns homepage template)
- `GET /items/{item_id}` — Retrieve item by id
- `POST /items/` — Create a new item
- `GET /search` — Search items (example)
- `GET /delete/{item_id}` — Example delete flow with template

## Project Layout

- `main.py` — FastAPI application and route registration
- `model.py` — Data models / ORM-like examples
- `schema.py` — Pydantic request/response schemas
- `database.py` — Lightweight persistence layer or DB connection
- `templates/` — Jinja2 HTML templates for demo pages

## Contributing
Fork the repo and open a PR. Keep changes small and focused.

## License
This project is provided as-is for learning and prototyping. Add a license file if you intend to publish.

---

If you want, I can add badges, a license file, or a shorter GitHub repo description. Which would you like next?
