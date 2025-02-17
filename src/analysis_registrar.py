import os
import importlib
import inspect
import logging
from analyses.base_analysis import BaseAnalysis

class AnalysisRegistrar:
    def __init__(self, analyses_dir="analyses"):
        self.analyses_dir = analyses_dir
        self.logger = logging.getLogger(__name__)

    def register_analyses(self, analyzer):
        self.logger.info("Registering analyses from directory: %s", self.analyses_dir)
        for filename in os.listdir(self.analyses_dir):
            if filename.endswith(".py") and filename != "base_analysis.py":
                module_name = f"{self.analyses_dir}.{filename[:-3]}"
                module = importlib.import_module(module_name)
                
                # Find all classes in the module that inherit from BaseAnalysis
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, BaseAnalysis) and obj is not BaseAnalysis:
                        analyzer.register_analysis(obj)
                        self.logger.info("Registered analysis: %s", name) 