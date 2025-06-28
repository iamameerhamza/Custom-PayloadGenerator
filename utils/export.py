import json
import pyperclip

def export_payloads(payloads, filename):
    """
    Export payloads to a file.
    Supports .txt (plain text) and .json formats.
    """
    if filename.endswith(".json"):
        with open(filename, "w") as f:
            json.dump(payloads, f, indent=2)
    else:  # Default to .txt
        with open(filename, "w") as f:
            for payload in payloads:
                f.write(payload + "\n")

def copy_to_clipboard(payloads):
    """
    Copy all payloads to the clipboard, separated by newlines.
    """
    combined = "\n".join(payloads)
    pyperclip.copy(combined)
