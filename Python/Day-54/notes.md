# Day 54 — Authentication Basics + Dependency Injection

## 1. Authentication vs. Authorization

**Authentication** answers *"Who are you?"* — it verifies identity.
When a client sends an API key, a username/password pair, or a bearer
token, the server checks that credential and decides: is this a
request from someone/something it recognizes at all?

**Authorization** answers *"What are you allowed to do?"* — it comes
*after* authentication and checks permissions for an already-identified
caller. Being authenticated doesn't automatically mean being
authorized for every action.

Example:

```
Authentication: "Is this request carrying a valid API key?"
Authorization:  "Does the holder of this key have permission to
                  delete this resource?"
```

A request can fail authentication (no valid credential at all - who
even is this?) or pass authentication but fail authorization (we know
who you are, but you can't do that). Today's exercises only deal with
authentication - there's no notion of roles/permissions gating actions
yet.

## 2. API Keys

A simple, static secret string the client includes with each request
to prove it's allowed to call the API. The server holds a copy (or a
set of valid keys) and compares. No cryptographic signing, no
expiration, no encoded claims - just "does this string match a known
value?" That simplicity is also the weakness: a leaked key is valid
forever until manually revoked. Fine for internal tools, demos, and
service-to-service calls; not what you'd use for end-user login at
scale.

## 3. Bearer Tokens

A `Bearer` token is a credential presented as *"whoever bears
(possesses) this token is granted access"* - no additional proof of
identity is required beyond having the token itself. It's a delivery
convention more than a token format: the token could be a random
opaque string, a session ID, or (later) a JWT that encodes claims
(user id, expiry, roles) in a signed, self-contained way. Today's
`auth_demo.py` uses a hardcoded string as a stand-in bearer token -
the same flow JWTs use later, just without the signing/decoding step.

## 4. The `Authorization` Header

The standard HTTP header for sending credentials. Its value is
typically `<scheme> <credentials>`:

```
Authorization: Bearer sk-demo-12345
```

`Bearer` here is the *scheme* (there's also `Basic` for
base64-encoded username:password, etc.). FastAPI can read this header
directly with `Header(...)`, or use its built-in
`fastapi.security` helpers (`HTTPBearer`, `APIKeyHeader`, ...) which
parse the scheme for you and raise a clean 401/403 if it's missing or
malformed.

## 5. `Depends()` for Auth

`Depends()` isn't just for injecting shared logic (DB sessions,
pagination params) - it's the natural place to put an auth check,
because a dependency runs *before* the route body and can short-circuit
the request by raising an `HTTPException`. That keeps the route
function itself free of auth boilerplate: if the dependency didn't
raise, the caller is authenticated by the time the route body runs.

```python
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key

@app.get("/protected")
def protected_route(api_key: str = Depends(verify_api_key)):
    return {"message": "You have access"}
```

If the header is missing entirely, FastAPI itself returns a `422`
(the declared parameter is required and absent) before the dependency
even runs; if it's present but wrong, the dependency raises the `401`.

## 6. Protected vs. Public Endpoints

A **public** endpoint has no `Depends(verify_...)` in its signature -
anyone can call it, no credential needed. A **protected** endpoint
declares the auth dependency as a parameter, so FastAPI resolves it
(running the check) before the route body executes. The only
difference in the route's code is that one extra parameter - the
protection is entirely declarative, not something the route function
has to remember to check itself.

## 7. Today's Three Test Cases

For `/protected` (and later `/profile`):

| Request                          | Result           |
|-----------------------------------|------------------|
| No `Authorization` / no API key   | `401/422`        |
| Wrong key                         | `401 Unauthorized` |
| Correct key                       | `200 OK`         |

## 8. Key Takeaways

- Authentication = identity check; authorization = permission check.
  Today is authentication only.
- API keys and bearer tokens are both just credentials sent with a
  request - the difference is convention/format, not concept.
- `Depends()` lets an auth check run *before* the route body and
  short-circuit with an `HTTPException`, keeping routes themselves
  auth-agnostic.
- Hardcoding a secret key/credentials is only acceptable for today's
  learning exercise - never for anything real. Real systems hash
  passwords, rotate keys, and use signed/expiring tokens (JWT, OAuth).
