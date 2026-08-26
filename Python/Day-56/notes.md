# Day 56 — SQLAlchemy + FastAPI Database Integration (Light)

## 1. Database session

A **session** is the interface an application uses to talk to the
database - it's the workspace where objects get added, queried,
updated, and where changes are staged until `commit()` writes them to
disk (or `rollback()` discards them).

```
FastAPI Request
      |
      v
Route
      |
      v
Database Session
      |
      v
SQLAlchemy
      |
      v
SQLite
```

In FastAPI, the session is handed to a route as a dependency
(`Depends(get_db)`). `get_db()` yields one `Session` per request and
always closes it afterwards, even if the route raises - this is the
piece that connects Day 55's standalone SQLAlchemy script to a real
API: instead of one long-lived session for the whole program, each
request gets its own short-lived one.

## 2. SQLAlchemy model

A Python class maps to a database table. Each class attribute is a
`Column`, and each instance of the class is a row.

```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    age = Column(Integer, nullable=False)
```

`Base` (from `declarative_base()`) is what SQLAlchemy uses to track
every model and turn it into real `CREATE TABLE` statements via
`Base.metadata.create_all(bind=engine)`.

## 3. CRUD

The four operations every backend route boils down to:

| Letter | Operation | HTTP verb | SQLAlchemy call        |
|--------|-----------|-----------|-------------------------|
| C      | Create    | POST      | `db.add()` + `db.commit()` |
| R      | Read      | GET       | `db.query()` / `db.get()`  |
| U      | Update    | PUT/PATCH | mutate + `db.commit()`     |
| D      | Delete    | DELETE    | `db.delete()` + `db.commit()` |

Today's mini project covers C, R, D (Create, Read, Delete) - Update is
the natural next endpoint to add (`PUT /users/{id}`), skipped today to
stay inside the time box.

## 4. Mini project: `database_demo/`

Built a `User` API (`id`, `name`, `email`, `age`) backed by a real
SQLite file instead of an in-memory list, same structure as Day 55's
`01_student_database/`:

- `database.py` - engine, `SessionLocal`, `Base`, `get_db()` dependency.
- `models.py` - the `User` table model + `UserCreate` / `UserOut`
  Pydantic schemas (DB-facing shape kept separate from API-facing
  shape).
- `main.py` - `POST /users`, `GET /users`, `GET /users/{id}`,
  `DELETE /users/{id}`.

The key difference from Day 51-53's list-based APIs: every route now
depends on `db: Session = Depends(get_db)` and talks to `users.db` on
disk, so data survives a server restart.

## 5. LeetCode: 300. Longest Increasing Subsequence

File: [`DSA/DynamicProgramming/LC300_longest_increasing_subsequence.py`](../../DSA/DynamicProgramming/LC300_longest_increasing_subsequence.py)

Pattern: 1D DP, same "look back at every earlier sub-problem and keep
the best" shape as Coin Change (Day 55) - here the state is:

```
dp[i] = length of the longest increasing subsequence ending at index i
dp[i] = 1                              (nums[i] alone)
dp[i] = max(dp[i], dp[j] + 1)          for every j < i where nums[j] < nums[i]
answer = max(dp)                       (best subsequence can end anywhere)
```

O(n^2) time, O(n) space. The O(n log n) binary-search-over-tails
solution is a later refinement, not today's goal.
