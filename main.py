from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import random

app = FastAPI()

# CORS Middleware (Bütün kaynaklara izin veriyor)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend'den gelen isteklere izin ver
    allow_credentials=True,
    allow_methods=["GET"],  # Sadece GET isteklerine izin ver
    allow_headers=["*"],
)

# **Ülke Verileri (Bayrak URL'leri ile)**
data = {
    "Country": ["Brazil", "France", "Argentina", "Germany", "Spain", "Belgium", "Portugal",
                "Netherlands", "Turkey", "England", "Italy", "Croatia", "Uruguay", "Denmark", "Morocco", "Sweden",
                "Algeria", "Colombia", "Côte d’Ivoire", "Bosnia and Herzegovina", "Cameroon", "Chile", "Czech Republic",
                "Nigeria", "Norway", "Poland", "Senegal", "Serbia", "Switzerland", "United States", "Austria", "Egypt",
                "Ghana", "South Korea", "Mexico", "Ukraine"],
    "Index": [10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 6, 6, 6, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    "Flag": [
        "https://flagcdn.com/w320/br.png", "https://flagcdn.com/w320/fr.png", "https://flagcdn.com/w320/ar.png",
        "https://flagcdn.com/w320/de.png", "https://flagcdn.com/w320/es.png", "https://flagcdn.com/w320/be.png",
        "https://flagcdn.com/w320/pt.png", "https://flagcdn.com/w320/nl.png", "https://flagcdn.com/w320/tr.png",
        "https://flagcdn.com/w320/gb.png", "https://flagcdn.com/w320/it.png", "https://flagcdn.com/w320/hr.png",
        "https://flagcdn.com/w320/uy.png", "https://flagcdn.com/w320/dk.png", "https://flagcdn.com/w320/ma.png",
        "https://flagcdn.com/w320/se.png", "https://flagcdn.com/w320/dz.png", "https://flagcdn.com/w320/co.png",
        "https://flagcdn.com/w320/ci.png", "https://flagcdn.com/w320/ba.png", "https://flagcdn.com/w320/cm.png",
        "https://flagcdn.com/w320/cl.png", "https://flagcdn.com/w320/cz.png", "https://flagcdn.com/w320/ng.png",
        "https://flagcdn.com/w320/no.png", "https://flagcdn.com/w320/pl.png", "https://flagcdn.com/w320/sn.png",
        "https://flagcdn.com/w320/rs.png", "https://flagcdn.com/w320/ch.png", "https://flagcdn.com/w320/us.png",
        "https://flagcdn.com/w320/at.png", "https://flagcdn.com/w320/eg.png", "https://flagcdn.com/w320/gh.png",
        "https://flagcdn.com/w320/kr.png", "https://flagcdn.com/w320/mx.png", "https://flagcdn.com/w320/ua.png"
    ]
}

df = pd.DataFrame(data)

# **Şartı Sağlayan Rastgele 4 Ülke Seçme**
def select_countries(min_total=22):
    while True:
        selected = df.sample(4, random_state=None)
        if selected["Index"].sum() >= min_total:
            return selected.to_dict(orient="records")

@app.get("/random-countries")
async def get_random_countries():
    return {"selected_countries": select_countries()}
