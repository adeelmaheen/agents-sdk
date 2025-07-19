# import os
# from dotenv import load_dotenv
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
# from agents.run import RunConfig
# import asyncio

# # Load environment variables from the .env file
# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# # External client setup using Gemini API
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# # Model setup
# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# # Run configuration
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# # Main logic to analyze mood and suggest activities
# async def main():
#     agent_1 = Agent(
#         name="Mood Analyzer",
#         instructions="You are an agent that analyzes the mood based on the message and provides advice for that mood.",
#         model=model
#     )

#     agent_2 = Agent(
#         name="Activity Recommender",
#         instructions="If the mood is sad or stressed, suggest an activity to help relax or cheer up. If the mood is happy, suggest ways to stay positive.",
#         model=model
#     )

#     # Dynamic user input for mood analysis
#     user_message = input("Please share your current mood (e.g., happy, sad, stressed, jolly, annoyed, etc.): ")

#     # Running the agents to analyze the mood
#     mood_result = await Runner.run(agent_1, user_message, run_config=config)
#     print(f"Agent 1 (Mood Analyzer) Response: {mood_result.final_output}")

#     # Define the structured response dictionary
#     structured_response = {
#         "Mood": "",
#         "Analysis": "",
#         "Activity Suggestions": []
#     }

#     # Handling different moods and providing specific suggestions
#     if "happy" in mood_result.final_output:
#         structured_response["Mood"] = "Happy"
#         structured_response["Analysis"] = "You are in a positive and joyful mood."
#         activity_result = await Runner.run(agent_2, "Suggest ways to stay happy and positive", run_config=config)
#         structured_response["Activity Suggestions"] = [
#             "Practice gratitude daily",
#             "Spend time with loved ones",
#             "Engage in activities you enjoy"
#         ]
    
#     elif "sad" in mood_result.final_output or "stressed" in mood_result.final_output:
#         structured_response["Mood"] = "Sad or Stressed"
#         structured_response["Analysis"] = "You are feeling down or stressed and need relaxation."
#         activity_result = await Runner.run(agent_2, "Suggest an activity to help relax and improve mood", run_config=config)
#         structured_response["Activity Suggestions"] = [
#             "Take a deep breath and meditate",
#             "Go for a walk in nature",
#             "Practice deep breathing exercises"
#         ]
    
#     elif "jolly" in mood_result.final_output:
#         structured_response["Mood"] = "Jolly"
#         structured_response["Analysis"] = "You're feeling cheerful and ready for fun!"
#         activity_result = await Runner.run(agent_2, "Suggest some fun activities to keep the jolly mood going", run_config=config)
#         structured_response["Activity Suggestions"] = [
#             "Watch a funny movie",
#             "Listen to upbeat music",
#             "Try a fun outdoor activity"
#         ]

#     elif "annoyed" in mood_result.final_output:
#         structured_response["Mood"] = "Annoyed"
#         structured_response["Analysis"] = "You're feeling irritated and need calming activities."
#         activity_result = await Runner.run(agent_2, "Suggest some calming activities for annoyance", run_config=config)
#         structured_response["Activity Suggestions"] = [
#             "Take a break and drink some water",
#             "Do some stretching exercises",
#             "Practice mindfulness"
#         ]

#     elif "disappointed" in mood_result.final_output or "disheartened" in mood_result.final_output:
#         structured_response["Mood"] = "Disappointed or Disheartened"
#         structured_response["Analysis"] = "You're feeling down or disheartened and need emotional uplifting."
#         activity_result = await Runner.run(agent_2, "Suggest activities to lift the mood and overcome disappointment", run_config=config)
#         structured_response["Activity Suggestions"] = [
#             "Reflect on past successes",
#             "Talk to a friend or family member",
#             "Engage in a creative hobby"
#         ]
    
#     elif "crazy" in mood_result.final_output:
#         structured_response["Mood"] = "Crazy"
#         structured_response["Analysis"] = "You're full of high energy and need to channel it positively."
#         activity_result = await Runner.run(agent_2, "Suggest activities to channel the crazy energy into something productive", run_config=config)
#         structured_response["Activity Suggestions"] = [
#             "Work on a new creative project",
#             "Exercise to release energy",
#             "Organize or clean your space"
#         ]
    
#     else:
#         structured_response["Mood"] = "Unrecognized"
#         structured_response["Analysis"] = "The mood entered could not be recognized. Please provide a more specific mood."
#         structured_response["Activity Suggestions"] = ["Please try again with a more specific mood."]

#     # Printing the structured response
#     print("\n--- Mood Analysis Output ---")
#     print(f"Mood: {structured_response['Mood']}")
#     print(f"Analysis: {structured_response['Analysis']}")
#     print(f"Suggested Activities:")
#     for activity in structured_response["Activity Suggestions"]:
#         print(f"- {activity}")

# if __name__ == "__main__":
#     asyncio.run(main())

import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio

# Load environment variables from the .env file to securely access the Gemini API key
load_dotenv()

# Retrieve the Gemini API key from the environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# If no API key is found, raise an error and stop the execution
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# External client setup using Gemini API to connect to the Gemini service
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Set up the model for generating chat completions using the Gemini API
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Define the run configuration, including the model and external client
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Main function that analyzes the user's mood and provides activity suggestions
async def main():
    # Agent 1 is responsible for analyzing the user's mood based on the input message
    agent_1 = Agent(
        name="Mood Analyzer",
        instructions="You are an agent that analyzes the mood based on the message and provides advice for that mood.",
        model=model
    )

    # Agent 2 suggests activities based on the detected mood (e.g., happy, sad, etc.)
    agent_2 = Agent(
        name="Activity Recommender",
        instructions="If the mood is sad or stressed, suggest an activity to help relax or cheer up. If the mood is happy, suggest ways to stay positive.",
        model=model
    )

    # Asking the user for their current mood and adding a new line for better readability
    user_message = input("Please share your current mood (e.g., happy, sad, stressed, jolly, annoyed, etc.): \n")

    # Running the mood analysis agent to analyze the user's mood based on their input
    mood_result = await Runner.run(agent_1, user_message, run_config=config)
    print(f"Agent 1 (Mood Analyzer) Response: {mood_result.final_output}")

    # Define a dictionary to store the structured response (mood, analysis, and suggestions)
    structured_response = {
        "Mood": "",
        "Analysis": "",
        "Activity Suggestions": []
    }

    # Handle different moods based on the analysis and provide suggestions accordingly
    if "happy" in mood_result.final_output:
        structured_response["Mood"] = "Happy"
        structured_response["Analysis"] = "You are in a positive and joyful mood."
        activity_result = await Runner.run(agent_2, "Suggest ways to stay happy and positive", run_config=config)
        structured_response["Activity Suggestions"] = [
            "Practice gratitude daily",
            "Spend time with loved ones",
            "Engage in activities you enjoy"
        ]
    
    elif "sad" in mood_result.final_output or "stressed" in mood_result.final_output:
        structured_response["Mood"] = "Sad or Stressed"
        structured_response["Analysis"] = "You are feeling down or stressed and need relaxation."
        activity_result = await Runner.run(agent_2, "Suggest an activity to help relax and improve mood", run_config=config)
        structured_response["Activity Suggestions"] = [
            "Take a deep breath and meditate",
            "Go for a walk in nature",
            "Practice deep breathing exercises"
        ]
    
    elif "jolly" in mood_result.final_output:
        structured_response["Mood"] = "Jolly"
        structured_response["Analysis"] = "You're feeling cheerful and ready for fun!"
        activity_result = await Runner.run(agent_2, "Suggest some fun activities to keep the jolly mood going", run_config=config)
        structured_response["Activity Suggestions"] = [
            "Watch a funny movie",
            "Listen to upbeat music",
            "Try a fun outdoor activity"
        ]

    elif "annoyed" in mood_result.final_output:
        structured_response["Mood"] = "Annoyed"
        structured_response["Analysis"] = "You're feeling irritated and need calming activities."
        activity_result = await Runner.run(agent_2, "Suggest some calming activities for annoyance", run_config=config)
        structured_response["Activity Suggestions"] = [
            "Take a break and drink some water",
            "Do some stretching exercises",
            "Practice mindfulness"
        ]

    elif "disappointed" in mood_result.final_output or "disheartened" in mood_result.final_output:
        structured_response["Mood"] = "Disappointed or Disheartened"
        structured_response["Analysis"] = "You're feeling down or disheartened and need emotional uplifting."
        activity_result = await Runner.run(agent_2, "Suggest activities to lift the mood and overcome disappointment", run_config=config)
        structured_response["Activity Suggestions"] = [
            "Reflect on past successes",
            "Talk to a friend or family member",
            "Engage in a creative hobby"
        ]
    
    elif "crazy" in mood_result.final_output:
        structured_response["Mood"] = "Crazy"
        structured_response["Analysis"] = "You're full of high energy and need to channel it positively."
        activity_result = await Runner.run(agent_2, "Suggest activities to channel the crazy energy into something productive", run_config=config)
        structured_response["Activity Suggestions"] = [
            "Work on a new creative project",
            "Exercise to release energy",
            "Organize or clean your space"
        ]
    
    else:
        structured_response["Mood"] = "Unrecognized"
        structured_response["Analysis"] = "The mood entered could not be recognized. Please provide a more specific mood."
        structured_response["Activity Suggestions"] = ["Please try again with a more specific mood."]

    # Printing the structured response to the user
    print("\n--- Mood Analysis Output ---")
    print(f"Mood: {structured_response['Mood']}")
    print(f"Analysis: {structured_response['Analysis']}")
    print(f"Suggested Activities:")
    for activity in structured_response["Activity Suggestions"]:
        print(f"- {activity}")

# Run the main function asynchronously
if __name__ == "__main__":
    asyncio.run(main())
