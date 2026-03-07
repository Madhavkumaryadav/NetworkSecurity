import os
import sys
import pandas as pd

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger1 import logging
from networksecurity.utils.main_utils.Utils import load_object
from networksecurity.utils.ml_utils.model.estimator import NetworkModel

PREDICTION_LABEL_MAP = {1: "Phishing", 0: "Legitimate", -1: "Legitimate"}


class BatchPrediction:
    """
    Runs batch predictions from a CSV input file using saved model artifacts.
    """

    def __init__(
        self,
        input_file_path: str,
        model_file_path: str = "final_models/models.pkl",
        preprocessor_file_path: str = "final_models/preprocessor.pkl",
        output_file_path: str = "prediction_output/output.csv",
    ):
        self.input_file_path = input_file_path
        self.model_file_path = model_file_path
        self.preprocessor_file_path = preprocessor_file_path
        self.output_file_path = output_file_path

    def initiate_batch_prediction(self) -> str:
        """
        Loads the input CSV, runs predictions using the saved model, and writes
        the results (with a new 'predicted_column') to the output CSV path.

        Returns:
            str: Path to the output CSV file.
        """
        try:
            logging.info(f"Loading input data from: {self.input_file_path}")
            df = pd.read_csv(self.input_file_path)

            logging.info("Loading preprocessor and model artifacts")
            preprocessor = load_object(self.preprocessor_file_path)
            model = load_object(self.model_file_path)

            network_model = NetworkModel(preprocessor=preprocessor, model=model)

            logging.info("Running batch predictions")
            predictions = network_model.predict(df)

            df["predicted_column"] = predictions
            df["predicted_label"] = df["predicted_column"].map(PREDICTION_LABEL_MAP)

            output_dir = os.path.dirname(self.output_file_path)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
            df.to_csv(self.output_file_path, index=False)

            logging.info(
                f"Batch prediction complete. {len(df)} rows written to {self.output_file_path}"
            )
            return self.output_file_path

        except Exception as e:
            raise NetworkSecurityException(e, sys)
