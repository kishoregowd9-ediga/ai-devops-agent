import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("OPENAI_ENDPOINT")
)

def analyze_log_with_ai(log):

    prompt = f"""
You are a DevOps troubleshooting assistant.

Analyze this CI/CD pipeline failure log.

Identify root cause and suggest fix.

Log:
{log}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You help troubleshoot DevOps failures"},
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content