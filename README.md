# Network Security - Phishing & Intrusion Detection System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-success)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A machine learning-based system to detect **phishing websites** and malicious network activity using standard phishing and network intrusion datasets.

The project includes model training, experiment tracking with MLflow, data storage with MongoDB, and a user-friendly web interface built with Streamlit.

## Features

- Pre-trained ML model for binary classification (benign vs malicious/phishing)
- Batch prediction via CSV file upload
- Basic manual input for single-sample testing
- MLflow integration for experiment tracking
- MongoDB support for storing processed data (optional)
- Docker-ready setup
- Attempted FastAPI backend (currently under refactoring)

## Project Structure
NetworkSecurity/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Project dependencies
├── final_models/             # Saved trained models (.pkl, .joblib)
├── mlruns/                   # MLflow experiment tracking artifacts
├── Network_Data/             # Sample or processed datasets
├── valid_data/               # Validated/featured data
├── networksecurity/          # Core package
│   ├── components/           # Data ingestion, validation, model training
│   ├── pipeline/             # Training & prediction pipelines
│   └── utils/                # Helper functions
├── Dockerfile                # Container configuration
├── .env                      # Environment variables (gitignored)
├── .gitignore
└── README.md

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Steps

1. Clone the repository

   ```bash
   git clone https://github.com/Madhavkumaryadav/NetworkSecurity.git
   cd NetworkSecurity
Create and activate a virtual environment

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
Install dependencies

pip install -r requirements.txt
(Optional) Set up environment variables

Create a .env file in the root folder and add your MongoDB connection string if you're using the database features:

MONGODB_URL=your_mongodb_connection_string
Run the application

streamlit run app.py
The app should open in your browser at http://localhost:8501.

Usage
Batch Prediction
Go to the "Batch Prediction" section
Upload a CSV file containing the required features
Click "Predict" to get results for all rows
Single Sample Prediction
Enter feature values manually
Submit to see the prediction result
Note: Make sure your input data matches the features your model was trained on.

Deployment
The app is intended to be deployed on Streamlit Community Cloud.

Current known issue: Deployment fails on Python 3.13 due to dependency build errors (especially with catboost and protobuf).
Workaround (recommended):

Add a file named .python-version in the root with content:
3.11
Or manually set Python version to 3.11/3.12 in Streamlit Cloud app settings
After fixing, reboot the app from the dashboard.

Technologies Used
Core: Python, scikit-learn, pandas, numpy, joblib
Web Interface: Streamlit
Experiment Tracking: MLflow + DagsHub
Database: MongoDB (via pymongo)
API Layer (partial): FastAPI + Uvicorn
Containerization: Docker
Roadmap / Future Improvements
Fix Streamlit Cloud deployment compatibility
Remove FastAPI code from Streamlit app (move to separate backend if needed)
Add model performance metrics and visualizations (confusion matrix, ROC curve)
Improve input validation and feature documentation
Add SHAP/LIME explainability for predictions
Support real-time network traffic analysis (scapy/pyshark integration)
Better error handling and user feedback
Contributing
Contributions are welcome!
Please feel free to:

Open an issue if you find bugs or have feature ideas
Submit pull requests for fixes or improvements
Improve documentation