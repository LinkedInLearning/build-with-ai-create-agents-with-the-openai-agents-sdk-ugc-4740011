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
# # Orchestrate Mulitple Agents
# # ---------------------------------------------------------------------------
class TravelOutput(BaseModel):
    destination: str
    duration: str
    summary: str
    cost: str
    tips: str

# ---- Planner Agent (builds day-by-day itinerary) ----
planner_agent = Agent(
    name="Planner Agent",
    model="gpt-5",
    handoff_description="Use me when the user asks to plan or outline an itinerary, schedule, or daily plan.",
    instructions=(
        "You specialize in building day-by-day travel itineraries and sequencing activities. "
        'Always return JSON with this structure: {"destination":"string","duration":"string","summary":"string"}.'
    ),
    model_settings=ModelSettings(
        reasoning={"effort": "medium"},
        extra_body={"text": {"verbosity": "low"}}
    ),
    tools=[
        WebSearchTool()
    ]
)

# ---- Budget Agent (estimates costs under constraints) ----
budget_agent = Agent(
    name="Budget Agent",
    model="gpt-5",
    handoff_description="Use me when the user mentions budget, price, cost, dollars, under $X, or asks 'how much'.",
    instructions=(
        "You estimate costs for lodging, food, transport, and activities at a high level; flag budget violations. "
        'Always return JSON with this structure: {"cost":"string"}.'
    ),
    model_settings=ModelSettings(
        reasoning={"effort": "medium"},
        extra_body={"text": {"verbosity": "low"}}
    )
)

# ---- Local Guide Agent (adds local tips & dining) ----
local_guide_agent = Agent(
    name="Local Guide Agent",
    model="gpt-5",
    handoff_description="Use me when the user asks for food, restaurants, neighborhoods, local tips, or 'what's good nearby'.",
    instructions=(
        "You provide restaurants, neighborhoods, cultural tips, and current local highlights. "
        'Always return JSON with this structure: {"tips":"string"}.'
    ),
    model_settings=ModelSettings(
        reasoning={"effort": "medium"},
        extra_body={"text": {"verbosity": "low"}}
    ),
    tools=[
        WebSearchTool()
    ]
)

# ---- Core orchestrator: Travel Agent ----
travel_agent = Agent(
    name="Travel Agent",
    model="gpt-5",
    instructions=(
        "You are a friendly and knowledgeable travel planner that helps users plan trips, suggest destinations, and create detailed summaries of their journeys.\n"
        "Your primary role is to orchestrate other specialized agents (used as tools) to complete the user's request.\n"
        "\n"
        "When planning an itinerary, call the **Planner Agent** to create daily schedules, organize destinations, and recommend attractions or activities. Do not create itineraries yourself.\n"
        "When estimating costs, call the **Budget Agent** to calculate the total trip cost including flights, hotels, and activities. Do not calculate or estimate prices on your own.\n"
        "When recommending local experiences, restaurants, neighborhoods, or cultural highlights, call the **Local Guide Agent** to provide these insights. Do not generate local recommendations without this agent.\n"
        "\n"
        "Use these agents one at a time in a logical order based on the request — start with the Planner Agent, then the Budget Agent, and finally the Local Guide Agent.\n"
        "After receiving results from these agents, combine their outputs into a single structured summary.\n"
        "\n"
        "Return JSON output using this exact structure:\n"
        "{\"destination\": \"string\", \"duration\": \"string\", \"summary\": \"string\", \"cost\": \"string\", \"tips\": \"string\"}.\n"
    ),
    output_type=TravelOutput, 
    model_settings=ModelSettings(
          reasoning={"effort": "medium"},   # minimal | low | medium | high 
          extra_body={"text":{"verbosity":"low"}}  # low | medium | high
    ),
    tools=[
        WebSearchTool(),
        planner_agent.as_tool(
            tool_name="planner_agent", 
            tool_description="plan or outline an itinerary, schedule, or daily plan"),
        budget_agent.as_tool(
            tool_name="budget_agent", 
            tool_description="calculates the cost of a trip"),
        local_guide_agent.as_tool(
            tool_name="local_guide_agent", 
            tool_description="provide restaurants, neighborhoods, cultural tips, and current local highlights")
    ]
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
    print(f"Cost: {data.cost}")
    print(f"Tips: {data.tips}")

async def main():
    try:
        result = await Runner.run(travel_agent, '''I'm considering a trip to Jamaica sometime in late September or early October. 
                                                I'm pretty flexible with the exact dates, maybe around a week-long trip.     
                                                I'd like to get an idea of flight ticket prices and some well-located hotels.     
                                                I'm also a big foodie, so any recommendations for great local restaurants would be fantastic! 
                                                Do not ask follow-up questions.''')
        print_fields(result.final_output)
    except Exception as e:
        print("Error", e)

if __name__ == "__main__":
    asyncio.run(main())