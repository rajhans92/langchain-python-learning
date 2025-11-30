from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import json
load_dotenv()

model = init_chat_model("gpt-4.1")

# onversation = [
#     SystemMessage("You are a helpful assistant that translates English to French."),
#     HumanMessage("Translate: I love programming."),
#     AIMessage("J'adore la programmation."),
#     HumanMessage("Translate: how are you Rupesh.")
# ]


# response = model.invoke(onversation)

# print(json.dumps(response), indent=4)

#response = model.stream("Why do parrots have colorful feathers?")

##############################

# for chunk in model.stream("Why do parrots have colorful feathers?"):
#     print(chunk.content, end='', flush=True)

##############################

# responses = model.batch([
#     "Why do parrots have colorful feathers?",
#     "How do airplanes fly?",
#     "What is quantum computing?"
# ])
# print(responses)
# print("-----")
# for response in responses:
#     print(response.content)


# print("------------------------")
# print("------------------------")
for response1 in model.batch_as_completed([
    "Why do parrots have colorful feathers?",
    "How do airplanes fly?",
    "What is quantum computing?"
]):
    print(response1.content)
    print("------------------------")