"""
Build with AI: Create Agents with the OpenAI Agents SDK
All examples use Python and the OpenAI client.

Prereqs:
  pip install -r requirements.txt
  export API_KEY = os.environ[...] or set the api_key to the client
"""
import os
import asyncio
import json

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner, ModelSettings, WebSearchTool
from pydantic import BaseModel, ValidationError

# read local .env file
_ = load_dotenv(find_dotenv()) 

# retrieve OpenAI API key
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']  
)

# # ---------------------------------------------------------------------------
# # Extend the agent with tools
# # ---------------------------------------------------------------------------
class TravelOutput(BaseModel):
    destination: str
    duration: str
    summary: str

travel_agent = Agent(
    name="Travel Agent",
    model="gpt-5",
    instructions=(
        "You are a friendly and knowledgeable travel planner that helps users plan trips, "
        "suggest destinations, and create brief summaries of their journeys. "
        "Use tools when helpful (e.g., Web Search). "
        "Always return your response as valid JSON matching this structure: "
        '{"destination": "string", "duration": "string", "summary": "string"}'
    ), 
    output_type=TravelOutput, 
    model_settings=ModelSettings(
          reasoning={"effort": "medium"},   # minimal | low | medium | high 
          extra_body={"text":{"verbosity":"low"}}  # low | medium | high
    ),
    tools=[
        WebSearchTool()
    ],
)

# --- Pretty print helper ----------------------------------------------------
def print_fields(data):
    if isinstance(data, str):
        try:
            data = TravelOutput(**json.loads(data))
        except (json.JSONDecodeError, ValidationError) as e:
            print("Raw output:", data)
            return
    print(f"Destination: {data.destination}")
    print(f"Duration: {data.duration}")
    print(f"Summary: {data.summary}")

async def main():
    try:
        result = await Runner.run(travel_agent, "Plan a 3-day trip to Jamaica under $1500. " \
                                                "Find uncommon places that are off the beaten path and little known.")
        print_fields(result.final_output)
    except Exception as e:
        print("Error", e)

if __name__ == "__main__":
    asyncio.run(main())