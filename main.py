from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()
openai_api_key= os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=openai_api_key,
    base_url="https://openrouter.ai/api/v1",
)

model = OpenAIChatCompletionsModel(
    model="deepseek/deepseek-r1-0528-qwen3-8b:free",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name="Writer Agent",
    instructions="You are a helpful writer agent. generate a short stories,poems,easy etc based on the input sentence.", 
)

response = Runner.run_sync(
    agent,
    input=input("Enter a sentence in English: "),
    run_config=config
)

print(response.final_output) 