"""
Unit tests for the BatchPrediction pipeline.
"""
import os
import sys
import tempfile

import numpy as np
import pandas as pd
import pytest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from networksecurity.pipeline.batch_prediction import BatchPrediction, PREDICTION_LABEL_MAP


class TestBatchPrediction:

    def _make_input_csv(self, tmp_path, n_rows=5, n_cols=30):
        """Create a minimal CSV file that looks like the phishing dataset."""
        data = {f"feature_{i}": np.random.randint(-1, 2, n_rows) for i in range(n_cols)}
        df = pd.DataFrame(data)
        csv_path = str(tmp_path / "input.csv")
        df.to_csv(csv_path, index=False)
        return csv_path, df

    def test_prediction_label_map_covers_all_outputs(self):
        assert 1 in PREDICTION_LABEL_MAP
        assert 0 in PREDICTION_LABEL_MAP
        assert -1 in PREDICTION_LABEL_MAP
        assert PREDICTION_LABEL_MAP[1] == "Phishing"
        assert PREDICTION_LABEL_MAP[0] == "Legitimate"
        assert PREDICTION_LABEL_MAP[-1] == "Legitimate"

    def test_output_file_is_created(self, tmp_path):
        csv_path, df = self._make_input_csv(tmp_path)
        output_path = str(tmp_path / "output" / "result.csv")

        mock_preprocessor = MagicMock()
        mock_preprocessor.transform.return_value = df.values

        mock_model = MagicMock()
        mock_model.predict.return_value = np.ones(len(df), dtype=int)

        with patch(
            "networksecurity.pipeline.batch_prediction.load_object",
            side_effect=[mock_preprocessor, mock_model],
        ):
            bp = BatchPrediction(
                input_file_path=csv_path,
                output_file_path=output_path,
            )
            result_path = bp.initiate_batch_prediction()

        assert os.path.exists(result_path)
        assert result_path == output_path

    def test_output_csv_has_predicted_columns(self, tmp_path):
        csv_path, df = self._make_input_csv(tmp_path)
        output_path = str(tmp_path / "output.csv")

        mock_preprocessor = MagicMock()
        mock_preprocessor.transform.return_value = df.values

        mock_model = MagicMock()
        mock_model.predict.return_value = np.array([1, 0, 1, -1, 0])

        with patch(
            "networksecurity.pipeline.batch_prediction.load_object",
            side_effect=[mock_preprocessor, mock_model],
        ):
            bp = BatchPrediction(
                input_file_path=csv_path,
                output_file_path=output_path,
            )
            bp.initiate_batch_prediction()

        result = pd.read_csv(output_path)
        assert "predicted_column" in result.columns
        assert "predicted_label" in result.columns

    def test_predicted_labels_are_mapped_correctly(self, tmp_path):
        csv_path, df = self._make_input_csv(tmp_path, n_rows=3)
        output_path = str(tmp_path / "output.csv")

        mock_preprocessor = MagicMock()
        mock_preprocessor.transform.return_value = df.values

        mock_model = MagicMock()
        mock_model.predict.return_value = np.array([1, 0, -1])

        with patch(
            "networksecurity.pipeline.batch_prediction.load_object",
            side_effect=[mock_preprocessor, mock_model],
        ):
            bp = BatchPrediction(
                input_file_path=csv_path,
                output_file_path=output_path,
            )
            bp.initiate_batch_prediction()

        result = pd.read_csv(output_path)
        assert result["predicted_label"].tolist() == ["Phishing", "Legitimate", "Legitimate"]

    def test_missing_model_file_raises_exception(self, tmp_path):
        csv_path, _ = self._make_input_csv(tmp_path)
        output_path = str(tmp_path / "output.csv")

        bp = BatchPrediction(
            input_file_path=csv_path,
            model_file_path=str(tmp_path / "nonexistent.pkl"),
            preprocessor_file_path=str(tmp_path / "nonexistent_pre.pkl"),
            output_file_path=output_path,
        )
        with pytest.raises(Exception):
            bp.initiate_batch_prediction()

    def test_output_to_current_directory(self, tmp_path, monkeypatch):
        """Output path with no directory component should not raise an error."""
        csv_path, df = self._make_input_csv(tmp_path)
        # Change to tmp_path so the output file lands there
        monkeypatch.chdir(tmp_path)
        output_filename = "flat_output.csv"

        mock_preprocessor = MagicMock()
        mock_preprocessor.transform.return_value = df.values

        mock_model = MagicMock()
        mock_model.predict.return_value = np.ones(len(df), dtype=int)

        with patch(
            "networksecurity.pipeline.batch_prediction.load_object",
            side_effect=[mock_preprocessor, mock_model],
        ):
            bp = BatchPrediction(
                input_file_path=csv_path,
                output_file_path=output_filename,
            )
            result_path = bp.initiate_batch_prediction()

        assert os.path.exists(result_path)
