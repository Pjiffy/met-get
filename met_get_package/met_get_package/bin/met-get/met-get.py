#!/usr/bin/env python3

import argparse
import requests

API_KEY = "I9pDpPLfzjwuw48MPGw5ss4Or83SlksdbF-4yzeUQ-k"  # Replace with your AVWX API key

def get_metar(station_id):
    response = requests.get(f"https://avwx.rest/api/metar/{station_id}", headers={"Authorization": API_KEY})
    if response.status_code == 200:
        data = response.json()
        print(data["raw"])
    else:
        print("Error: Could not retrieve METAR data")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("station_id", help="Station ID for the desired airport")
    args = parser.parse_args()

    get_metar(args.station_id)

