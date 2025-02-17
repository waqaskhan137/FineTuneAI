import os
from datetime import datetime
import logging
from utils.report_formatter import ReportFormatter
from utils.analysis_descriptions import ANALYSIS_DESCRIPTIONS

class ReportManager:
    def __init__(self, formatter=None):
        self.formatter = formatter or ReportFormatter()
        self.logger = logging.getLogger(__name__)

    def format_results(self, results):
        self.logger.info("Formatting analysis results")
        formatters = {
            "LexicalDiversityAnalysis": lambda result: (
                f"- Unique Word Ratio: {result[0]:.4f}\n- Most Common Words: {result[1]}"
            ),
            "EmbeddingSimilarityAnalysis": lambda result: (
                result if isinstance(result, str) else f"- Average Similarity Score: {result:.4f}"
            ),
            "ContextConsistencyAnalysis": lambda result: f"- Average Consistency Score: {result:.4f}",
            "TopicModelingAnalysis": lambda result: "\n".join(f"- {topic}" for topic in result),
            "DialogueStructureAnalysis": lambda result: result,
            "SentimentAnalysis": lambda result: "\n".join(f"- {sentiment}: {count}" for sentiment, count in result.items()),
            "KeywordDensityAnalysis": lambda result: "\n".join(f"- {keyword}: {density:.4f}" for keyword, density in result.items()),
            "PronounReferencingAnalysis": lambda result: "\n".join(f"- {pronoun}: {count}" for pronoun, count in result.items()),
        }

        default_formatter = lambda result: result.to_markdown(index=False) if hasattr(result, 'to_markdown') else str(result)

        for analysis_name, result in results.items():
            description = ANALYSIS_DESCRIPTIONS.get(analysis_name, {})
            title = description.get("title", analysis_name)
            desc = description.get("description", "")

            content = formatters.get(analysis_name, default_formatter)(result)
            self.formatter.add_section(title, desc, content)
            self.logger.info("Formatted result for analysis: %s", analysis_name)

    def save_report(self, report_path=None):
        self.logger.info("Saving report")
        report_content = self.formatter.get_report()

        # Ensure the reports directory exists
        os.makedirs("reports", exist_ok=True)

        # Generate a timestamp for the report filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"dataset_analysis_report_{timestamp}.md"
        report_path = report_path or os.path.join("reports", report_filename)

        # Save the report to the specified path
        with open(report_path, "w") as report_file:
            report_file.write(report_content)

        self.logger.info("Report saved to %s", report_path) 