from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from pydantic import BaseModel, Field
from langchain.tools import tool
from dotenv import load_dotenv
import json
load_dotenv()

@tool
def get_current_weather(location: str) -> str:
    """Get the current weather in a given location."""
    return f"The current weather in {location} is sunny with a temperature of 25°C."


model = init_chat_model("gpt-4.1")

model_with_tools = model.bind_tools([get_current_weather])

# response = model_with_tools.invoke("What's the weather like in Boston?")

# for tool_call in response.tool_calls:
#     # View tool calls made by the model
#     result = get_current_weather(tool_call)
#     print("Tool call result:", result)


# Step 1: Model generates tool calls
messages = [{"role": "user", "content": "What's the weather in Boston?"}]
response = model_with_tools.invoke(messages)
messages.append(response)

for tool_call in response.tool_calls:
    tool_result = get_current_weather.invoke(tool_call)
    messages.append(tool_result)

final_response = model_with_tools.invoke(messages)
print(final_response.text)