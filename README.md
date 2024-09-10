# Summer Heatwave Alert System

This project is a Flask-based web application that uses machine learning to predict heatwaves and send alerts via a web/mobile interface.

## Features
- Predict heatwaves using machine learning.
- User-friendly web interface.
- Real-time prediction and alerts.

## Requirements
Install the necessary dependencies using:

```bash
pip install -r requirements.txt
```
## To run the Flask app, execute: run the app

```bash
python app.py
```
## Dataset

```bash
For the dataset, you can find a weather dataset with features like temperature, humidity, wind speed, and possibly heatwave information from platforms such as:

Kaggle - Weather datasets
NOAA - National Weather Service datasets
OpenWeather API (for real-time data if you want to collect your own)
A good example dataset is Daily Climate Time Series Data, which contains weather variables and can be adapted for heatwave prediction.

To download and prepare your dataset, do the following:

Go to Kaggle or another data source.
Download a weather dataset that contains temperature, humidity, wind speed, and any other relevant features.
Ensure the dataset has a "heatwave" or similar column indicating whether a heatwave occurred (binary: 0 for no heatwave, 1 for heatwave).
Rename it to heatwave_data.csv and place it in your project folder.
```
## File Structure
```bash
heatwave_prediction.py: Script for training the machine learning model.
app.py: Flask app for heatwave alerts.
static/: Static files for the web interface.
templates/: HTML templates for rendering web pages.
models/: Contains the trained model.
```
