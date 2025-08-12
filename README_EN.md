# FLO CLTV Prediction

🇺🇸 **English Version** | 🇹🇷 **[Türkçe Versiyon](README.md)**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
Professional Customer Lifetime Value (CLTV) prediction, segmentation, automated reporting, and API service for FLO customers using advanced analytics and machine learning.

## Features
- **CLTV Calculation & Segmentation**: Advanced lifetime value prediction with customer segmentation
- **Automated Reporting**: Dynamic markdown reports with visualizations
- **REST API Service**: FastAPI-powered endpoints for real-time predictions
- **Interactive Dashboard**: Streamlit-based web interface
- **Testing Infrastructure**: Comprehensive test suite with quality assurance
- **Docker Support**: Containerized deployment ready
- **CI/CD Integration**: Automated testing and quality control

## Quick Start

### Installation
```bash
git clone https://github.com/hakancelik/FLO_cltv_prediction.git
cd FLO_cltv_prediction
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
pip install fastapi uvicorn streamlit pytest flake8 invoke
```

### Usage

#### Command Line Interface
```bash
python main.py
```
Outputs and reports are generated in `report/` and `screen/` directories.

#### API Service
```bash
python -m uvicorn main_api:app --reload
```
**Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

#### API Endpoints
- `POST /predict_cltv/`: Upload CSV file, get CLTV and segment predictions

**Example cURL:**
```bash
curl -X POST "http://127.0.0.1:8000/predict_cltv/" \
     -F "file=@data/flo_data_20k.csv"
```

#### Interactive Dashboard
```bash
python -m streamlit run dashboard.py
```
Web interface for file upload, visualization, and result download.

## Automated Reporting
Every execution automatically updates `report/report.md` with:
- **Statistical Summary**: Comprehensive data analysis
- **Segment Distribution**: Customer segmentation insights
- **CLTV Distribution**: Value distribution with visualizations
- **Model Parameters**: Technical model information

## Project Structure
```
FLO_cltv_prediction/
├── main.py                 # Command line main script
├── main_api.py             # FastAPI REST service
├── dashboard.py            # Streamlit web interface
├── tasks.py                # Automation commands (invoke)
├── config.py               # Configuration parameters
├── scripts/                # Core modules
│   ├── data_processing.py  # Data preprocessing pipeline
│   ├── modeling.py         # ML model fitting and prediction
│   ├── segmentation.py     # Customer segmentation
│   ├── visualization.py    # Chart generation
│   ├── pipeline.py         # End-to-end pipeline
│   └── reporting.py        # Automated report generation
├── tests/                  # Automated test suite
├── report/                 # Generated reports and visualizations
├── screen/                 # Generated charts
├── data/                   # Raw data files
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
├── .github/workflows/      # CI/CD pipelines
└── README.md               # Project documentation
```

## Automation Commands
```bash
# Testing & Quality
invoke test        # Run all tests
invoke lint        # Code quality check
invoke all-tests   # Complete quality assurance

# Execution
invoke run         # Command line execution
invoke api         # Start API service
invoke dashboard   # Launch web interface

# Setup
invoke install     # Install all dependencies
```

## Testing
```bash
# Run all tests
pytest

# Code quality check
flake8 scripts/

# Complete test suite
invoke all-tests
```

## Docker Deployment
```bash
# Build image
docker build -t flo-cltv .

# Run container
docker run -p 8000:8000 flo-cltv
```

**Access API**: [http://localhost:8000/docs](http://localhost:8000/docs)

## CI/CD Integration
GitHub Actions workflow included for:
- Automated testing on push/PR
- Code quality validation
- Multi-environment compatibility

## Development
See [DEVELOPMENT_GUIDE_EN.md](DEVELOPMENT_GUIDE_EN.md) for step-by-step development instructions.

## API Documentation
### POST /predict_cltv/
Upload customer data CSV and receive CLTV predictions with segmentation.

**Request**: Multipart form with CSV file
**Response**: JSON array with CLTV values and customer segments

**Example Response**:
```json
[
  {"cltv": 245.67, "cltv_segment": "A"},
  {"cltv": 123.45, "cltv_segment": "B"}
]
```

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`invoke all-tests`)
4. Commit changes (`git commit -m 'Add amazing feature'`)
5. Push to branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## Requirements
- Python 3.10+
- Dependencies listed in `requirements.txt`
- Optional: Docker for containerized deployment

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors
- **hakancelik** - *Initial work* - [GitHub](https://github.com/hakancelik)

## Acknowledgments
- FLO dataset for CLTV analysis
- Lifetimes library for CLV modeling
- FastAPI and Streamlit communities
