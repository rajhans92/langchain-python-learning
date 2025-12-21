from langchain_openai import ChatOpenAI;
from dotenv import load_dotenv;
load_dotenv()


model = ChatOpenAI(model="gpt-4.1")

response = model.stream("Why do parrots talk?")
connt_res = ""
for res in response:
    print(res.content, end='', flush=True)
    print("<<==================================>><<==================================>><<==================================>><<==================================>>")
    connt_res += res.content

print("<<==================================>>")
print(connt_res)