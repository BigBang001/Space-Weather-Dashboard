"""
Data Retrieval
Module for fetching real-time solar and geomagnetic data from NOAA APIs.
"""

import requests
import pandas as pd

NOAA_API_URL = "https://services.swpc.noaa.gov/json/goes/primary.json"

def get_noaa_data():
    """
    Fetches solar data from NOAA's API.

    Returns:
        DataFrame: Processed solar data or None if the request fails.
    """
    try:
        response = requests.get(NOAA_API_URL)
        response.raise_for_status()
        data = response.json()

        # Extracting relevant fields
        processed_data = [
            {
                "time": item["time_tag"],
                "xray_flux": item.get("xray", {}).get("flux", None),
                "proton_flux": item.get("proton", {}).get("flux", None),
                "electron_flux": item.get("electron", {}).get("flux", None),
            }
            for item in data
        ]
        df = pd.DataFrame(processed_data)
        df["time"] = pd.to_datetime(df["time"])
        return df
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return None
