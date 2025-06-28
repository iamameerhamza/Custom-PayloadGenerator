import random
import re

def obfuscate(payload):
    """
    Apply random obfuscation technique to a payload.
    """
    techniques = [
        _add_comments,
        _case_randomization,
        _whitespace_manipulation,
        _character_encoding
    ]
    technique = random.choice(techniques)
    return technique(payload)

# Obfuscation Techniques

def _add_comments(payload):
    """
    Randomly insert comments into HTML tags.
    """
    return re.sub(r'(<[^>]+)', r'\1/*{}*/'.format(_random_string(4)), payload)

def _case_randomization(payload):
    """
    Randomize casing of HTML tags and attributes.
    """
    def random_case(match):
        return ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in match.group(0))
    
    return re.sub(r'<[^>]+>', random_case, payload)

def _whitespace_manipulation(payload):
    """
    Insert random whitespace characters.
    """
    return payload.replace(' ', random.choice([' ', '\t', '/**/', '\n']))

def _character_encoding(payload):
    """
    Replace specific characters with HTML entity equivalents.
    """
    encodings = {
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;',
    }
    return ''.join(encodings.get(c, c) for c in payload)

# Helper

def _random_string(length):
    """
    Generate a random alphanumeric string of given length.
    """
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=length))
