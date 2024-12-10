"""
Data Visualization
Module for visualizing solar data and predictions using Seaborn and SunPy.
"""

import seaborn as sns
import matplotlib.pyplot as plt

def visualize_solar_activity(data, predictions):
    """
    Visualizes solar activity trends and predictions.

    Args:
        data (DataFrame): Solar activity data.
        predictions (np.array): Solar event predictions.
    """
    try:
        # Add predictions to the dataset
        data["prediction"] = predictions

        # Plotting trends
        plt.figure(figsize=(12, 6))
        sns.lineplot(x="time", y="xray_flux", data=data, label="X-ray Flux")
        sns.lineplot(x="time", y="proton_flux", data=data, label="Proton Flux")
        sns.lineplot(x="time", y="electron_flux", data=data, label="Electron Flux")

        # Adding predictions
        plt.scatter(data["time"], data["prediction"], color="red", label="Predicted Events")

        plt.title("Solar Activity Trends and Predictions")
        plt.xlabel("Time")
        plt.ylabel("Flux / Predictions")
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error in visualization: {e}")
