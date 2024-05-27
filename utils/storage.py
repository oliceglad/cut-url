import os
import json

STORAGE_PATH = 'storage/urls.json'
def load_storage():
    if not os.path.exists(STORAGE_PATH):
        return {}
    with open(STORAGE_PATH, 'r') as file:
        return json.load(file)

def save_storage(data):
    with open(STORAGE_PATH, 'w') as file:
        json.dump(data, file)

def add_url_mapping(short_url, full_url, alias):
    storage = load_storage()
    storage[short_url] = {"full_url": full_url, "alias": alias}
    save_storage(storage)

def get_full_url(short_url):
    storage = load_storage()
    return storage.get(short_url, None)

def get_all_mappings():
    return load_storage()
