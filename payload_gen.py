#!/usr/bin/env python3

import argparse
from modules import xss
from modules import sqli
from modules import cmdi
from utils import encoding

def main():
    parser = argparse.ArgumentParser(description="Web Exploit Payload Generator")

    # Module selection
    parser.add_argument('--xss', action='store_true', help='Generate XSS payloads')
    parser.add_argument('--sqli', action='store_true', help='Generate SQLi payloads')
    parser.add_argument('--cmdi', action='store_true', help='Generate Command Injection payloads')

    # Processing options (placeholders for now)
    parser.add_argument('--encode', choices=['base64', 'url', 'hex'], help='Encoding method')
    parser.add_argument('--obfuscate', action='store_true', help='Apply obfuscation')

    # Output options (placeholders for now)
    parser.add_argument('--output', help='Output file (txt/json)')
    parser.add_argument('--clipboard', action='store_true', help='Copy to clipboard')

    args = parser.parse_args()

    # Basic feedback for testing
    print("Selected options:")
    if args.xss:
        print("- XSS Payload Generation enabled")
        payloads = xss.generate_xss()
        for p in payloads:
            if args.encode:
                p = encoding.apply_encoding(p, args.encode)
            print(p)
    if args.sqli:
        print("- SQLi Payload Generation enabled")
        payloads = sqli.generate_sqli()
        for p in payloads:
            if args.encode:
                p = encoding.apply_encoding(p, args.encode)
            print(p)
    if args.cmdi:
        print("- Command Injection Payload Generation enabled")
        payloads = cmdi.generate_cmdi()
        for p in payloads:
            if args.encode:
                p = encoding.apply_encoding(p, args.encode)
            print(p)
    
    if args.obfuscate:
        print("- Obfuscation enabled")
    if args.output:
        print(f"- Output file: {args.output}")
    if args.clipboard:
        print("- Copy to clipboard enabled")

if __name__ == "__main__":
    main()
