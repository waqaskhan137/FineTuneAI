from .base_analysis import BaseAnalysis
import language_tool_python

class GrammarSyntaxAnalysis(BaseAnalysis):
    def run(self):
        # Initialize the language tool
        tool = language_tool_python.LanguageTool('en-US')
        
        # Drop NaN values and convert to a list
        texts = self.df_dataset["Assistant"].dropna().tolist()
        
        # Analyze each text for grammar and syntax errors
        error_counts = []
        for text in texts:
            matches = tool.check(text)
            error_counts.append(len(matches))
        
        # Return the average number of errors per text
        avg_errors = sum(error_counts) / len(error_counts) if error_counts else 0
        return f"Average grammar/syntax errors per text: {avg_errors:.2f}" 