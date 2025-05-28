# Weather Data Analysis and Prediction

This project analyzes historical weather data and predicts future temperature trends using time series analysis and machine learning techniques.

## Features

- Historical weather data analysis
- Temperature trend visualization
- Time series forecasting
- Seasonal decomposition
- Temperature prediction models

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the analysis:
```bash
python weather_analysis.py
```

## Project Structure

- `weather_analysis.py`: Main script for data analysis and prediction
- `requirements.txt`: Project dependencies
- `data/`: Directory for storing weather data
- `models/`: Directory for saved prediction models

## Data Sources

The project uses historical weather data that can be obtained from various sources:
- NOAA Climate Data Online
- OpenWeatherMap API
- Local weather stations

## Analysis Components

1. Data Preprocessing
   - Handling missing values
   - Data normalization
   - Time series decomposition

2. Visualization
   - Temperature trends
   - Seasonal patterns
   - Year-over-year comparisons

3. Prediction Models
   - ARIMA/SARIMA models
   - Prophet forecasting
   - Machine learning regression

## License

MIT License 