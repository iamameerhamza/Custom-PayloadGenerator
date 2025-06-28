import json
import pyperclip
import os
import datetime

def export_payloads(payloads, filename=None):
    """
    Export payloads to a file.
    Supports .txt and .json formats.
    Adds timestamp to filename if not provided.
    Saves to 'samples/' folder by default.
    """
    if not payloads:
        print("[!] No payloads to export.")
        return

    # Ensure samples directory exists
    os.makedirs("samples", exist_ok=True)

    # Auto-generate filename if not provided
    if not filename:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"samples/payloads_{timestamp}.txt"

    # Prepend samples/ if filename has no path
    if not os.path.dirname(filename):
        filename = os.path.join("samples", filename)

    # Ensure correct extension
    if filename.endswith(".json"):
        with open(filename, "w") as f:
            json.dump(payloads, f, indent=2)
        print(f"[+] Payloads exported to {filename} (JSON format)")
    else:  # Default to .txt
        with open(filename, "w") as f:
            f.write("\n".join(payloads))
        print(f"[+] Payloads exported to {filename} (Text format)")

def copy_to_clipboard(payloads):
    """
    Copy all payloads to the clipboard, separated by newlines.
    """
    if not payloads:
        print("[!] No payloads to copy.")
        return

    combined = "\n".join(payloads)
    pyperclip.copy(combined)
    print("[+] Payloads copied to clipboard.")
