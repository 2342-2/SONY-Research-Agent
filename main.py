from .env import load_dotenv
from pyadantic import BaseModel
from langchain_openai_ import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatOpenAI()
llm2 = ChatAnthropic()