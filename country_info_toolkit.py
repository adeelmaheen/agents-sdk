import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Tools for Capital, Language, and Population
async def get_country_info(country_name):
    capital_tool = Agent(
        name="Capital Tool",
        instructions="You provide the capital of the country.",
        model=model
    )
    language_tool = Agent(
        name="Language Tool",
        instructions="You provide the language spoken in the country.",
        model=model
    )
    population_tool = Agent(
        name="Population Tool",
        instructions="You provide the population of the country.",
        model=model
    )

    orchestrator_agent = Agent(
        name="Country Info Orchestrator",
        instructions="You take the country name and use all tools to provide complete information about the country.",
        model=model
    )

    # Running tools using orchestrator
    capital_result = await Runner.run(capital_tool, country_name, run_config=config)
    language_result = await Runner.run(language_tool, country_name, run_config=config)
    population_result = await Runner.run(population_tool, country_name, run_config=config)

    # Combine the results
    country_info = {
        "Country": country_name,
        "Capital": capital_result.final_output,
        "Language(s)": language_result.final_output,
        "Population": population_result.final_output
    }

    return country_info

async def main():
    country_name = input("Enter a country name to get information: ")
    country_info = await get_country_info(country_name)
    print("\n--- Country Information ---")
    for key, value in country_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    asyncio.run(main())
