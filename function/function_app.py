import azure.functions as func
from agent.app import run_agent

app = func.FunctionApp()

@app.route(route="analyze")
def analyze(req: func.HttpRequest) -> func.HttpResponse:

    log = req.get_body().decode()

    result = run_agent(log)

    return func.HttpResponse(str(result))