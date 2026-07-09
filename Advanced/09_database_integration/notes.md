# Topic 9: Database Integration & ORMs in Python

Database integration is foundational for backend development. Python's PEP 249 defines the standard Database API Specification (DB-API) implemented by database drivers.

---

## 1. DB-API & SQLite (`sqlite3`)

SQLite is a self-contained, serverless, zero-configuration SQL database engine. Python ships with a built-in module `sqlite3` implementing DB-API 2.0.

### Core Workflow:
1. **Connection**: Connect to database file (or `:memory:` for RAM-only database).
2. **Cursor**: Obtain a cursor object to execute SQL commands and retrieve results.
3. **Execution**: Run SQL statements.
4. **Transactions**: Commit changes (`connection.commit()`) or rollback (`connection.rollback()`).
5. **Cleanup**: Close cursor and connection.

```python
import sqlite3
conn = sqlite3.connect('app.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (id INT, name TEXT)')
conn.commit()
conn.close()
```

---

## 2. Preventing SQL Injection

> [!CAUTION]
> Never format strings directly into SQL queries (e.g. `f"SELECT * FROM users WHERE name='{name}'"`). This allows **SQL Injection Attacks**.

Always use **parameterized queries** where variables are bound to placeholders (`?` or `:name`).
```python
# Safe Parameterized execution
cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
```

---

## 3. Object-Relational Mappings (ORMs)

An ORM maps database tables to object-oriented classes.

### Benefits:
- Abstracts SQL queries away behind Pythonic method calls.
- Simplifies schema generation and model validation.
- Prevents SQL Injection by default via parameterized database interactions.

### Standard Python ORMs:
- **SQLAlchemy**: The most popular, comprehensive, and powerful SQL toolkit and ORM for Python.
- **Django ORM**: Built-in ORM of the Django web framework.
- **Peewee**: A lightweight, simple ORM.
