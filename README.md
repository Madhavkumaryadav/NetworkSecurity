# 🛡️ Network Security — Phishing & Intrusion Detection System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688)](https://fastapi.tiangolo.com/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2)](https://mlflow.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Storage-47A248)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end machine learning project that detects **phishing websites** and malicious network activity. It covers the full ML lifecycle: data ingestion from MongoDB, schema validation, transformation, model training, experiment tracking with MLflow, and batch inference through a web API.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Docker](#-docker)
- [Experiment Tracking](#-experiment-tracking)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🔎 Overview

Phishing and network-based attacks remain among the most common security threats. This project trains a binary classifier that labels a sample as **benign** or **malicious/phishing** from engineered URL and network features.

The codebase is organised as an installable Python package (`networksecurity`) with a modular, component-based training pipeline, so each stage (ingestion → validation → transformation → training) can be run, tested, and extended independently.

## ✨ Key Features

- **Modular ML pipeline** – separate components for data ingestion, validation, transformation, and model training
- **Pre-trained model artifacts** – saved preprocessor and model in `final_models/` for immediate inference
- **Batch prediction** – upload a CSV and receive predictions for every row, rendered as an HTML table and saved to disk
- **On-demand training** – retrain the model by calling a single API endpoint
- **MongoDB integration** – raw data is pushed to and read from a MongoDB collection
- **MLflow experiment tracking** – parameters, metrics, and models are logged for comparison
- **Custom logging & exception handling** – consistent error reporting across the package
- **Docker support** and **CI workflow** (GitHub Actions) included

## 🏗️ Architecture

```
 CSV Dataset ──► push_data.py ──► MongoDB
                                    │
                                    ▼
                          Data Ingestion
                                    │
                                    ▼
                          Data Validation  ◄── data_schema/
                                    │
                                    ▼
                        Data Transformation
                                    │
                                    ▼
                  Model Training + MLflow Tracking
                                    │
                                    ▼
              final_models/ (preprocessor + model)
                                    │
                                    ▼
          FastAPI  ──►  /predict (CSV in, predictions out)
```

## 🧰 Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.8+ |
| ML / Data | scikit-learn, pandas, numpy, joblib |
| API | FastAPI, Uvicorn, Jinja2 |
| Database | MongoDB (`pymongo`) |
| Experiment Tracking | MLflow (with DagsHub support) |
| DevOps | Docker, GitHub Actions |

## 📂 Project Structure

```
NetworkSecurity/
├── .github/workflows/      # CI/CD workflow definitions
├── networksecurity/        # Core package
│   ├── components/         # Ingestion, validation, transformation, training
│   ├── constant/           # Pipeline constants (DB / collection names, etc.)
│   ├── entity/             # Config and artifact entities
│   ├── exception/          # Custom exception handling
│   ├── logger/             # Logging setup
│   ├── pipeline/           # Training pipeline orchestration
│   └── utils/              # main_utils (I/O helpers), ml_utils (model/estimator)
├── Network_Data/           # Source dataset(s)
├── data_schema/            # Schema used for data validation
├── valid_data/             # Validated data output
├── final_models/           # Saved preprocessor and trained model
├── prediction_output/      # Output CSV from batch predictions
├── templates/              # HTML templates for prediction results
├── app.py                  # FastAPI application (train / predict endpoints)
├── main.py                 # Pipeline entry point
├── push_data.py            # Loads dataset into MongoDB
├── test_mongodb.py         # MongoDB connectivity check
├── mlflow.db               # Local MLflow tracking store
├── setup.py                # Package setup
├── requirements.txt        # Dependencies
├── Dockerfile              # Container definition
└── README.md
```

> Folders such as `build/`, `dist/` and `NetworkSecurity.egg-info/` are packaging artifacts generated by `setup.py`.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher (3.11 / 3.12 recommended)
- Git
- A MongoDB instance (e.g., MongoDB Atlas) if you want to run ingestion/training

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Madhavkumaryadav/NetworkSecurity.git
cd NetworkSecurity

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
MONGODB_URL_KEY=your_mongodb_connection_string
```

> ⚠️ Never commit your `.env` file or credentials. Rotate any key that has been exposed.

### (Optional) Load data into MongoDB

```bash
python test_mongodb.py   # verify connection
python push_data.py      # push the dataset into MongoDB
```

## 🧪 Usage

### Run the API

```bash
python app.py
```

The server starts at **http://localhost:8000** and redirects to the interactive Swagger docs at **/docs**.

### Train the model

Open `http://localhost:8000/train` (or use the Swagger UI). This runs the full pipeline and saves artifacts to `final_models/`.

### Run predictions

1. Open `http://localhost:8000/docs`
2. Choose **POST /predict**
3. Upload a CSV containing the same features the model was trained on
4. Results are displayed as a table and saved to `prediction_output/output.csv`

## 📡 API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Redirects to the Swagger documentation |
| `GET` | `/train` | Runs the complete training pipeline |
| `POST` | `/predict` | Accepts a CSV file and returns predictions |

**cURL example**

```bash
curl -X POST "http://localhost:8000/predict" \
     -F "file=@sample.csv"
```

## 🐳 Docker

```bash
docker build -t networksecurity .
docker run -p 8000:8000 --env-file .env networksecurity
```

## 📈 Experiment Tracking

Training runs are logged with MLflow. To explore them locally:

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Then visit **http://localhost:5000**. Remote tracking via DagsHub is also supported.

## 🗺️ Roadmap

- [ ] Add model evaluation visuals (confusion matrix, ROC curve, PR curve)
- [ ] Add explainability with SHAP / LIME
- [ ] Improve input validation and feature documentation
- [ ] Add unit and integration tests to the CI pipeline
- [ ] Add a single-sample prediction form
- [ ] Support real-time traffic analysis (Scapy / PyShark)
- [ ] Restrict CORS and remove debug prints / secret logging for production use

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push the branch: `git push origin feature/your-feature`
5. Open a Pull Request

Bug reports and feature ideas can be filed under [Issues](https://github.com/Madhavkumaryadav/NetworkSecurity/issues).

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

## 👤 Author

**Madhav Kumar Yadav**
GitHub: [@Madhavkumaryadav](https://github.com/Madhavkumaryadav)

---

⭐ If you find this project useful, consider giving it a star!
