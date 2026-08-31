# Day 60 — Authentication Foundations: Password Hashing + JWT

## 1. Authentication vs. Authorization

- **Authentication** = *who are you?* Proving identity - typically an
  email + password check that confirms "this really is Alice."
- **Authorization** = *what are you allowed to do?* A permissions check
  that runs *after* identity is established - e.g. "Alice is a normal
  user, only Admins can delete users."

Authentication always comes first: there's nothing to authorize until
the system knows who's asking. Today's project only covers
authentication (login + a protected route); it doesn't add roles or
permission levels.

## 2. Password hashing

Passwords must never be stored as plain text - if the database ever
leaks, plain-text passwords leak directly, and because people reuse
passwords, that leak compromises accounts on other sites too.

Instead, a **hash function** turns the password into a fixed-size,
one-way fingerprint before it's stored:

```
password -> hash function -> stored password hash
```

At login, the entered password is hashed again and compared to the
stored hash - the plain password itself is never saved anywhere, only
re-derived in memory for the instant it takes to check it.

## 3. Password verification

```
entered password -> verify against stored hash -> correct?
```

Today's project uses `bcrypt` directly (`hashpw` / `checkpw`) rather
than `passlib`: `passlib` is effectively unmaintained and breaks on
recent `bcrypt` releases, and current FastAPI guidance points at using
`bcrypt`/`pwdlib` directly instead. `bcrypt` also salts every hash
automatically, so two users with the same password end up with
different stored hashes.

## 4. Hash vs. encryption

- **Encryption** is reversible: given the right key, ciphertext can be
  decrypted back into the original plaintext. Used when the original
  value needs to be recovered later.
- **Hashing** is one-way: there's no key that turns a hash back into
  the original password. Verification works by hashing the *new* input
  and comparing hashes, never by "decrypting" the stored one.

Passwords are hashed, never encrypted, because the system should never
need (or be able) to recover the original password at all.

## 5. JWT (JSON Web Token)

A JWT is a signed, three-part token (`header.payload.signature`) that
encodes claims about a user - e.g. `sub` (the subject/identity) and
`exp` (expiry). It's created once at login and handed to the client to
present on later requests, so the server doesn't have to look up a
session on every call.

Important: the payload is base64-encoded, **not encrypted** - anyone
holding the token can read its contents. Only the signature is
protected, which is why nothing sensitive (passwords, hashes) ever
goes inside a JWT payload - see Day 55's `jwt_demo.py` for a hands-on
look at the three parts and what happens when a token is tampered
with.

## 6. Access token

The JWT issued after a successful login. It's short-lived (30 minutes
in today's project) and self-contained: verifying it only requires the
server's secret key, no database session lookup. No refresh tokens
today - once it expires, the client just logs in again.

## 7. Bearer token

The convention for sending the access token on later requests:

```
Authorization: Bearer <token>
```

"Bearer" means whoever holds ("bears") the token is treated as
authenticated - there's no additional proof of identity beyond
possessing a valid, unexpired, correctly-signed token. This is why
tokens must be transmitted over HTTPS in production and never logged.

## 8. Protected endpoint

A route that requires a valid token before it runs. In FastAPI this is
a dependency (`get_current_user`) that:

1. Reads the `Authorization: Bearer <token>` header.
2. Decodes + verifies the JWT's signature and expiry.
3. Loads the user the token's `sub` claim identifies.
4. Raises `401 Unauthorized` if any step fails - missing header, bad
   signature, expired token, or a user that no longer exists.

Only if all four steps succeed does the route body ever execute.

## 9. The full flow

```
REGISTER
   |
   v
Hash Password
   |
   v
Database


LOGIN
   |
   v
Verify Password
   |
   v
Create JWT
   |
   v
Client


REQUEST
   |
   v
JWT
   |
   v
Verify Token
   |
   v
Protected Route
```

## 10. Mini project: `01_auth_api/`

A minimal `User` model (`id`, `name`, `email`, `password_hash` - no
plain `password` column, ever) with three routes:

- `POST /register` - hashes the password with `bcrypt`, stores the
  user, returns the user *without* the hash.
- `POST /login` - verifies the password against the stored hash,
  returns a signed JWT (`access_token`) on success.
- `GET /profile` - protected by the `get_current_user` dependency;
  returns the current user only when a valid bearer token is supplied,
  otherwise 401.

See [`01_auth_api/README.md`](01_auth_api/README.md) for the full
endpoint list and how to run it.

## 11. LeetCode: 198. House Robber

File: [`DSA/DynamicProgramming/LC198_house_robber.py`](../../DSA/DynamicProgramming/LC198_house_robber.py)

At every house there are exactly two mutually exclusive choices:

- **skip** house `i` -> best total is whatever was already best through
  house `i-1`.
- **rob** house `i` -> house `i-1` must be left alone, so best total is
  `nums[i] + best through house i-2`.

```
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

Since `dp[i]` only ever needs the previous two values, it collapses
into two rolling variables (`prev2`, `prev1`) instead of a full `dp`
array - the same shape as Fibonacci.

- `prev2, prev1 = 0, nums[0]`
- for each remaining `money`: `current = max(prev1, prev2 + money)`,
  then slide the window: `prev2, prev1 = prev1, current`.
- Return `prev1`.
- O(n) time, O(1) space.
