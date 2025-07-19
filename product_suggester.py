import os
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.run import RunConfig
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
import asyncio

# Load environment variables from .env file
load_dotenv()

# Retrieve your Gemini API key from the environment
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Initialize the external Gemini client using AsyncOpenAI and Gemini API key
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define the model you want to use from Gemini (here we are using gemini-2.0-flash)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Create the RunConfig using the Gemini model and client
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Function to get treatment advice from Gemini API
async def get_treatment_advice(symptom: str):
    prompt = f"Please provide treatment advice for {symptom}."
    agent = Agent(
        name="SmartStoreAgent",
        instructions="You are a helpful assistant that suggests products based on user needs. If the user reports a symptom, suggest an appropriate product or treatment.",
        model=model
    )
    
    # Running the agent to get the result based on user input
    result = await Runner.run(agent, prompt, run_config=config)
    return result.final_output


# Main function to interact with the user
async def main():
    # Take user input (e.g., "I have a headache")
    user_input = input("Please describe your symptom (e.g., 'I have a headache'): ")
    
    # Get product suggestion and treatment advice from the agent
    suggestion = await get_treatment_advice(user_input)
    
    print(f"Suggestion: {suggestion}")


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())

