import re

URL_REGEX = re.compile(r'^(https?://)?(www\.)?(\w+\.\w+)(/.*)?$')
CONSONANTS_REGEX = re.compile(r'[^aeiouAEIOU0-9\s\W_]', re.ASCII)
