# Network Security - Phishing & Intrusion Detection System

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/Madhavkumaryadav/NetworkSecurity/actions/workflows/main.yml/badge.svg)](https://github.com/Madhavkumaryadav/NetworkSecurity/actions)

A machine learning-based system to detect **phishing websites** and malicious network activity using standard phishing and network intrusion datasets.

The project includes a full ML training pipeline, experiment tracking with MLflow, data storage with MongoDB, a FastAPI web server for predictions, and a Docker-ready deployment setup.

## Features

- Pre-trained ML model for binary classification (Legitimate vs Phishing)
- Batch prediction via CSV file upload (REST API endpoint)
- Reusable `BatchPrediction` pipeline module
- MLflow integration for experiment tracking (with DagsHub remote)
- Data drift detection using the Kolmogorov-Smirnov test
- MongoDB support for storing raw data (optional — local CSV also supported)
- Docker-ready setup
- GitHub Actions CI with lint and test steps

## Project Structure

```
NetworkSecurity/
├── app.py                    # FastAPI web server (train + predict endpoints)
├── main.py                   # CLI entry point for the full training pipeline
├── requirements.txt          # Python dependencies
├── Dockerfile                # Container configuration
├── data_schema/
│   └── schema.yaml           # Feature definitions (30 columns + target)
├── final_models/             # Saved trained models (.pkl)
├── prediction_output/        # Batch prediction output CSVs
├── templates/                # Jinja2 HTML templates for prediction table
├── tests/                    # Unit tests (pytest)
├── networksecurity/          # Core package
│   ├── components/           # Data ingestion, validation, transformation, training
│   ├── pipeline/             # TrainingPipeline + BatchPrediction
│   ├── utils/                # Helper functions (YAML, pickle, numpy, evaluation)
│   ├── entity/               # Config and artifact dataclasses
│   ├── exception/            # Custom exception with traceback details
│   ├── logger/               # File-based logger
│   └── constant/             # Pipeline-wide constants
└── .github/workflows/        # CI/CD workflow (lint + test)
```

## Installation

### Prerequisites

- Python 3.11 (recommended)
- Git

### Steps

1. Clone the repository

   ```bash
   git clone https://github.com/Madhavkumaryadav/NetworkSecurity.git
   cd NetworkSecurity
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux / macOS
   # venv\Scripts\activate       # Windows
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Set up environment variables

   Create a `.env` file in the root folder:

   ```
   MONGODB_URL_KEY=your_mongodb_connection_string
   MONGO_DB_URL=your_mongodb_connection_string
   ```

## Running the Application

### FastAPI Web Server

```bash
python app.py
```

The server starts at `http://localhost:8000`.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/`      | GET    | Redirects to interactive API docs (`/docs`) |
| `/train` | GET    | Runs the full training pipeline |
| `/predict` | POST | Upload a CSV to get batch predictions |

### Training Pipeline (CLI)

```bash
python main.py
```

Runs data ingestion → validation → transformation → model training. Artifacts are saved under `artifacts/`.

### Batch Prediction (Python API)

```python
from networksecurity.pipeline.batch_prediction import BatchPrediction

bp = BatchPrediction(input_file_path="path/to/features.csv")
output_path = bp.initiate_batch_prediction()
print(f"Predictions written to: {output_path}")
```

### Docker

```bash
docker build -t network-security .
docker run -p 8000:8000 network-security
```

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

## Technologies Used

| Category | Technologies |
|----------|-------------|
| Core ML | Python, scikit-learn, pandas, numpy |
| Web API | FastAPI, Uvicorn |
| Experiment Tracking | MLflow, DagsHub |
| Database | MongoDB (pymongo) |
| Containerization | Docker |
| CI/CD | GitHub Actions |

## Roadmap / Future Improvements

- Add SHAP/LIME model explainability
- Support real-time network traffic analysis (scapy/pyshark)
- Add confusion matrix and ROC curve visualizations
- Improve input validation with Pydantic models
- Expand unit test coverage
- Add model performance comparison dashboard

## Contributing

Contributions are welcome!

- Open an issue if you find bugs or have feature ideas
- Submit pull requests for fixes or improvements
- Improve documentation