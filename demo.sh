#!/bin/bash

# Payload Generator Demo Script

show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --xss                   Generate XSS payloads"
    echo "  --sqli                  Generate SQLi payloads"
    echo "  --sqli-type [TYPE]      SQLi category: all, auth, union, error, bool, time"
    echo "  --sqli-evasion          Apply SQLi evasion techniques"
    echo "  --cmdi                  Generate Command Injection payloads"
    echo "  --encode [TYPE]         Encoding: base64, url, hex, unicode"
    echo "  --obfuscate             Apply layered obfuscation"
    echo "  --output [FILE]         Save payloads to file (.txt or .json)"
    echo "  --clipboard             Copy payloads to clipboard"
    echo "  --check-all             Run quick check for all major modules"
    echo "  --help                  Show this help message"
}

if [[ $# -eq 0 ]]; then
    show_help
    exit 1
fi

if [[ "$1" == "--check-all" ]]; then
    echo "[*] Running full tool functionality check..."
    
    echo "[+] Testing XSS payloads..."
    python3 payload_gen.py --xss || { echo "[✖] XSS payload test failed."; exit 1; }

    echo "[+] Testing SQLi payloads with evasion..."
    python3 payload_gen.py --sqli --sqli-type union --sqli-evasion || { echo "[✖] SQLi payload test failed."; exit 1; }

    echo "[+] Testing CMDi payloads with encoding..."
    python3 payload_gen.py --cmdi --encode hex || { echo "[✖] CMDi payload test failed."; exit 1; }

    echo "[+] Testing XSS payloads with obfuscation..."
    python3 payload_gen.py --xss --obfuscate || { echo "[✖] XSS obfuscation test failed."; exit 1; }

    echo "[✔] All core modules ran successfully!"
    exit 0
fi

# Forward all other arguments directly to payload_gen.py
python3 payload_gen.py "$@"
