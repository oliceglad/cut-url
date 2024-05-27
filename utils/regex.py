from common.regex_rules import URL_REGEX, CONSONANTS_REGEX

def is_valid_url(url):
    return URL_REGEX.match(url) is not None

def extract_consonants(text):
    return ''.join(CONSONANTS_REGEX.findall(text))
