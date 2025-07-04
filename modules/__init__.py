from . import xss, sqli, cmdi

MODULE_MAP = {
    'xss': xss.get_all_payloads,
    'sqli': sqli.get_all_payloads,
    'cmdi': cmdi.get_all_payloads
}
