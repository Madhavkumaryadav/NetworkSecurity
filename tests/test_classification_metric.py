"""
Unit tests for classification metric utilities.
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from networksecurity.utils.ml_utils.metric.classification_metric import get_classification_score


class TestClassificationMetric:
    def test_perfect_predictions(self):
        y_true = np.array([1, 1, 0, 0, 1])
        y_pred = np.array([1, 1, 0, 0, 1])

        result = get_classification_score(y_true, y_pred)

        assert result.f1_score == pytest.approx(1.0, abs=1e-6)
        assert result.precision_score == pytest.approx(1.0, abs=1e-6)
        assert result.recall_score == pytest.approx(1.0, abs=1e-6)

    def test_returns_artifact_with_float_fields(self):
        y_true = np.array([1, 0, 1, 0])
        y_pred = np.array([1, 1, 0, 0])

        result = get_classification_score(y_true, y_pred)

        assert isinstance(result.f1_score, float)
        assert isinstance(result.precision_score, float)
        assert isinstance(result.recall_score, float)

    def test_scores_bounded_between_0_and_1(self):
        y_true = np.array([1, 0, 1, 1, 0, 0])
        y_pred = np.array([0, 1, 1, 0, 0, 1])

        result = get_classification_score(y_true, y_pred)

        assert 0.0 <= result.f1_score <= 1.0
        assert 0.0 <= result.precision_score <= 1.0
        assert 0.0 <= result.recall_score <= 1.0

    def test_handles_binary_labels_0_and_1(self):
        """Labels are 0/1 after data_transformation replaces -1 with 0."""
        y_true = np.array([0, 1, 0, 1, 1])
        y_pred = np.array([0, 1, 1, 1, 0])

        result = get_classification_score(y_true, y_pred)

        assert result.f1_score > 0.0

    def test_no_zero_division_error_on_all_same_predictions(self):
        """zero_division=0 should prevent exceptions when all predictions are one class."""
        y_true = np.array([1, 1, 1, 0])
        y_pred = np.array([1, 1, 1, 1])

        result = get_classification_score(y_true, y_pred)
        assert 0.0 <= result.f1_score <= 1.0
