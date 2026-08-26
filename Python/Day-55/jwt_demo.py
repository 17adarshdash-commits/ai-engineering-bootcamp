"""
Day 55 - JWT Structure Demo

Goal: get hands-on with encoding/decoding a JWT using PyJWT, see the
three-part structure, and observe what happens when a token is tampered
with.

Install:
    pip install PyJWT

Run:
    python jwt_demo.py

Important: this is a *structural* demo, not production auth. Never put
passwords or other secrets inside a JWT payload - the payload is only
base64-encoded, not encrypted, so anyone holding the token can read it.
"""

import jwt

# In a real app this would be a long, random value pulled from an
# environment variable - never hardcoded or committed like this.
SECRET_KEY = "day55-demo-secret-key-not-for-production-use"
ALGORITHM = "HS256"


def create_token(payload: dict) -> str:
    """Encode a payload into a signed JWT."""
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    """Verify the signature and return the payload's claims."""
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


def main():
    # 1. Create a payload (claims about who this token represents).
    payload = {
        "sub": "admin",
        "role": "user",
    }
    print("Payload:", payload)

    # 2. Encode it into a token.
    token = create_token(payload)
    print("\nEncoded JWT:")
    print(token)

    # 3. Look at the three dot-separated parts.
    header_b64, payload_b64, signature_b64 = token.split(".")
    print("\nThree parts:")
    print("  Header (base64):   ", header_b64)
    print("  Payload (base64):  ", payload_b64)
    print("  Signature (base64):", signature_b64)

    # jwt.get_unverified_header() decodes the header without checking
    # the signature - useful for inspection, never for trust decisions.
    print("\nDecoded header:", jwt.get_unverified_header(token))

    # 4. Decode + verify it.
    decoded = decode_token(token)
    print("\nDecoded + verified payload:", decoded)

    # 5. Tamper with the token and see what happens.
    print("\n--- Tampering test ---")
    tampered_token = token[:-4] + "abcd"  # corrupt the last few chars of the signature
    try:
        decode_token(tampered_token)
        print("Tampered token was accepted (this shouldn't happen!)")
    except jwt.InvalidSignatureError:
        print("Tampered token rejected: signature verification failed.")

    # 6. Also try decoding with the wrong secret key.
    print("\n--- Wrong secret key test ---")
    try:
        jwt.decode(token, "not-the-real-secret", algorithms=[ALGORITHM])
        print("Token decoded with wrong key (this shouldn't happen!)")
    except jwt.InvalidSignatureError:
        print("Rejected: wrong secret key can't reproduce the signature.")


if __name__ == "__main__":
    main()
