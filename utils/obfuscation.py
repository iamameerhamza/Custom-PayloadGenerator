import random
import re

# List of common keywords attackers may try to bypass filters for
KEYWORDS = ['script', 'alert', 'onerror', 'img', 'svg', 'iframe']

def obfuscate(payload):
    """
    Apply layered obfuscation to a payload:
    - Keyword splitting
    - Comment injection
    - Random case switching
    - Random whitespace manipulation
    - Character encoding
    """
    payload = _split_keywords(payload, KEYWORDS)
    payload = _add_comments(payload)
    payload = _random_case(payload)
    payload = _whitespace_manipulation(payload)
    payload = _character_encoding(payload)
    return payload


# Obfuscation Techniques

def _split_keywords(payload, keywords):
    """
    Split keywords by injecting random characters or comments.
    """
    for kw in keywords:
        if kw.lower() in payload.lower():
            injection = random.choice(['/**/', '%20', '', '\t'])
            parts = list(kw)
            obfuscated_kw = injection.join(parts)
            pattern = re.compile(re.escape(kw), re.IGNORECASE)
            payload = pattern.sub(obfuscated_kw, payload)
    return payload

def _add_comments(payload):
    """
    Randomly insert comments inside HTML tags.
    """
    return re.sub(r'(<[^>]+)', lambda m: m.group(1) + f'/*{_random_string(4)}*/', payload)

def _random_case(payload):
    """
    Randomize casing of characters within tags and payload.
    """
    return ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in payload)

def _whitespace_manipulation(payload):
    """
    Insert random whitespace characters throughout the payload.
    """
    return payload.replace(' ', random.choice([' ', '\t', '/**/', '\n']))

def _character_encoding(payload):
    """
    Replace key characters with HTML entity equivalents.
    """
    encodings = {
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;',
    }
    return ''.join(encodings.get(c, c) for c in payload)


# Helper Function

def _random_string(length):
    """
    Generate a random alphanumeric string of given length.
    """
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=length))
