
import argparse
from modules import xss
from modules import sqli
from modules import cmdi
from utils import ENCODER_MAP, export, obfuscation
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
    group.add_argument('--sqli-type', choices=['all', 'auth', 'union', 'error', 'bool', 'time'], help='SQLi payload category (default: all)')
    group.add_argument('--sqli-evasion', action='store_true', help='Apply evasion techniques to SQLi payloads')
    group.add_argument('--cmdi', action='store_true', help='Generate Command Injection payloads')

    # Processing Options
    group2 = parser.add_argument_group("Payload Processing Options")
    group2.add_argument('--encode', choices=['base64', 'url', 'hex', 'unicode'], help='Encoding method')
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
        payloads.extend(xss.get_all_payloads())

    if args.sqli:
        print("- SQLi Payload Generation enabled")
        
        if args.sqli_type and args.sqli_type != "all":
            payloads.extend(sqli.get_payloads_by_type(args.sqli_type, evasion=args.sqli_evasion))
        else:
            payloads.extend(sqli.get_all_payloads(evasion=args.sqli_evasion))

    if args.cmdi:
        print("- Command Injection Payload Generation enabled")
        payloads.extend(cmdi.get_all_payloads())

    if args.encode:
        print(f"- Encoding: {args.encode}")
        encoder_func = ENCODER_MAP.get(args.encode)
        if encoder_func:
            payloads = [encoder_func(p) for p in payloads]


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
