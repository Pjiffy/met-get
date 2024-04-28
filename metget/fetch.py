import requests
from formatter import taf_format

AVWX_API_key = " "  # COPY API KEY HERE


def mfetch(station_id: str):
    """Returns a metar from the given station id
    """
    response = requests.get(f"https://avwx.rest/api/metar/{station_id}",
                            headers={"Authorization": AVWX_API_key})
    if response.status_code == 200:
        data = response.json()
        print(data["raw"])
    else:
        print(f"Error: {response.status_code}")


def tfetch(station_id: str):
    """Returns a taf from the given station id.
    """
    response = requests.get(f"https://avwx.rest/api/taf/{station_id}",
                            headers={"Authorization": AVWX_API_key})
    if response.status_code == 200:
        data = response.json()
        print(taf_format(data["raw"]))
    else:
        print(f"Error: {response.status_code}")
