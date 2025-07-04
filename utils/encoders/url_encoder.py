import urllib.parse

def encode(payload: str) -> str:
    return urllib.parse.quote(payload)
