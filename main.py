"""
Space Weather Dashboard
Main file to integrate data retrieval, analysis, and visualization.
"""

from utils.data_retrieval import get_noaa_data
from utils.data_analysis import predict_solar_events
from utils.data_visualization import visualize_solar_activity

def main():
    print("Fetching solar data from NOAA...")
    solar_data = get_noaa_data()
    if not solar_data:
        print("Failed to retrieve solar data. Please check your API connection.")
        return

    print("Analyzing solar event probabilities...")
    predictions = predict_solar_events(solar_data)

    print("Generating visualizations...")
    visualize_solar_activity(solar_data, predictions)
    print("Dashboard complete!")

if __name__ == "__main__":
    main()
