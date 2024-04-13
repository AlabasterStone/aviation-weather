import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    METERs_data = requests.get("https://aviationweather.gov/cgi-bin/data/metar.php?ids=ZBAA")
    TAFs_data = requests.get("https://aviationweather.gov/cgi-bin/data/taf.php?ids=ZBAA")
    return METERs_data.content+TAFs_data.content
