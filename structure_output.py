from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import json
load_dotenv()

class Movie(BaseModel):
    """A movie with details."""
    title: str = Field(..., description="The title of the movie")
    director: str = Field(..., description="The director of the movie")
    year: int = Field(..., description="The release year of the movie")
    genre: str = Field(..., description="The genre of the movie")


model = init_chat_model("gpt-4.1")

model_with_structure = model.with_structured_output(Movie)

response = model_with_structure.invoke("Provide details about the movie Inception")
print(response)