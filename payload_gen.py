#!/usr/bin/env python3

import argparse
from modules import xss
from modules import sqli
from modules import cmdi
from utils import encoding
from utils import export  
from utils import obfuscation

def main():
    parser = argparse.ArgumentParser(
        description="Web Exploit Payload Generator - Modular Payload Creator for XSS, SQLi, and CMDi",
        epilog="Example: python payload_gen.py --xss --encode base64 --obfuscate --output payloads.txt"
    )

    # Payload Modules
    group = parser.add_argument_group("Payload Type Selection")
    group.add_argument('--xss', action='store_true', help='Generate XSS payloads')
    group.add_argument('--sqli', action='store_true', help='Generate SQLi payloads')
    group.add_argument('--cmdi', action='store_true', help='Generate Command Injection payloads')

    # Processing Options
    group2 = parser.add_argument_group("Payload Processing Options")
    group2.add_argument('--encode', choices=['base64', 'url', 'hex'], help='Encoding method')
    group2.add_argument('--obfuscate', action='store_true', help='Apply random obfuscation')

    # Output Options
    group3 = parser.add_argument_group("Output Options")
    group3.add_argument('--output', nargs='?', const=True, help='Output file (.txt or .json), auto-generate if omitted')
    group3.add_argument('--clipboard', action='store_true', help='Copy payloads to clipboard')

    args = parser.parse_args()

    # Basic feedback for testing
    print("Selected options:")

    payloads = []  # Initialize empty payload list

    if args.xss:
        print("- XSS Payload Generation enabled")
        payloads.extend(xss.generate_xss())

    if args.sqli:
        print("- SQLi Payload Generation enabled")
        payloads.extend(sqli.generate_sqli())

    if args.cmdi:
        print("- Command Injection Payload Generation enabled")
        payloads.extend(cmdi.generate_cmdi())

    if args.encode:
        print(f"- Encoding: {args.encode}")
        payloads = [encoding.apply_encoding(p, args.encode) for p in payloads]

    if args.obfuscate:
        print("- Obfuscation enabled")
        payloads = [obfuscation.obfuscate(p) for p in payloads]

    # Output handling
    output_target = args.output if isinstance(args.output, str) else None

    if args.output:
        export.export_payloads(payloads, output_target)
    elif args.clipboard:
        export.copy_to_clipboard(payloads)
    else:
        for p in payloads:
            print(p)

if __name__ == "__main__":
    main()
