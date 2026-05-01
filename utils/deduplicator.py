from config import seen_places
from utils.runtime_json_data import append_to_jsonl


def add_existing_link(link, name, rating):
    if link in seen_places or link == "NA":
        return True
    else:
        seen_places[link] = {"name": name, "rating": rating, "details_fetched": False}
        record = {link: seen_places[link]}
        append_to_jsonl(record)
        return False