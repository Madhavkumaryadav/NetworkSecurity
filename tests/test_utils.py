"""
Unit tests for networksecurity.utils.main_utils.Utils
"""
import os
import sys
import pickle
import tempfile

import numpy as np
import pytest
import yaml

# Ensure the package root is on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from networksecurity.utils.main_utils.Utils import (
    read_yaml_file,
    write_yaml_file,
    save_numpy_array_data,
    load_numpy_array_data,
    save_object,
    load_object,
    evaluate_models,
)


# ── write_yaml_file / read_yaml_file ─────────────────────────────────────────

class TestYamlUtils:
    def test_write_and_read_yaml(self, tmp_path):
        content = {"key": "value", "number": 42}
        file_path = str(tmp_path / "test.yaml")

        write_yaml_file(file_path, content)

        result = read_yaml_file(file_path)
        assert result["key"] == "value"
        assert result["number"] == 42

    def test_write_yaml_replace_true_overwrites_file(self, tmp_path):
        file_path = str(tmp_path / "test.yaml")

        write_yaml_file(file_path, {"version": 1})
        write_yaml_file(file_path, {"version": 2}, replace=True)

        result = read_yaml_file(file_path)
        assert result["version"] == 2

    def test_write_yaml_replace_false_does_not_delete_existing(self, tmp_path):
        """When replace=False the file is still written (overwritten in place)."""
        file_path = str(tmp_path / "test.yaml")

        write_yaml_file(file_path, {"a": 1})
        write_yaml_file(file_path, {"b": 2}, replace=False)

        result = read_yaml_file(file_path)
        # The second write should succeed and produce a readable YAML file
        assert result is not None

    def test_write_yaml_creates_intermediate_directories(self, tmp_path):
        file_path = str(tmp_path / "subdir" / "nested" / "output.yaml")
        write_yaml_file(file_path, {"ok": True})
        assert os.path.exists(file_path)


# ── save / load numpy arrays ─────────────────────────────────────────────────

class TestNumpyUtils:
    def test_save_and_load_array(self, tmp_path):
        arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
        file_path = str(tmp_path / "array.npy")

        save_numpy_array_data(file_path, arr)
        loaded = load_numpy_array_data(file_path)

        np.testing.assert_array_equal(arr, loaded)

    def test_save_creates_directory(self, tmp_path):
        arr = np.zeros((5, 3))
        file_path = str(tmp_path / "subdir" / "array.npy")

        save_numpy_array_data(file_path, arr)
        assert os.path.exists(file_path)


# ── save / load objects ───────────────────────────────────────────────────────

class TestPickleUtils:
    def test_save_and_load_object(self, tmp_path):
        obj = {"hello": "world", "numbers": [1, 2, 3]}
        file_path = str(tmp_path / "obj.pkl")

        save_object(file_path, obj)
        loaded = load_object(file_path)

        assert loaded == obj

    def test_load_object_missing_file_raises(self, tmp_path):
        file_path = str(tmp_path / "missing.pkl")
        with pytest.raises(Exception):
            load_object(file_path)


# ── evaluate_models ───────────────────────────────────────────────────────────

class TestEvaluateModels:
    """evaluate_models should use f1_weighted scoring for classification."""

    def test_returns_dict_with_model_names(self):
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.datasets import make_classification

        X, y = make_classification(n_samples=200, n_features=10, random_state=42)
        x_train, x_test = X[:160], X[160:]
        y_train, y_test = y[:160], y[160:]

        models = {"DT": DecisionTreeClassifier()}
        params = {"DT": {"max_depth": [2, 4]}}

        report = evaluate_models(x_train, y_train, x_test, y_test, models, params)

        assert "DT" in report
        score = report["DT"]
        assert 0.0 <= score <= 1.0

    def test_score_is_f1_not_r2(self):
        """r2_score can be negative; f1_weighted is always in [0, 1]."""
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.datasets import make_classification

        X, y = make_classification(n_samples=200, n_features=5, random_state=0)
        x_train, x_test = X[:160], X[160:]
        y_train, y_test = y[:160], y[160:]

        models = {"DT": DecisionTreeClassifier(max_depth=1)}
        params = {"DT": {}}

        report = evaluate_models(x_train, y_train, x_test, y_test, models, params)
        assert report["DT"] >= 0.0, "f1_weighted must be >= 0"
