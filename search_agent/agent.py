from google.adk.agents import Agent
from google.adk.tools import google_search

instruction_prompt = "You are a helpful assistant that can answer questions."
response_format = "You should respond in a friendly and helpful manner. Do not summarize the results."

root_agent = Agent(
    name="search_assistant_agent",
    model="gemini-2.5-flash",
    description="Agent to search the web for a wide range of information.",
    instruction=instruction_prompt + response_format,
    tools=[ google_search ]
)