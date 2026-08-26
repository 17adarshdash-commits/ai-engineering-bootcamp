# Day 55 — JWT Concepts + SQLAlchemy Introduction

## 1. What is a JWT?

A **JSON Web Token (JWT)** is a compact, URL-safe token used to represent
authenticated user information as it moves between a client and a server.
Instead of the server keeping session state in memory (or a database) for
every logged-in user, it hands the client a signed token containing the
claims it needs, and the client presents that token on every subsequent
request.

### Structure: `header.payload.signature`

A JWT is three base64url-encoded segments joined by dots:

```
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiJ9.4pcPyMD1t...
└──── header ────┘ └──── payload ────┘ └─ signature ─┘
```

- **Header** — metadata about the token itself: token type (`JWT`) and
  the signing algorithm (e.g. `HS256`).
- **Payload** — the claims: arbitrary key/value data about the subject
  (`sub`, `role`, expiry, etc.). This is just base64-encoded JSON — **not
  encrypted**, so anyone holding the token can read it.
- **Signature** — computed by signing `header + "." + payload` with a
  secret key (HS256) or a private key (RS256). The server recomputes
  this signature on every request and compares it to the one on the
  token; if they don't match, the token has been tampered with (or
  forged) and is rejected.

## 2. Authentication flow with JWT

```
User
 |
 v
POST /login (username + password)
 |
 v
Server verifies credentials
 |
 v
JWT generated (signed with server's secret)
 |
 v
Client stores token (e.g. in memory, local storage)
 |
 v
Client sends token with requests
   Authorization: Bearer <token>
 |
 v
Server verifies token's signature + expiry
 |
 v
Protected endpoint runs, using claims from the payload
```

Key point: the server does not need to look anything up to "remember"
who's logged in — the signature alone proves the payload is authentic
and untampered, so the token is self-contained (stateless auth).

## 3. Important: JWTs are encoded, not encrypted

Because the payload is just base64, **never put passwords, secrets, or
sensitive personal data in a JWT payload.** Anyone can decode it and read
it without the signing key — the signature only prevents *modification*,
not *reading*.

## 4. SQLAlchemy / ORM concepts

**ORM (Object Relational Mapping)** lets you work with Python objects
that represent database rows, instead of writing raw SQL:

```
SELECT * FROM users;      -->      session.query(User).all()
```

### The hierarchy

```
Database
   |
   v
Table
   |
   v
Row
   |
   v
Column
```

### How SQLAlchemy maps this to Python

```
SQLAlchemy
    |
    v
Python classes  <-->  Database tables
```

Core building blocks used today:

- **Engine** — the entry point to the database; holds the connection
  info (e.g. `sqlite:///students.db`) and knows how to talk to it.
- **Model** — a Python class (subclassing `Base`) whose attributes map
  to table columns. One model = one table.
- **Table** — the actual database table a model maps to (declared via
  `__tablename__` on the model).
- **Column** — a single field on the table (`id`, `name`, etc.), with a
  type (`Integer`, `String`, `Float`, ...).
- **Primary key** — the column that uniquely identifies each row
  (`id`, marked with `primary_key=True`).
- **Session** — the workspace for talking to the database: add objects,
  query them, commit changes, roll back on error. Roughly one session
  per unit of work (e.g. per request in a real app).

### The flow

```
Python
  |
  v
SQLAlchemy (ORM layer)
  |
  v
SQLite (actual database file on disk)
```

Not covered today: relationships between tables (foreign keys,
`relationship()`), migrations (Alembic), connection pooling — those come
once the basics (CRUD on a single table) are solid.

## 5. LeetCode: 322. Coin Change

Already solved on Day 43
([`DSA/DynamicProgramming/LC322_coin_change.py`](../../DSA/DynamicProgramming/LC322_coin_change.py))
as part of an earlier SQL-focused day that also included a DP problem.
Reviewed today rather than re-solved — the DP state is:

```
dp[a] = fewest coins to make amount a
dp[0] = 0
dp[a] = min(dp[a], 1 + dp[a - coin]) for every coin <= a
```

Same "try every choice, keep the best" tabulation shape as House Robber
/ Min Cost Climbing Stairs, except the choice is *which coin* rather
than a single binary include/exclude decision.
