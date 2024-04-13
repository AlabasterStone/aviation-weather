import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/{searchID}")
def read_root(searchID):
    METERs_data = requests.get(f"https://aviationweather.gov/cgi-bin/data/metar.php?ids={searchID}")
    TAFs_data = requests.get(f"https://aviationweather.gov/cgi-bin/data/taf.php?ids={searchID}")
    return METERs_data.content+TAFs_data.content
