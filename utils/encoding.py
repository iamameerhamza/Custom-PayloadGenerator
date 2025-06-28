import base64
import urllib.parse

def apply_encoding(payload, method):
    """
    Apply encoding to a payload.
    Supported methods: base64, url, hex
    """
    if method == 'base64':
        return base64.b64encode(payload.encode()).decode()
    elif method == 'url':
        return urllib.parse.quote(payload)
    elif method == 'hex':
        return payload.encode().hex()
    return payload  # Return unchanged if method is invalid or None
