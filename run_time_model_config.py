from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

configurable_model = init_chat_model(temperature=0)

gpt_reply = configurable_model.invoke(
    "what's your name",
    config={"configurable": {"model": "gpt-5-nano"}},  # Run with GPT-5-Nano
)

print("===================================")
print(gpt_reply)

cloude_reply = configurable_model.invoke(
    "what's your name",
    config={"configurable": {"model": "claude-sonnet-4-5-20250929"}},  # Run with Claude
)
print("===================================")
print(cloude_reply)