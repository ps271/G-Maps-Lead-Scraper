import json
import os
import config


keyword = config.KEYWORD
location = config.LOCATION
root_file = config.PROJECT_ROOT
file = f"{root_file}/Data/{keyword}_{location}"

def save_to_json(data, filename=f"{file}.json"):
    temp_file = filename + ".tmp"

    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    os.replace(temp_file, filename)

def append_to_jsonl(record, filename=f"{file}.jsonl"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def load_json(filename=f"{file}.json"):
    if not os.path.exists(filename):
        return {}

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def load_from_jsonl(filename=f"{file}.jsonl"):
    data = {}

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                record = json.loads(line)
                for key, value in record.items():
                    if value.get("details_fetched"):
                        data.update(record)
    except FileNotFoundError:
        pass

    return data
