from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()
llm = init_chat_model(
    "gpt-4.1",
    temperature=0
)

message = HumanMessage(
    content=[
        {"type": "text", "text": "What is happening in this image?"},
        {
            "type": "image_url",
            "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
            }
        }
    ]
)

response = llm.invoke([message])
print(response.content)
