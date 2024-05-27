import random
import string
from common import messages
from utils import regex, storage, url_request
from logger.logger_config import logger

def generate_short_url(full_url):
    domain_and_zone = full_url.split('//')[-1].split('/')[0]
    domain, zone = domain_and_zone.split('.')
    consonants_only = regex.extract_consonants(domain)
    short_url = f"{consonants_only}.{zone}"
    return short_url


def register_url():
    full_url = input(messages.REGISTER_PROMPT).strip().lower()
    if not regex.is_valid_url(full_url):
        logger.error("Invalid URL format")
        print("Неверный формат URL")
        return

    alias = full_url.split('/')[2]
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
