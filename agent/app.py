from agent.log_analyzer import search_known_issue
from agent.openai_client import analyze_log_with_ai
from agent.storage import store_log

def run_agent(log):

    store_log(log)

    solution = search_known_issue(log)

    if solution:
        return {
            "type":"known_issue",
            "solution":solution
        }

    ai_solution = analyze_log_with_ai(log)

    return {
        "type":"ai_analysis",
        "solution":ai_solution
    }
