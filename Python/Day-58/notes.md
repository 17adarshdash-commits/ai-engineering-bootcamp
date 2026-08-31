# Day 58 — SQLAlchemy Relationships (One-to-Many)

## 1. Foreign key

A foreign key is a column that stores the primary key of a row in
another table - it's how one table points at another.

```
users
----------------
id
name
email


posts
----------------
id
title
content
user_id  <- foreign key
```

`posts.user_id` doesn't duplicate the user's data (name, email); it
just stores the `id` of the user that post belongs to. That single
column is what connects a post back to a specific user - everything
else about the user is looked up through the join, not copied.

## 2. Why relational databases use separate tables

If every post carried the author's name and email directly instead of
a `user_id`, updating one user's email would mean rewriting every post
row they ever created, and nothing would stop two posts from
disagreeing about the same person's email. Splitting `users` and
`posts` into separate tables means each fact is stored exactly once
(the user's email lives only in `users`), and the foreign key is the
single link that ties a post to its author. This is the same principle
Day 56/57 touched on with normalization - one source of truth per
fact, connected by keys instead of duplicated by copy.

## 3. One-to-many

```
ONE USER
   |
   +-- POST 1
   +-- POST 2
   +-- POST 3
```

One user can own many posts, but each post belongs to exactly one
user. This is the most common relationship shape in relational data -
"one parent, many children" - and it's what `user_id` on the `posts`
table encodes: many rows in `posts` can share the same `user_id`, but
each row has only one.

## 4. `relationship()` and `back_populates`

The foreign key column (`user_id`) is what the database understands.
`relationship()` is what *Python* understands - it lets SQLAlchemy
objects navigate the link without writing manual joins:

```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)

    posts = relationship("Post", back_populates="author")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    author = relationship("User", back_populates="posts")
```

- `user_id = Column(Integer, ForeignKey("users.id"))` is the real
  database-level link - the actual column SQLite stores.
- `posts = relationship("Post", back_populates="author")` on `User`
  lets you write `user.posts` to get every `Post` row with that
  user's `id` as `user_id`, without writing a query by hand.
- `author = relationship("User", back_populates="posts")` on `Post`
  is the mirror image - `post.author` gives back the `User` object
  that post belongs to.
- `back_populates` is what keeps the two sides in sync: it tells each
  `relationship()` which attribute on the *other* class is its
  counterpart, so `relationship()` knows `User.posts` and
  `Post.author` describe the same link from opposite directions.

The foreign key is required (it's what SQL actually enforces);
`relationship()` is a convenience layer on top that turns that column
into attribute-style navigation (`user.posts`, `post.author`) instead
of manual `db.query(Post).filter(Post.user_id == user.id)` calls.

## 5. Practice: `relationship_practice/`

Built a minimal `User` <-> `Post` one-to-many pair to exercise the
concepts above before applying them in the mini project:

- `database.py` - engine, `SessionLocal`, `Base`, same reusable shape
  as Day 55/56.
- `models.py` - `User` and `Post` models linked by `user_id` +
  `relationship()`/`back_populates` on both sides.
- `main.py` - creates one user, creates several posts for that user,
  then reads the relationship both directions: `user.posts` (a
  user's posts) and `post.author` (a post's author).

## 6. LeetCode: 1143. Longest Common Subsequence (retention)

File: [`DSA/DynamicProgramming/LC1143_longest_common_subsequence.py`](../../DSA/DynamicProgramming/LC1143_longest_common_subsequence.py)

Retention day - no new problem. Re-derived the solution from memory
instead of rereading it first:

- `dp[i][j]` = length of the LCS between `text1[:i]` and `text2[:j]`
  (the first `i` characters of `text1`, first `j` of `text2`). Row 0
  and column 0 are 0, since the LCS of anything with an empty prefix
  is empty.
- If `text1[i-1] == text2[j-1]`: the matching character extends
  whatever LCS already existed one step back on *both* strings, so
  `dp[i][j] = dp[i-1][j-1] + 1` - both pointers retreat past the
  matched pair, plus 1 for the match itself.
- If they don't match: the current pair of last characters can't both
  be in the LCS together, so try dropping one side at a time and keep
  the better result: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.
  - `dp[i-1][j]` = best LCS if `text1`'s last character is dropped
    (kept `text2` as-is).
  - `dp[i][j-1]` = best LCS if `text2`'s last character is dropped
    (kept `text1` as-is).
  - Taking the max instead of picking one is what guarantees the
    optimal answer - dropping the "wrong" side first is still
    reachable through a later cell, so nothing is lost by trying
    both.
- Answer is `dp[m][n]`, the bottom-right cell, since that's the LCS
  over the *full* strings.

## 7. Mini project: `01_blog_api/`

A database-backed FastAPI blog with two related tables:

```
User 1 ----------< Many Posts
```

- `database.py` - engine, `SessionLocal`, `Base`, `get_db()`.
- `models.py` - `User` and `Post` SQLAlchemy models, linked by
  `user_id` (`ForeignKey`) + `relationship()`/`back_populates`.
- `schemas.py` - Pydantic request/response shapes, kept separate from
  the SQLAlchemy models (same split as Day 56/57).
- `main.py` - `/users` and `/posts` CRUD, plus `GET /users/{id}/posts`
  to read a user's posts through the relationship.

See [`01_blog_api/README.md`](01_blog_api/README.md) for the full
endpoint list and how to run it.
