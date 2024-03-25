import json


def extract_json(json_data, attack_label):
    if attack_label in json_data:
        return json_data[attack_label]
    else:
        return []


def parse_attack_json(attack_json):
    return json.dumps(attack_json, indent=2)