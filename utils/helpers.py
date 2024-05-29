import random
import string
from common import messages
from utils import regex, storage, url_request
from logger.logger_config import logger
def _split(text_):
    word = []
    t = []
    if "https" in text_:
        text_ = text_[5:]
    else:
        text_ = text_[4:]
    for i in text_:
        if i == '.':
            word.append(''.join(t))
            t = []
        else:
            t.append(i)
    if t:
        word.append(''.join(t))
    return word

def generate_short_url(full_url):
    print(full_url, _split(full_url))
    domain, zone = _split(full_url)[0], _split(full_url)[1]
    consonants_only = regex.extract_consonants(domain)
    short_url = f"{consonants_only}.{zone}"
    return short_url


def register_url():
    full_url = input(messages.REGISTER_PROMPT).lower()
    if not regex.is_valid_url(full_url):
        logger.error("Invalid URL format")
        print("Неверный формат URL")
        return

    alias = full_url
    short_url = generate_short_url(alias)
    short_url = short_url
    storage.add_url_mapping(short_url, full_url, alias)
    print(messages.REGISTER_SUCCESS.format(short_url, alias, full_url))


def get_home_page():
    alias = input(messages.HOME_PAGE_PROMPT).strip().lower()
    mappings = storage.get_all_mappings()

    for short_url, data in mappings.items():
        if data["alias"] == alias:
            status_code = url_request.check_url(data["full_url"])
            if status_code:
                print(
                    f"Адрес домашней страницы: {data['full_url']}\nПсевдоним домашней страницы: {alias}\nКод ответа страницы: {status_code}")
            return

    print(messages.HOME_PAGE_NOT_FOUND)


def get_standard_url():
    short_url = input(messages.URL_PROMPT).strip().lower()

    mapping = storage.get_full_url(short_url)
    if mapping:
        status_code = url_request.check_url(mapping["full_url"])
        if status_code:
            print(
                f"Стандартный интернет-адрес: {mapping['full_url']}\nКороткий интернет-адрес: {short_url}\nКод ответа страницы: {status_code}")
        return

    print(messages.URL_NOT_FOUND)


def get_all_urls():
    mappings = storage.get_all_mappings()
    print(messages.ALL_URLS_HEADER)
    for short_url, data in mappings.items():
        print(
            f"Короткий URL: {short_url}\nСтандартный URL: {data['full_url']}\nПсевдоним: {data['alias']}\n")
