def encode(payload: str) -> str:
    return ''.join(f"\\u{ord(c):04x}" for c in payload)
