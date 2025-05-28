import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from datetime import datetime
import os

def get_weather_data(city="London"):
    """Get current weather data from OpenWeatherMap API"""
    api_key = "06ce023c0be29621fc47e5dee774329b"
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            weather = data['weather'][0]['description']
            print(f"\nCurrent Weather in {city}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {weather}")
            return temp
        else:
            print(f"Error: {data['message']}")
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def generate_weather_data(days=30, base_temp=15):
    """Generate synthetic weather data"""
    dates = pd.date_range(end=datetime.now(), periods=days)
    temperatures = np.random.normal(base_temp, 5, days) + 10 * np.sin(np.linspace(0, 4*np.pi, days))
    
    df = pd.DataFrame({
        'date': dates,
        'temperature': temperatures
    })
    df.set_index('date', inplace=True)
    return df

def plot_temperature(df, city):
    """Plot temperature data"""
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['temperature'])
    plt.title(f'Temperature Trend in {city}')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    plt.savefig('data/temperature_trend.png')
    plt.close()
    print("\nTemperature trend plot saved as 'data/temperature_trend.png'")

def main():
    # Get city from user
    city = input("Enter city name (default: London): ").strip() or "London"
    
    # Get current weather
    current_temp = get_weather_data(city)
    
    # Generate weather data
    if current_temp is not None:
        print("\nGenerating weather data based on current temperature...")
        df = generate_weather_data(base_temp=current_temp)
    else:
        print("\nUsing default temperature for data generation...")
        df = generate_weather_data()
    
    # Plot the data
    print("\nGenerating temperature plot...")
    plot_temperature(df, city)
    
    # Show statistics
    print("\nTemperature Statistics:")
    print(f"Mean Temperature: {df['temperature'].mean():.2f}°C")
    print(f"Max Temperature: {df['temperature'].max():.2f}°C")
    print(f"Min Temperature: {df['temperature'].min():.2f}°C")
    print(f"Temperature Std Dev: {df['temperature'].std():.2f}°C")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please make sure you have all required packages installed:")
        print("pip install numpy pandas matplotlib requests") 