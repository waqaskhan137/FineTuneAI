import os
from glob import glob
from .base_agent import BaseAgent

class FineTuningStrategyDefinerAgent(BaseAgent):
    def __init__(self, provider="groq", model_name="deepseek-r1-distill-llama-70b", temperature=0.7, max_tokens=500, memory=True, api_key=None):
        super().__init__(provider, model_name, temperature, max_tokens, memory, api_key)
    
    def define_strategy(self, user_prompt):
        """
        Define a fine-tuning strategy based on the user prompt.
        :param user_prompt: The prompt provided by the user.
        :return: The AI-generated strategy.
        """
        system_prompt = (
            "You are an AI agent specialized in analyzing text corpus reports. "
            "Your task is to generate a strategy document that outlines improvements "
            "and recommendations for achieving better results in future analyses."
        )
        return self.run(user_prompt, system_prompt)

def get_latest_report(directory="reports/"):
    """
    Get the latest report file from the specified directory.
    :param directory: The directory to search for report files.
    :return: The path to the latest report file.
    """
    report_files = glob(os.path.join(directory, "dataset_analysis_report_*.md"))
    
    # Debugging output
    print(f"Looking for report files in: {os.path.abspath(directory)}")
    print(f"Found report files: {report_files}")
    
    if not report_files:
        raise FileNotFoundError("No report files found in the specified directory.")
    
    # Sort files by modification time in descending order
    report_files.sort(key=os.path.getmtime, reverse=True)
    return report_files[0]

# Example usage
if __name__ == "__main__":
    # Instantiate the agent
    strategy_agent = FineTuningStrategyDefinerAgent(provider="groq", model_name="qwen-2.5-32b")
    
    # Get the latest report
    latest_report_path = get_latest_report()
    with open(latest_report_path, 'r') as file:
        sample_report = file.read()
    
    # Define a strategy based on the latest report
    strategy_response = strategy_agent.define_strategy(sample_report)
    
    # Print the strategy response
    print(strategy_response) 