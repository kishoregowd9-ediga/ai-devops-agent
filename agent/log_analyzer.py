import json

def search_known_issue(log):

    with open("agent/knowledge_base.json") as f:
        kb = json.load(f)

    log_lower = log.lower()

    for item in kb:
        if item["pattern"].lower() in log_lower:
            return item["solution"]

    return None