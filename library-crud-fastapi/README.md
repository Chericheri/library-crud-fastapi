# 📚 Library CRUD API (FastAPI + SQLite)

A minimal, fully-working **Create-Read-Update-Delete** service for **Authors** and **Books**.  
Perfect for Assignment Question 2 (FastAPI branch).

---

## ⚙️ How It Works (high-level)

1. **FastAPI** exposes REST endpoints (JSON over HTTP).  
2. **SQLAlchemy** maps Python classes (`Author`, `Book`) to SQLite tables.  
3. **Pydantic** validates every incoming/outgoing JSON.  
4. **Uvicorn** is the ASGI server that handles requests.  
5. **SQLite** (`library.db`) stores the data locally—no install, no password.

---

## 🧪 Run in 2 Minutes (Windows, macOS, Linux)

### 1. Clone / download this repo
```bash
git clone https://github.com/YOUR_USERNAME/library-crud-fastapi.git
cd library-crud-fastapi
```

### 2. Create & activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the server
```bash
uvicorn main:app --reload
```
(default URL: http://127.0.0.1:8000)

---

## 📖 Using the API

### A. Interactive Docs (Swagger)
Open http://127.0.0.1:8000/docs  
Click any endpoint → `Try it out` → fill body/parameters → `Execute`

### B. Raw `curl` / PowerShell Examples

```powershell
# 1. Add an author
curl -X POST "http://127.0.0.1:8000/authors" `
     -H "Content-Type: application/json" `
     -d '{"name":"Agatha Christie"}'

# 2. List authors
curl http://127.0.0.1:8000/authors

# 3. Add a book (author_id = 1)
curl -X POST "http://127.0.0.1:8000/books" `
     -H "Content-Type: application/json" `
     -d '{"title":"Murder on the Orient Express","author_id":1}'

# 4. Update book title
curl -X PUT "http://127.0.0.1:8000/books/1?title=New Title"

# 5. Delete book
curl -X DELETE "http://127.0.0.1:8000/books/1"
```

---

## 📡 API Endpoints

| HTTP | Endpoint | Description | Request Body / Query |
|------|----------|-------------|----------------------|
| POST | `/authors` | Create author | `{"name":"..."}` |
| GET | `/authors` | List all authors | — |
| GET | `/authors/{id}` | Get single author | — |
| DELETE | `/authors/{id}` | Remove author | — |
| POST | `/books` | Create book | `{"title":"...","author_id":x}` |
| GET | `/books` | List all books | — |
| GET | `/books/{id}` | Get single book | — |
| PUT | `/books/{id}` | Update title only | `?title=newTitle` |
| DELETE | `/books/{id}` | Delete book | — |

All responses are JSON.  
Errors return `{ "detail": "..." }` with proper HTTP status codes (404, 422, etc.).

---

## 🗃️ Database Schema (SQLite)

**authors**  
- id : INTEGER PK  
- name : TEXT NOT NULL  

**books**  
- id : INTEGER PK  
- title : TEXT NOT NULL  
- author_id : INTEGER FK → authors.id  

Relationships enforced by SQLAlchemy & foreign-key constraints.

---

## 🧹 Stop / Reset

| Task | Command |
|------|---------|
| Stop server | `Ctrl + C` |
| Delete DB & start fresh | `del library.db` (Windows) or `rm library.db` (macOS/Linux) then restart server |

---

## ✅ Submission Checklist

- [ ] Entire folder pushed to **your** GitHub repo  
- [ ] `requirements.txt` present → one-command install  
- [ ] `README.md` (this file) present → shows how to run + sample calls  
- [ ] Screenshot / link to Swagger docs included (optional but nice)

That’s it—happy coding!