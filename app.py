import requests
from fastapi import FastAPI

app = FastAPI()

origins = [
    "github.io",
]

# 后台api允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_data")
def read_root(searchID):
    METERs_data = requests.get(f"https://aviationweather.gov/cgi-bin/data/metar.php?ids={searchID}")
    TAFs_data = requests.get(f"https://aviationweather.gov/cgi-bin/data/taf.php?ids={searchID}")
    return METERs_data.content+TAFs_data.content
