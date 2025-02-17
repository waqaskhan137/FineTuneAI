import os
import logging
from datetime import datetime
from dataset_analyzer import DatasetAnalyzer
from analysis_registrar import AnalysisRegistrar
from report_manager import ReportManager
from logging_config import setup_logging
from agent.fine_tuning_agent import FineTuningStrategyDefinerAgent, get_latest_report

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting the dataset analysis process")

    # Update the path to the dataset
    analyzer = DatasetAnalyzer("../data/Sample Dataset.xlsx")
    
    # Register analyses
    registrar = AnalysisRegistrar()
    registrar.register_analyses(analyzer)

    # Execute analyses and get results
    results = analyzer.execute_analyses()

    # Format and save the report
    report_manager = ReportManager()
    report_manager.format_results(results)
    report_manager.save_report()

    logger.info("Dataset analysis process completed")

    # Generate a strategy document based on the latest analysis report
    try:
        latest_report_path = get_latest_report("reports/")
        with open(latest_report_path, 'r') as file:
            analysis_report = file.read()

        # Instantiate the fine-tuning strategy agent
        strategy_agent = FineTuningStrategyDefinerAgent(provider="groq", model_name="qwen-2.5-32b")
        strategy_response = strategy_agent.define_strategy(analysis_report)

        # Save the strategy document with a unique identifier
        strategy_filename = f"strategy_document_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        strategy_path = os.path.join("reports", strategy_filename)
        with open(strategy_path, 'w') as strategy_file:
            strategy_file.write(strategy_response)

        logger.info(f"Strategy document saved as {strategy_filename}")

    except FileNotFoundError as e:
        logger.error(f"Error generating strategy document: {e}")

if __name__ == "__main__":
    main() 