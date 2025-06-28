
# 🚀 Web Exploit Payload Generator (One-File Edition)

A standalone, evasion-ready payload generation tool for common web vulnerabilities:

✅ Cross-Site Scripting (XSS)  
✅ SQL Injection (SQLi)  
✅ Command Injection (CMDi)  
✅ Encoding & Obfuscation for bypass techniques  

---

## ⚒️ **Features**

- One clean, editable `.py` file — no folder structure needed  
- Evasion-ready payloads with bypass techniques  
- Supports Base64, URL, and Hex encoding  
- Randomized obfuscation to evade filters  
- Outputs to terminal, `.txt`, or `.json` files  
- Copy payloads to clipboard  
- Auto-generates filenames with timestamps  

---

## 🚀 **Quick Start**

### **Requirements**

- Python 3.x  
- `pyperclip` library  

```bash
pip install pyperclip
```

---

## 🖥️ **Usage**

```bash
python3 payload_generator.py [--xss|--sqli|--cmdi] [--encode base64|url|hex] [--obfuscate] [--output [FILENAME]] [--clipboard]
```

---

## 📦 **Examples**

### Generate XSS payloads:

```bash
python3 payload_generator.py --xss
```

### Generate SQLi payloads with URL encoding, save to file:

```bash
python3 payload_generator.py --sqli --encode url --output sqli_encoded.txt
```

### Command Injection payloads, copied to clipboard:

```bash
python3 payload_generator.py --cmdi --clipboard
```

### Full payload generation with encoding, obfuscation, and auto-saved file:

```bash
python3 payload_generator.py --xss --sqli --cmdi --encode base64 --obfuscate --output
```

---

## 📂 **Output Behavior**

- `--output [FILENAME]` → Saves to provided filename  
- `--output` alone → Auto-generates timestamped filename in `samples/` folder  
- `--clipboard` → Copies payloads to clipboard  
- Default → Prints payloads to terminal  

---

## 📚 **References**

- [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)  
- [PortSwigger XSS Filter Evasion Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)  
- [OWASP Command Injection](https://owasp.org/www-community/attacks/Command_Injection)  

---

## ⚠️ **Disclaimer**

For educational and authorized testing only. Use responsibly.

---
## 🙌 **Credits**
Created with ❤️ by **TEAM NEBULA**
*Part of internship red team project*

---
