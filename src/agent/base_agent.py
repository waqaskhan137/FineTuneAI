from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

class BaseAgent:
    def __init__(self, provider="openai", model_name="gpt-4", temperature=0.7, max_tokens=500, memory=True, api_key=None):
        """
        Initializes the LLM Agent with multiple provider options.
        :param provider: The AI provider ('openai', 'groq')
        :param model_name: The model name for the selected provider
        :param temperature: The randomness of the responses (0.0 - 1.0)
        :param max_tokens: Maximum tokens per response
        :param memory: Whether to use conversation memory
        :param api_key: API key for the selected provider, defaults to environment variable if not provided
        """
        self.provider = provider.lower()
        self.api_key = api_key or os.getenv("API_KEY")
        
        if self.provider == "openai":
            self.llm = OpenAI(model_name=model_name, temperature=temperature, max_tokens=max_tokens, openai_api_key=self.api_key)
        elif self.provider == "groq":
            self.llm = ChatGroq(model_name=model_name, temperature=temperature, max_tokens=max_tokens, groq_api_key=self.api_key)
        else:
            raise ValueError("Unsupported provider. Choose from 'openai' or 'groq'.")
        
        self.memory = ConversationBufferMemory() if memory else None
    
    def _get_prompt_template(self, user_prompt):
        """
        Creates a structured prompt template.
        :param user_prompt: User query.
        """
        prompt_text = """
        {user_prompt}
        AI: """
        return PromptTemplate(input_variables=["user_prompt"], template=prompt_text)
    
    def run(self, user_prompt, system_prompt="You are an AI assistant helping with queries."):
        """
        Executes the LLM agent with a given user prompt and optional system instruction.
        :param user_prompt: The prompt provided by the user.
        :param system_prompt: A system-level instruction (default is generic AI assistant).
        :return: The AI-generated response.
        """
        # Combine system and user prompts into a single input
        combined_prompt = f"{system_prompt}\nUser: {user_prompt}\nAI:"
        
        prompt_template = self._get_prompt_template(combined_prompt)
        chain = LLMChain(llm=self.llm, prompt=prompt_template, memory=self.memory)
        
        # Use the combined prompt as a single input
        response = chain.run({"user_prompt": combined_prompt})
        return response
